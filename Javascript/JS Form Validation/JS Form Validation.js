function validateTextbox(){
	var box1 = document.getElementById('name');
	var box2 = document.getElementById("address");
	var box3 = document.getElementById("phone");
	var box4 = document.getElementById("email");
	if (box1.value.length < 5 || box2.value < 5) {
		alert("enter a name");
		box1.focus();
		box1.style.border = "solid 2px red";
		return false;
	}
}