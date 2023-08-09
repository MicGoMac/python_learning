import bcrypt

'''
copied from https://medium.com/@HeCanThink/bcrypt-safeguarding-users-passwords-in-python-fd8400bdd03
'''

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
def verify_password(hashed_password, input_password):
    # Verify if the input password matches the hashed password
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)
# Example usage
if __name__ == "__main__":
    # Original password to be hashed and stored
    original_password = "mysecretpassword"
    # Hash the password
    hashed_password = hash_password(original_password)
    print("Hashed Password:", hashed_password)
    # Simulate a login attempt with an input password
    input_password = "mysecretpassword"
    is_password_correct = verify_password(hashed_password, input_password)
    
    if is_password_correct:
        print("Login successful.")
    else:
        print("Login failed. Invalid password.")
