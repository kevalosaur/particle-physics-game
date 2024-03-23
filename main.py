from pyscript import document, window
from particledata import *
from generator import *
from diagramtosvg import convert_diagram

window.console.log("test!")

env = Env(-100, 100, -100, 100, 1)

print(propagate(POSITRON, 0, 0, 100, 0, env))

test_object = [Trail(ELECTRON, LinePath(-50, 60, -20, 20)), Trail(ELECTRON, CirclePath(-50, 60, 50, 1.57, 3.14))]

document.querySelector('#svghere').innerHTML = convert_diagram(test_object)