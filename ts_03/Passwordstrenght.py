import re

def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 12
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*()_+{}|:"<>?~\[\];\',./]', password))

    # Calculate score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    # Provide feedback
    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score >= 2:
        return "Moderate"
    elif score >= 1:
        return "Weak"
    else:
        return "Very Weak"

# Example usage
password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password strength:", strength)
