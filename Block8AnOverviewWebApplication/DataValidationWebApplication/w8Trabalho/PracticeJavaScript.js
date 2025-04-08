"use strict";

$(document).ready(() => {
    // Automatically focus on the email input when the page loads
    $("#email").focus();

    // Change event for radio buttons to detect selection
    $(":radio").change(() => {
        console.log("Membership option changed.");
    });

    // Handle form submission
    $("#member_form").submit(event => {
        event.preventDefault(); // Prevent form from submitting until validation

        const email = $("#email").val();
        const membership = $("input[name='membership']:checked").val();

        // Basic validation for email and membership
        if (!email || !membership) {
            alert("Please fill out all fields.");
            return;
        }

        alert(`Form submitted successfully!\nEmail: ${email}\nMembership: ${membership}`);
    });
});
