
function topDown() {
    document.getElementsByTagName('section')[0].setAttribute("id", "ani");

}
function downTop() {
    document.getElementsByTagName("section")[0].removeAttribute("id");
}
function easeInOutBack() {
    document.getElementsByTagName("section")[0].style.transitionTimingFunction="cubic-bezier(0.68,-0.55,0.265,1.55)";
    document.getElementsByTagName("section")[0].innerHTML="easeInOutBack";
    document.getElementsByTagName("section")[0].style.backgroundColor="green";
    

}
function easeOutBack() {
    var e = document.getElementsByTagName("section")[0]
    e.style.transitionTimingFunction="cubic-bezier(0.175,0.885,0.32,1.275)";
    e.style.backgroundColor="pink";
    e.innerHTML="easeOutBack";
    
    var c = document.getElementById("copy")
    c.innerHTML="easeOutBack";
}

function easeInOutCubic(){
    var name = "easeInOutCubic" //ease name
    var number = "0.47, 0, 0.745, 0.715" //ease value
    var cubic = "cubic-bezier(" + number + ")" //ease value for cubic-bezier
    var e = document.getElementsByTagName("section")[0] //toast element
    var easeName = document.getElementById("easeName") //output text of ease name
    var numberElement = document.getElementById("number") // output text of ease value
    e.innerHTML=name;
    e.style.transitionTimingFunction=cubic;
    e.style.backgroundColor="orange";
    
    easeName.innerHTML=name;
    numberElement.innerHTML=number;
    

}
