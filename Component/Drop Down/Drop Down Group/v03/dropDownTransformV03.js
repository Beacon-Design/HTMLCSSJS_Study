
function topDown() {
    document.getElementsByTagName('section')[0].setAttribute("id", "ani");

}
function downTop() {
    document.getElementsByTagName("section")[0].removeAttribute("id");
}
function easeInSine() {
//    (element: section tag )give an id by topdown function
    document.getElementById("ani").style.transitionTimingFunction="cubic-bezier(0.47, 0, 0.745, 0.715)";
    document.getElementById("ani").innerHTML="easeInSine";
    
//    document.getElementById("ani").style.backgroundColor="red";
    
    
//    this line work
//    document.getElementsByTagName("section")[0].style.backgroundColor="red";
//    this line work
//    document.getElementsByTagName("section")[0].style.transitionTimingFunction="cubic-bezier(0.175, 0.885, 0.32, 1.275)";
    
}
function easeOutSine() {
    var e = document.getElementById("ani")
    e.style.transitionTimingFunction="cubic-bezier(0.39, 0.575, 0.565, 1)";
    e.style.backgroundColor="pink";
    e.innerHTML="easeOutSine";
}
