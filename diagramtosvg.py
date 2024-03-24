import math
from pyscript import document

SVG_HEIGHT = 400
SVG_WIDTH = 600

def polar_to_cartesian(cx, cy, radius, angle_radians):
    return cx + (radius * math.cos(angle_radians)), cy + (radius * math.sin(angle_radians))

def cartesian_to_web(x, y, h, w):
    return x+(w*.5), (h*.5)-y

def polar_to_web(cx, cy, radius, angle_radians, h, w):
    xc, yc = polar_to_cartesian(cx, cy, radius, angle_radians)
    return cartesian_to_web(xc, yc, h, w)

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
            x, y, r, t1, t2 = path.x, path.y, path.r, path.t1, path.t2
            isReflexArc = '1' if t2-t1 >= math.pi else '0'
            x1, y1 = polar_to_web(x, y, r, t1, SVG_HEIGHT, SVG_WIDTH)
            x2, y2 = polar_to_web(x, y, r, t2, SVG_HEIGHT, SVG_WIDTH)
            d = " ".join([
                "M", str(x1), str(y1),
                "A", str(r), str(r), '0', isReflexArc, '0', str(x2), str(y2),
            ])

        id = p.label
        if id in particle_bucket:
            particle_bucket[id] += 1
        else:
            particle_bucket[id] = 0
        id += str(particle_bucket[id])

        out += f"<path class=\"{p.label}\" id=\"{id}\" d=\"{d}\" />"

    out += "</svg>"
    return out