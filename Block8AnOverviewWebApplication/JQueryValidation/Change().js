$(function () {
  $(":radio").change(() => {
    const radioButton = $(":radio:checked").val();
    if (radioButton === "corporate") {
      $("#company_name").attr("disabled", false);
      $("#company_name").next().text("*");
    } else {
      $("#company_name").attr("disabled", true);
      $("#company_name").next().text("");
    }
  });
});
