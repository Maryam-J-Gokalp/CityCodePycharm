document.addEventListener("DOMContentLoaded", () => {
    const joinListButton = document.getElementById("joinList");
    const clearFormButton = document.getElementById("clearForm");

    joinListButton.addEventListener("click", () => {
        const email1 = document.getElementById("email1").value.trim();
        const email2 = document.getElementById("email2").value.trim();
        const firstName = document.getElementById("firstName").value.trim();
        let errorMessage = "";

        if (email1 === "") {
            errorMessage += "First email is required.\n";
        }
        if (email2 === "") {
            errorMessage += "Confirm email is required.\n";
        }
        if (email1 !== email2) {
            errorMessage += "Both emails must match.\n";
        }
        if (firstName === "") {
            errorMessage += "First name is required.\n";
        }

        if (errorMessage) {
            alert(errorMessage);
            document.getElementById("email1").focus();
        } else {
            alert("Successfully joined the email list!");
            document.getElementById("emailForm").reset();
        }
    });

    clearFormButton.addEventListener("click", () => {
        document.getElementById("emailForm").reset();
        document.getElementById("email1").focus();
    });
});
