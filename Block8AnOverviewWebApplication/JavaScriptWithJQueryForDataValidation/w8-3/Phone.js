const phonePattern = /^\d{3}-\d{3}-\d{4}$/; // Defines the pattern for phone numbers like 999-999-9999
const phone = $("#phone").val().trim();    // Gets the value from the phone input and trims whitespace

if (phone == "") {
    // Show error message here (this part is missing in your snippet)
} else if (!phonePattern.test(phone)) {
    $("#phone").next().text("Use 999-999-9999 format.");
    isValid = false;
} else {
    $("#phone").next().text(""); // Clears the error message if valid
}

$("#phone").val(phone); // Sets the trimmed value back into the input
