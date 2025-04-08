"use strict";

$(document).ready(() => {

    // Manage radio button selection and enable/disable company name field
    $(":radio").change(() => {
        const selectedOption = $(":radio:checked").val();
        if (selectedOption === "corporate") {
            $("#company_name").prop("disabled", false);
            $("#company_name").next().text("*");
        } else {
            $("#company_name").prop("disabled", true);
            $("#company_name").next().text("");
        }
    });

    // Form submission handler for validation
    $("#member_form").submit(event => {

        let isValid = true;

        // Email validation
        const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b/;
        const email = $("#email").val().trim();

        if (email === "") {
            $("#email").next().text("This field is required.");
            isValid = false;
        } else if (!emailPattern.test(email)) {
            $("#email").next().text("Must be a valid email address.");
            isValid = false;
        } else {
            $("#email").next().text("");
        }
        $("#email").val(email);

        // Password field validation
        const password = $("#password").val().trim();
        if (password.length < 6) {
            $("#password").next().text("Must be 6 or more characters.");
            isValid = false;
        } else {
            $("#password").next().text("");
        }
        $("#password").val(password);

        // Password confirmation validation
        const verifyPassword = $("#verify").val().trim();
        if (verifyPassword === "") {
            $("#verify").next().text("This field is required.");
            isValid = false;
        } else if (verifyPassword !== password) {
            $("#verify").next().text("Must match the first password entry.");
            isValid = false;
        } else {
            $("#verify").next().text("");
        }
        $("#verify").val(verifyPassword);

        // Company name validation (if applicable)
        if (!$("#company_name").prop("disabled")) {
            const company = $("#company_name").val().trim();
            if (company === "") {
                $("#company_name").next().text("This field is required.");
                isValid = false;
            } else {
                $("#company_name").next().text("");
            }
            $("#company_name").val(company);
        }

        // First name validation
        const firstName = $("#first_name").val().trim();
        if (firstName === "") {
            console.log("First name is required.");
            isValid = false;
        } else {
            console.log("First Name entered:", firstName);
        }

        // Last name validation
        const lastName = $("#last_name").val().trim();
        if (lastName === "") {
            console.log("Last name is required.");
            isValid = false;
        } else {
            $("#last_name").next().text("");
        }
        $("#last_name").val(lastName);

        // Phone number validation
        const phonePattern = /^\d{3}-\d{3}-\d{4}$/;
        const phone = $("#phone").val().trim();

        if (phone === "") {
            $("#phone").next().text("This field is required.");
            isValid = false;
        } else if (!phonePattern.test(phone)) {
            $("#phone").next().text("Format must be 999-999-9999.");
            isValid = false;
        } else {
            $("#phone").next().text("");
        }
        $("#phone").val(phone);

        // If any field is invalid, prevent the form from being submitted
        if (!isValid) {
            event.preventDefault();
        }

    });
});


