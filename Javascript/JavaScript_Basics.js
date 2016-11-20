// Function these are equivalent
var myFunc = function (param1,param2){
	code goes here
}

function myFunc(param1,param2){
	code goes here
} 

// call itself
(function (){return "12"})();



// Three Objects all equivalent
var bio={
	"name":"jim"
}

bio.name = "jim";
bio["name"] = "jim";