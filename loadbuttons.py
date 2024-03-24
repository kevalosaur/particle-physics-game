import particledata
from pyscript import document

buttondiv = document.querySelector('#buttons')

for particle in particledata.PARTICLES:
    buttondiv.innerHTML += f'<button class="particle-button" id={particle.ident}>{particle.symbol}<span class="particle-tooltip">{particle.desc_text()}</span></button>'