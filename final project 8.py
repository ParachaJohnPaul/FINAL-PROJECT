import random
import string

def generate_password(length):
    """
    Generate a random alphanumeric password of a given length.

    Parameters:
    length (int): Length of the password to be generated.

    Returns:
    str: The generated password.
    """
    
    characters = string.ascii_letters + string.digits
    
   
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
   
    length = int(input("Enter the length of the password: "))
    
   
    password = generate_password(length)
    
   
    print("Generated password:", password)
