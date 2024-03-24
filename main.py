from pyscript import document, window
from particledata import *
from generator import *
from diagramtosvg import convert_diagram

window.console.log("test!")

env = Env(-1000, 1000, -1000, 1000, 1)

test_object = propagate(PARTICLES['pi_n'], -100, 60, 5000, 4, env)

document.querySelector('#svghere').innerHTML = convert_diagram(test_object)