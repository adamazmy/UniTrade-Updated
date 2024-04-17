// Example 1: Add validation for email format
const emailInput = document.getElementById('id_email');

emailInput.addEventListener('blur', function() {
  const email = this.value;
  const emailRegex = /^(([^<>()[\\]\\\\.,;:\s@"]+(\.[^<>()[\\]\\\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  if (emailRegex.test(email) = False) {
    alert('Please enter a valid email address.');
  }
});

// Example 2: Show/hide password on checkbox click
const passwordInput1 = document.getElementById('id_password1');
const passwordInput2 = document.getElementById('id_password2');

const showPasswordCheckbox = document.getElementById('show_password');

showPasswordCheckbox.addEventListener('click', function() {
  if (this.checked) {
    passwordInput1.type = 'text';
  } else {
    passwordInput1.type = 'password';
    console.log(passwordInput1.type); // Added line

  }

  // Repeat for passwordInput2 (optional, for testing)
  if (this.checked) {
    passwordInput2.type = 'text';
    console.log(passwordInput2.type); // Added line

  } else {
    passwordInput2.type = 'password';
    console.log(passwordInput2.type); // Added line

  }
  
});
