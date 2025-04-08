"use strict";

// Shortcut for selecting elements
const $ = selector => document.querySelector(selector);

// Display error messages in a list
const displayErrorMsgs = msgs => {
  const ul = document.createElement("ul");
  ul.classList.add("messages");

  for (let msg of msgs) {
    const li = document.createElement("li");
    li.appendChild(document.createTextNode(msg));
    ul.appendChild(li);
  }

  const existing = document.querySelector("ul");
  if (existing == null) {
    const form = $("form");
    form.parentNode.insertBefore(ul, form);
  } else {
    existing.parentNode.replaceChild(ul, existing);
  }
};

// Form validation and submission
const processEntries = () => {
  const email = $("#email_address");
  const phone = $("#phone");
  const country = $("#country");
  const terms = $("#terms");
  const comments = $("#comments");

  const msgs = [];

  if (email.value.trim() === "") {
    msgs.push("Please enter an email address.");
  }

  if (phone.value.trim() === "") {
    msgs.push("Please enter a mobile phone number.");
  }

  if (country.value === "") {
    msgs.push("Please select a country.");
  }

  if (!terms.checked) {
    msgs.push("You must agree to the terms of service.");
  }

  if (comments.value.trim() === "") {
    msgs.push("Please enter a comment.");
  }

  if (msgs.length === 0) {
    $("form").submit();
  } else {
    displayErrorMsgs(msgs);
  }
};

// Reset the form and remove messages
const resetForm = () => {
  $("form").reset();
  const messages = document.querySelector("ul");
  if (messages) messages.remove();
  $("#email_address").focus();
};

// Event listeners
document.addEventListener("DOMContentLoaded", () => {
  $("#register").addEventListener("click", processEntries);
  $("#reset_form").addEventListener("click", resetForm);
  $("#email_address").focus();
});
