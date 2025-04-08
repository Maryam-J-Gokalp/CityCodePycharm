document.getElementById("email_form").addEventListener("submit", function(event) {
    let email1 = document.getElementById("email_1").value.trim();
    let email2 = document.getElementById("email_2").value.trim();
    let firstName = document.getElementById("first_name").value.trim();
    let valid = true;

    // Clear previous error messages
    document.getElementById("error_email_1").textContent = "";
    document.getElementById("error_email_2").textContent = "";
    document.getElementById("error_first_name").textContent = "";

    if (email1 === "") {
        document.getElementById("error_email_1").textContent = "Email is required.";
        valid = false;
    }

    if (email2 === "") {
        document.getElementById("error_email_2").textContent = "Please confirm your email.";
        valid = false;
    } else if (email1 !== email2) {
        document.getElementById("error_email_2").textContent = "Emails must match.";
        valid = false;
    }

    if (firstName === "") {
        document.getElementById("error_first_name").textContent = "First name is required.";
        valid = false;
    }

    if (!valid) {
        event.preventDefault();  // Stops form submission if there are errors
    }
});
