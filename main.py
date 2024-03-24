from pyscript import document, window
from particledata import *
from generator import *
from diagramtosvg import convert_diagram

window.console.log("test!")

env = Env(-1000, 1000, -1000, 1000, 1)

test_object = propagate(PARTICLES['mu-'], -50, 60, 50, 45, env) \
            + propagate(PARTICLES['mu+'], -55, 70, -15, 70, env)

document.querySelector('#svghere').innerHTML = convert_diagram(test_object)