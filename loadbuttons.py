import particledata
from pyscript import document

buttondiv = document.querySelector('#buttons')
buttonHTML = ""

for particle in particledata.PARTICLES:
    particle = particledata.PARTICLES[particle]
    put_bar = " antimatter-bar" if particle.ident in ['ve_bar', 'vmu_bar'] else ""
    buttonHTML += f'<button class="particle-button{put_bar}" id={particle.ident}>{particle.symbol}<span class="particle-tooltip">{particle.desc_text()}</span></button>'

buttondiv.innerHTML = buttonHTML