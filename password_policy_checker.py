import re

def is_strong(password):
    return bool(re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$', password))

def check_passwords():
    passwords = ['Test123', 'Strong@123', 'weakpass', 'Admin#2023']
    for pwd in passwords:
        print(f"{pwd}: {'Strong' if is_strong(pwd) else 'Weak'}")

if __name__ == '__main__':
    check_passwords()