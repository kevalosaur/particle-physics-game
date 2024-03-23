from pyscript import document, window
from particledata import *
from generator import *
from diagramtosvg import convert_diagram

window.console.log("test!")

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

test_object = [Trail(ELECTRON, LinePath(-50, 60, -20, 20)), Trail(ELECTRON, CirclePath(-50, 60, 50, 1.57, 3.14))]

document.querySelector('#svghere').innerHTML = convert_diagram(test_object)