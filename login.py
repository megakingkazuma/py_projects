class LoginSystem:
    def __init__(self, password, max_attempts):
        self.password = password
        self.max_attempts = max_attempts
        self.attempts = max_attempts

    def log_in(self):
        while self.attempts > 0:
            pre_password = input("What is the password?\n")
            self.attempts -= 1
            if pre_password == self.password:
                print("Password Correct.")
                return True
            else:
                print(f"Incorrect password, {self.attempts} attempts left.")
        print("Maximum attempts reached, exiting program.")
        return False


if __name__ == "__main__":
    password = "bingo"
    max_attempts = 3

    login_system = LoginSystem(password, max_attempts)
    if login_system.log_in():
        # Continue with the program logic if login is successful
        print("Welcome to the program!")
    else:
        # Exit the program or take appropriate action for login failure
        print("Exiting the program.")
