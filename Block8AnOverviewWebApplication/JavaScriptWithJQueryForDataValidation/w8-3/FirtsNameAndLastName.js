let isValid = true; // Make sure this is declared at the start of your validation function

// Validate first name
const firstName = $("#first_name").val().trim();
if (firstName === "") {
    $("#first_name").next().text("This field is required.");
    isValid = false;
} else {
    $("#first_name").next().text("");
}

// Validate last name
const lastName = $("#last_name").val().trim(); // Fixed selector
if (lastName === "") {
    $("#last_name").next().text("This field is required.");
    isValid = false;
} else {
    $("#last_name").next().text("");
}

// Optionally, reset the input values to trimmed values
$("#first_name").val(firstName);
$("#last_name").val(lastName);

