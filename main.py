from pyscript import document, window
from particledata import *
from generator import *
from diagramtosvg import convert_diagram

window.console.log("test!")

env = Env(-100, 100, -100, 100, 1)

test_object = propagate(ELECTRON, -50, 60, 30, 45, env) \
            + propagate(POSITRON, -50, 60, 15, 20, env)

document.querySelector('#svghere').innerHTML = convert_diagram(test_object)