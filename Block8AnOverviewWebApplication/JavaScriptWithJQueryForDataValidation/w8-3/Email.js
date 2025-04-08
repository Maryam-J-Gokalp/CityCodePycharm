if  (email == "") {
$("#email").next().text("This field is required.");
isValid = false;
} else if ( !emailPattern.test(email) ) {
$("#email").next().text("Must be a valid email address.");
isValid = false;
} else {
$("#email").next().text("");
}
$("#email").val(email);
