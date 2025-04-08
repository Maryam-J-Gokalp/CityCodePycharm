const phonePattern = /^\d{3}-\d{3}-\d{4}$/;
const phone = $("#phone").val().trim();
let isValid = true;

if (phone === "") {
    $("#phone").next().text("This field is required.");
    isValid = false;
} else if (!phonePattern.test(phone)) {
    $("#phone").next().text("Use 999-999-9999 format.");
    isValid = false;
} else {
    $("#phone").next().text("");
}

$("#phone").val(phone);
