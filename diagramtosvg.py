import json
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

test_json = """{
    "particles": [
        {
            "label": "electron",
            "path": {
                "type": "line",
                "params": {
                    "x1": -50,
                    "y1": 60,
                    "x2": -20,
                    "y2": 20
                }
            }
        },
        {
            "label": "electron",
            "path": {
                "type": "circle",
                "params": {
                    "x": -50,
                    "y": 60,
                    "r": 50,
                    "t1": 1.57,
                    "t2": 3.14
                }
            }
        }
    ]
}"""

if __name__ == '__main__':
    # with open('diagramtemplate.json') as diagram_json:
    #     diagram_string = diagram_json.read()
    diagram_string = test_json
    diagram = json.loads(diagram_string)

    particle_bucket = dict()

    out = f"<svg height=\"{SVG_HEIGHT}\" width=\"{SVG_WIDTH}\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\">"

    for p in diagram['particles']:
        path = p['path']
        d = ""
        if path['type'] == 'line':
            x1, y1, x2, y2 = path['params']['x1'], path['params']['y1'], path['params']['x2'], path['params']['y2']
            x1w, y1w = cartesian_to_web(x1, y1, SVG_HEIGHT, SVG_WIDTH)
            x2w, y2w = cartesian_to_web(x2, y2, SVG_HEIGHT, SVG_WIDTH)
            d = " ".join([
                "M", str(x1w), str(y1w),
                "L", str(x2w), str(y2w),
            ])
        elif path['type'] == 'circle':
            x, y, r, t1, t2 = path['params']['x'], path['params']['y'], path['params']['r'], path['params']['t1'], path['params']['t2']
            isReflexArc = '1' if t2-t1 >= math.pi else '0'
            x1, y1 = polar_to_web(x, y, r, t1, SVG_HEIGHT, SVG_WIDTH)
            x2, y2 = polar_to_web(x, y, r, t2, SVG_HEIGHT, SVG_WIDTH)
            d = " ".join([
                "M", str(x1), str(y1),
                "A", str(r), str(r), '0', isReflexArc, '0', str(x2), str(y2),
            ])

        id = p['label']
        if id in particle_bucket:
            particle_bucket[id] += 1
        else:
            particle_bucket[id] = 0
        id += str(particle_bucket[id])

        out += f"<path class=\"{p['label']}\" id=\"{id}\" d=\"{d}\" stroke=\"black\" stroke-width=\"4\"/>"

    out += "</svg>"

    document.querySelector('#svghere').innerHTML = out