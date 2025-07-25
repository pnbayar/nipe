import re

def is_strong_password(pwd):
    if len(pwd) < 8:
        return False
    if not re.search(r'[A-Z]', pwd):
        return False
    if not re.search(r'[a-z]', pwd):
        return False
    if not re.search(r'\d', pwd):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd):
        return False
    return True

# Example
print(is_strong_password("Test@123"))  # Output: True
