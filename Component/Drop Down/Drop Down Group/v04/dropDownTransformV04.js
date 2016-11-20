
function topDown() {
    document.getElementsByTagName('section')[0].setAttribute("id", "ani");

}
function downTop() {
    document.getElementsByTagName("section")[0].removeAttribute("id");
}
function easeInOutBack() {
//    (element: section tag )give an id by topdown function
    document.getElementsByTagName("section")[0].style.transitionTimingFunction="cubic-bezier(0.68,-0.55,0.265,1.55)";
    document.getElementsByTagName("section")[0].innerHTML="easeInOutBack";
    document.getElementsByTagName("section")[0].style.backgroundColor="green";
    
//    document.getElementById("ani").style.backgroundColor="red";
    
    
//    this line work
//    document.getElementsByTagName("section")[0].style.backgroundColor="red";
//    this line work
//    document.getElementsByTagName("section")[0].style.transitionTimingFunction="cubic-bezier(0.175, 0.885, 0.32, 1.275)";
    
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
    var name = "easeInOutCubic"
    var number = "0.47, 0, 0.745, 0.715"
    var cubic = "cubic-bezier(" + number + ")"
    var e = document.getElementsByTagName("section")[0]
    var copy = document.getElementById("copy")
    e.innerHTML=name;
    e.style.transitionTimingFunction=cubic;
    e.style.backgroundColor="orange";
    
    copy.innerHTML=cubic;
    

}
