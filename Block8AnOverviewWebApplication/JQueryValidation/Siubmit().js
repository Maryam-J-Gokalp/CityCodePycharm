$("#member_form").submit(event => {
  event.preventDefault(); // Prevent the form from submitting right away
  let isValid = true;

  const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b/;
  const email = $("#email").val().trim();

  // Validate email
  if (email === "" || !emailPattern.test(email)) {
    isValid = false;
    $("#email").next().text("Please enter a valid email.");
  } else {
    $("#email").next().text("");
  }

  // If all validations pass, submit the form
  if (isValid) {
    $("#member_form")[0].submit();
  }
});
