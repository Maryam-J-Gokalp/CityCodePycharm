"use strict";
const clickSub = evt => {
    const h2Element = evt.currentTarget;                 
    const divElement = h2Element.nextElementSibling;     
    h2Element.classList.toggle("minus");
    divElement.classList.toggle("open");
    evt.preventDefault();   
};

document.addEventListener("DOMContentLoaded", () => {
    const h2Subs = document.querySelectorAll("#faqs h2");	    
    for (let h2E of h2Subs) {
        h2E.addEventListener("click", clickSub);
    }
    h2Subs[0].firstChild.focus();       
});

