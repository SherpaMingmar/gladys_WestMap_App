
import re

def login():
    """
    Asks the user for a login (email address) and password, and validates them.
    Returns the user login (email address) to the gladysUserInterface module if successful.
    """
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        user_login = input("Enter your email address: ")
        user_password = get_password()  # Prompt for password
        if validate_email(user_login) and validate_password(user_password):
            return user_login
        else:
            print("Invalid email address or password. Please try again.")
            attempts += 1

    print("Exceeded maximum number of attempts. Exiting...")
    exit()

def get_password():
    """
    Asks the user for a password.
    Returns the entered password.
    """
    return input("Enter your password: ")

def validate_email(email):
    """
    Validates if the given string is a valid email address.
    Returns True if valid, otherwise False.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)
def validate_password(password):
    """
    Validates if the given password meets the criteria.
    Returns True if valid, otherwise False.
    For example, minimum length, specific characters, etc.
    """
    # Add your password validation criteria here
    # For example, minimum length, specific characters, etc.
    if len(password) >= 8:
        return True
    else:
        return False
    

# The rest of your code remains unchanged...

# Example usage
if __name__ == "__main__":
    user_name = login()
    print(f"Logged in as: {user_name}")
