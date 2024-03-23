from pyscript import document, window
from particledata import *
from generator import *
from diagramtosvg import convert_diagram

window.console.log("test!")

test_object = [Trail(ELECTRON, LinePath(-50, 60, -20, 20)), Trail(ELECTRON, CirclePath(-50, 60, 50, 1.57, 3.14))]

document.querySelector('#svghere').innerHTML = convert_diagram(test_object)