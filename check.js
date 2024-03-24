var activeButton;

function check(lineLabel){
    console.log(lineLabel+", "+activeButton)
    if(lineLabel == activeButton) {
        alert("Correct")
    }
    else {
        alert("Incorrect")
    }
}

document.addEventListener('mousedown', function(event) {
    if(event.target.nodeName == 'BUTTON') {
        activeButton = event.target.id;
    }
});