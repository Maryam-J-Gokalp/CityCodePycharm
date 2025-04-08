// Get the trimmed value of the first name input
const firstName = $("#first_name").val().trim();

if (firstName === "") {
    // Handle case where first name is empty
    console.log("First name is required.");
} else {
    // Handle valid first name
    console.log("First Name:", firstName);
}

// Get the trimmed value of the last name input
const lastName = $("#last_name").val().trim();

if (lastName === "") {
    // Handle case where last name is empty
    console.log("Last name is required.");
} else {
    // Clear any adjacent error text if last name is valid
    $("#last_name").next().text("");
}

// Set the value of the last name input field
$("#last_name").val(lastName);
