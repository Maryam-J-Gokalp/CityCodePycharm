if ( !$("#company_name").attr("disabled")) {
const companyName = $("#company_name").val().trim();
if (companyName == "") {
$("#company_name").next().text("This field is required.");
isValid = false;
} else {
$("#company_name").next().text("");
}
$("#company_name").val(companyName);
}
