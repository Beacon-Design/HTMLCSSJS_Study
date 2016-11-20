/*
This is empty on purpose! Your code to build the resume will go here.
 */
 // $("#main").innerhtml("good");
 $("#main").append("jim");

 var email = "a@123.com";
 var newEmail = email.replace("a","123");
 console.log(email);
 console.log(newEmail);

var skills=["0","1","2"];
 $("#main").append(skills[0]);

// this is object
var work={
	"name" : "Tom",
	"age" : 13,
	"skills": skills
} ;

var job={};
job["first"]="cook";
job["second"]="fish";
job.third = "farmer";

$("#main").append(job.first,job.second,job["third"]);

// this is JSON
var member={
	"no1":"ONE",
	"no2":2,
	"no3":["3-1","3-2","3-3"],
	"no4":"www.baidu.com",
	"no5":[
	{
		"fiveA":"this is fiveA",
		"fiveB":1900,
		"fiveC":["apple","banana"]
	},
	{
		"book":"tree",
		"beer":false,
		"top":null
	}

	]

};

$("#main").append(member.no4);
$("#main").append(member.no5[0].fiveA);