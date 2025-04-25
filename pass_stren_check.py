import re

def check_password_strength(password):
    length = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[\W_]', password)  # Special characters (non-alphanumeric)

    score = sum([bool(length), bool(has_upper), bool(has_lower), bool(has_digit), bool(has_special)])

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

# --- Main ---
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    strength = check_password_strength(pwd)
    print(f"Password strength: {strength}")
