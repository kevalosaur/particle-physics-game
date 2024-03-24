import json
import math
import numpy as np
from pyscript import document

SVG_HEIGHT = 400
SVG_WIDTH = 600

def polar_to_cartesian(cx, cy, radius, angle_radians):
    return cx + (radius * np.cos(angle_radians)), cy + (radius * np.sin(angle_radians))

def cartesian_to_web(x, y, h, w):
    return x+(w*.5), (h*.5)-y

def polar_to_web(cx, cy, radius, angle_radians, h, w):
    xc, yc = polar_to_cartesian(cx, cy, radius, angle_radians)
    return cartesian_to_web(xc, yc, h, w)

def curve_func(t, R, a):
    return R*np.exp(-a*t)

def convert_diagram(diagram):
    particle_bucket = dict()

    out = f"<svg height=\"{SVG_HEIGHT}\" width=\"{SVG_WIDTH}\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\">"

    for p in diagram:
        path = p.path
        d = ""
        if path.mode == 'line':
            x1, y1, x2, y2 = path.x1, path.y1, path.x2, path.y2
            x1w, y1w = cartesian_to_web(x1, y1, SVG_HEIGHT, SVG_WIDTH)
            x2w, y2w = cartesian_to_web(x2, y2, SVG_HEIGHT, SVG_WIDTH)
            d = " ".join([
                "M", str(x1w), str(y1w),
                "L", str(x2w), str(y2w),
            ])
        elif path.mode == 'circle':
            x1, y1, x2, y2, r = path.x1, path.y1, path.x2, path.y2, path.r
            isReflexArc = '1' if t2-t1 >= np.pi else '0'
            isCounterclockwise = '1' if r < 0 else '0'
            r = abs(r)
            x1, y1 = polar_to_web(x, y, r, t1, SVG_HEIGHT, SVG_WIDTH)
            x2, y2 = polar_to_web(x, y, r, t2, SVG_HEIGHT, SVG_WIDTH)
            d = " ".join([
                "M", str(x1), str(y1),
                "A", str(r), str(r), '0', isReflexArc, isCounterclockwise, str(x2), str(y2),
            ])
        elif path.mode == 'spiral':
            x, y, r, s, t0, T, a = path.x, path.y, path.r, path.curve_sign, path.t0, path.t, path.a
            samples = math.ceil(T*30)
            ts = np.linspace(0, T, samples)
            xs, ys = curve_func(ts, r, a)*np.cos(s*ts+t0)+x, curve_func(ts, r, a)*np.sin(s*ts+t0)+y
            xsw, ysw = cartesian_to_web(xs, ys, SVG_HEIGHT, SVG_WIDTH)
            d = " ".join(sum([["M", str(xsw[0]), str(ysw[0])]] + [["L", str(xsw[i]), str(ysw[i])] for i in range(len(ts))], []))

        id = p.label
        if id in particle_bucket:
            particle_bucket[id] += 1
        else:
            particle_bucket[id] = 0
        id += str(particle_bucket[id])

        out += f"<path class=\"{p.label}\" id=\"{id}\" d=\"{d}\" onclick=\"check(\'{p.label}\')\"/>"

    out += "</svg>"
    return out