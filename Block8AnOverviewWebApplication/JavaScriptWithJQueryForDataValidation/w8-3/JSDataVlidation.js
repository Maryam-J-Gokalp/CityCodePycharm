"use strict";

$(document).ready(() => {
    // Focus on the email input field when the page loads
    $("#email").focus();

    // Optional: handle radio button change (not implemented yet)
    $(":radio").change(() => {
        // You can add logic here later if needed
    });

    // Form submission handler
    $("#member_form").submit(event => {
        let isValid = true;

        // Email validation
        const email = $("#email").val().trim();
        if (email === "") {
            $("#email").next().text("This field is required.");
            isValid = false;
        } else if (!email.includes("@")) {
            $("#email").next().text("Must be a valid email address.");
            isValid = false;
        } else {
            $("#email").next().text("");
        }
        $("#email").val(email);

        // Password validation
        const password = $("#password").val().trim();
        if (password === "") {
            $("#password").next().text("This field is required.");
            isValid = false;
        } else {
            $("#password").next().text("");
        }
        $("#password").val(password);

        // Verify password
        const verify = $("#verify").val().trim();
        if (verify === "") {
            $("#verify").next().text("This field is required.");
            isValid = false;
        } else if (verify !== password) {
            $("#verify").next().text("Must match first password entry.");
            isValid = false;
        } else {
            $("#verify").next().text("");
        }
        $("#verify").val(verify);

        // First Name
        const firstName = $("#first_name").val().trim();
        if (firstName === "") {
            $("#first_name").next().text("This field is required.");
            isValid = false;
        } else {
            $("#first_name").next().text("");
        }
        $("#first_name").val(firstName);

        // Last Name
        const lastName = $("#last_name").val().trim();
        if (lastName === "") {
            $("#last_name").next().text("This field is required.");
            isValid = false;
        } else {
            $("#last_name").next().text("");
        }
        $("#last_name").val(lastName);

        // Company Name (only if enabled)
        if (!$("#company_name").prop("disabled")) {
            const companyName = $("#company_name").val().trim();
            if (companyName === "") {
                $("#company_name").next().text("This field is required.");
                isValid = false;
            } else {
                $("#company_name").next().text("");
            }
            $("#company_name").val(companyName);
        }

        // Prevent form submission if any field is invalid
        if (!isValid) {
            event.preventDefault();
        }
    });
});
