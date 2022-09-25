def password_validator(password):
    password_valid = True
    if len(password)>10 or len(password)<6:
        print(f"Password must be between 6 and 10 characters")
        password_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        password_valid = False
    counter = 0
    for i in password:
        if i.isdigit():
            counter += 1
    if counter < 2:
        print("Password must have at least 2 digits")
        password_valid = False
    if password_valid:
        print(f"Password is valid")
password = input()
password_validator(password)

