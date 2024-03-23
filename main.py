from pyscript import document, window
from particledata import *
from generator import *
from diagramtosvg import convert_diagram

window.console.log("test!")

env = Env(-100, 100, -100, 100, 10)

test_object = propagate(PHOTON, -50, 60, 100, 20, env) + propagate(POSITRON, -50, 60, 100, 30, env) + propagate(ELECTRON, -50, 60, 90, 40, env)

# test_object = [Trail(ELECTRON, LinePath(-50, 60, -20, 20)), Trail(ELECTRON, CirclePath(-50, 60, 50, 1.57, 3.14))]

document.querySelector('#svghere').innerHTML = convert_diagram(test_object)