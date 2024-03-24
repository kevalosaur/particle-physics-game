let activeButton;
let canvas;

document.addEventListener('mousedown', function(event) {
    let activeElement = event.target;
    console.log(activeElement.nodeName);
    if(activeElement.nodeName == 'BUTTON') {
        activeButton = activeElement;
    }
    else if(activeElement.nodeName == 'path') {
        let particleClicked = activeElement.className.baseVal;
        if(activeButton) {
            if(activeButton.id == particleClicked) {
                // correct answer! yay!
                activeElement.classList.add('correct');
    
                // check if all correct
                canvas = document.getElementById('canvas');
                let allCorrect = true
                canvas.childNodes.forEach((node) => {
                    allCorrect &&= node.classList.contains('correct');
                });
                if(allCorrect) {
                    alert('all correct');
                }
            }
            else {
                // wrong answer! boo!
                activeButton.classList.add('wrong');
                setTimeout(() => {
                    activeButton.classList.remove('wrong');
                }, 820);
            }
        }  
    }
});