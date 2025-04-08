$(document).ready(function() {
    // When the document is ready, the code inside this block will run.

    // Example form data (adjust as necessary):
    var formData = {
        key1: "value1",
        key2: "value2"
    };

    // Example URL (replace with your actual URL)
    var url = "https://example.com/your-endpoint";

    // AJAX request
    $.ajax({
        url: url,              // Specify the URL to send the request to
        method: "POST",        // Specify the HTTP method (POST)
        data: formData,        // The data to send in the request body
        success: function(response) {  // What to do if the request is successful
            console.log("Response:", response);  // Example of logging the response
            // You can also update the UI based on the response here
        },
        error: function(xhr, status, error) {  // What to do if there is an error
            console.error("Error:", error);  // Log the error to the console
            console.log("Status:", status);  // Log the status of the request
            console.log("Response:", xhr.responseText);  // Log the response text for debugging
            // You can handle the error in the UI here (e.g., show an error message)
        }
    });
});
