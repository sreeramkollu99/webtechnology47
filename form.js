var submit = document.getElementById("submitButton");

submit.addEventListener("click",function(){
	var firstName = document.getElementById("fname").value;
	var lastName = document.getElementById("lname").value;
	var mobileNumber = document.getElementById("mobile").value;
	var city = document.getElementById("city").value;
	var pincode = document.getElementById("pincode").value;
	var state = document.getElementById("state").value;
	// var reset = document.getElementById("resetButton");
	var alpha = /^[a-zA-Z]+$/;
	var number = /^[0-9]+$/;
	// console.log("Hello") 
	console.log(firstName);
	if(!firstName.match(alpha)||firstName.length>30){
		alert("Please Enter First Name In Specified Format");
		return;
	}
	if(!lastName.match(alpha)||lastName.length>30){
		alert("Please Enter Last Name In Specified Format");
		return;
	}
	if(!mobileNumber.match(number)||mobileNumber.length!=10){
		alert("Please Enter 10 digit Mobile Number");
		return;
	}
	if(!city.match(alpha)||city.length>30){
		alert("Please Enter City In Specified Format");
		return;
	}
	if(!pincode.match(number)||pincode.length!=6){
		alert("Please Enter 6 digit Pincode");
		return;
	}
	if(!state.match(alpha)||state.length>30){
		alert("Please Enter State In Specified Format");
		return;
	}
});