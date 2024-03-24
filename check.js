let activeButton;

document.addEventListener('mousedown', function(event) {
    let activeElement = event.target;
    console.log(activeElement.nodeName);
    if(activeElement.nodeName == 'BUTTON') {
        activeButton = activeElement;
    }
    else if(activeElement.nodeName == 'path') {
        let particleClicked = activeElement.className.baseVal
        if(activeButton.id == particleClicked){
            // correct answer! yay!
            activeElement.classList.add('correct');
        }
        else {
            // wrong answer! boo!
            activeButton.classList.add('wrong');
            setTimeout(() => {
                activeButton.classList.remove('wrong');
            }, 820);
            // alert("incorrect");
        }
    }
});