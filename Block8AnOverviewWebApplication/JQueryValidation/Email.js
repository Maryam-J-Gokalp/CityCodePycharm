const email = $("#email").val().trim();
const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b/;

if (email === "") {
  $("#email").next().text("This field is required.");
  isValid = false;
} else if (!emailPattern.test(email)) {
  $("#email").next().text("Must be a valid email address.");
  isValid = false;
} else {
  $("#email").next().text("");
}

// Re-assign the trimmed value back to the field
$("#email").val(email);
