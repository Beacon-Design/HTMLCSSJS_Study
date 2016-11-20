//add item <p>
function addItem(){

	var element=document.createElement("p");
	var main=document.getElementById("main");
	main.appendChild(element);
	var text=document.createTextNode("this is.");
	element.appendChild(text);

}

//remove item <p>
function removeItem(){
	var elementH=document.getElementsByTagName("p")[0];
	var parent=elementH.parentNode;
	parent.removeChild(elementH);
}

//set attribute id to h1
function setAttri(){
	var attributeSec=document.createAttribute("id");
	attributeSec.nodeValue="sec";
	var elementSec=document.getElementsByTagName("section")[0];
	elementSec.setAttributeNode(attributeSec);

	document.getElementsByTagName("h2")[0].setAttribute("class","cl");
}

//parent to child
function pToC(){
	var parent=document.getElementById("art");
	var fChild=parent.firstElementChild;
	fChild.style.backgroundColor="green";
	var lChild=parent.lastElementChild;
	lChild.style.backgroundColor="cyan";
}

//child to parent
function cToP(){
	var child=document.getElementById("hMid");
	var parent=child.parentElement;
	parent.style.color="yellow";

	document.getElementById("ptoc").parentNode.style.backgroundColor="gray";
}

//next sibling
function nextSiblingColor(){
	var me=document.getElementById("sib");
	var nextSibling=me.nextElementSibling;
	nextSibling.style.color="red";
}
//previous sibling
function previousSiblingColor(){
	var me=document.getElementById("sib");
	var previousSibling=me.previousElementSibling;
	previousSibling.style.color="blue";
}



