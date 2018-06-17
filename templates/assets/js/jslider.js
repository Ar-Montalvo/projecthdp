/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */



var slider, slider1, slider2, slider3, slider4, output
slider   = document.getElementById("myRange");
output = document.getElementById("demo");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.innerHTML = this.value;
}
slider1 = document.getElementById("myRange1");
// Update the current slider value (each time you drag the slider handle)
slider1.oninput = function() {
    output.innerHTML = this.value;
}
slider2   = document.getElementById("myRange2");
// Update the current slider value (each time you drag the slider handle)
slider2.oninput = function() {
    output.innerHTML = this.value;
}
slider3   = document.getElementById("myRange3");
// Update the current slider value (each time you drag the slider handle)
slider3.oninput = function() {
    output.innerHTML = this.value;
}

/*
slider4   = document.getElementById("myRange4");
// Update the current slider value (each time you drag the slider handle)
slider4.oninput = function() {
    output.innerHTML = this.value;
}
*/
