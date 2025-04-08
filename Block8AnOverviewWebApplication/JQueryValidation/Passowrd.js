const password = $("#password").val().trim();
$("#password").val(password); // Always update the trimmed value

if (password === "") {
  $("#password").next().text("This field is required.");
  isValid = false;
} else if (password.length < 6) {
  $("#password").next().text("Must be 6 or more characters.");
  isValid = false;
} else {
  $("#password").next().text("");
}

