let isValid = true; // Initialize isValid variable

// Check if the input is not disabled
if (!$("#company_name").prop("disabled")) {
    const companyName = $("#company_name").val().trim(); // Get the trimmed value of the input

    // Validate if the company name is empty
    if (companyName === "") {
        // Display error message
        $("#company_name").next().text("This field is required.");
        isValid = false;
    } else {
        // Clear the error message
        $("#company_name").next().text("");
    }

    // Optionally, you can set the value again, though it's not necessary in this case
    // $("#company_name").val(companyName); // This is redundant since companyName already holds the value
}

