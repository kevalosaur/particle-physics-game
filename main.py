from pyscript import document, window
from particledata import *
from generator import *
from diagramtosvg import convert_diagram
import random

window.console.log("test!")

env = Env(-1000, 1000, -1000, 1000, 1)

test_object = []

for _ in range(random.randint(1, 3)):
    ident = random.choice(["e_n", "e_p", "mu_n", "mu_p"])
    x, y, px, py = random.random() * 200 - 100, random.random() * 200 - 100, random.random() * 200 - 100, random.random() * 200 - 100
    test_object += propagate(PARTICLES[ident], x, y, px, py, env)

document.querySelector('#svghere').innerHTML = convert_diagram(test_object)