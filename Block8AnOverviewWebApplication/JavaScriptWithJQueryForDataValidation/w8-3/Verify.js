let isValid = true; // Declare and initialize the isValid variable

// Get the values of the password and verify password fields
const password = $("#password").val().trim();
const verify = $("#verify").val().trim();

// Reset the error message
$("#verifyError").text("");

// Check if the verify password is empty
if (verify === "") {
    $("#verifyError").text("This field is required.");
    isValid = false;
}
// Check if the verify password matches the original password
else if (verify !== password) {
    $("#verifyError").text("Must match first password entry.");
    isValid = false;
}

if (isValid) {
    // If valid, proceed with form submission or further actions
    console.log("Form is valid!");
} else {
    // If not valid, prevent form submission (if this is inside a submit handler)
    console.log("Form is invalid!");
}

// Optional: If you want to prevent the form from submitting
$("#form").submit((event) => {
    if (!isValid) {
        event.preventDefault(); // Prevent form submission
    }
});
