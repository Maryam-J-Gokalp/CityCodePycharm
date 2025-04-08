const password = $("#password").val().trim();
if ( password.length < 6) {
$("#password").next().text("Must be 6 or more characters.");
isValid = false;
} else {
$("#password").next().text("");
}
$("#password").val(password);
