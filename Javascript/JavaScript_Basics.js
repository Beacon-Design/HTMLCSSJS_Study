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

//Two object all equivalent
var person = { firstname:"Tony", lastname:"Alice" };

person = new object();
person.first = "Tony";
person.lastname = "Alice";

//passing value
var tony ={name:"tony"};
function great(person){
    console.log("hi" + person.name);
}
great(tony);
great({name:"jim"});

//two all same
var english = {};
english.greeting = {};
english.greeting.great = "hello";


var english = {
    greeting: {
        greet: "hello"
    }
};
