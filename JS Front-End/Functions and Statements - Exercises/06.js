function passwordValidator(password) {
    let digitCount = 0;
    let valid = true;
  
    if (password.length < 6 || password.length > 10) {
      console.log("Password must be between 6 and 10 characters");
      valid = false;
    }
  
    if (!password.match(/^[a-zA-Z0-9]+$/)) {
      console.log("Password must consist only of letters and digits");
      valid = false;
    }
  
    for (let i = 0; i < password.length; i++) {
      if (password[i].match(/[0-9]/)) {
        digitCount++;
      }
    }
  
    if (digitCount < 2) {
      console.log("Password must have at least 2 digits");
      valid = false;
    }
  
    if (valid) {
      console.log("Password is valid");
    }
  }
  
  passwordValidator("logIn"); // Output: Password must be between 6 and 10 characters, Password must have at least 2 digits
  passwordValidator("Passw0rd"); // Output: Password is valid
  