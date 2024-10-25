import re

def assess_password_strength(password):
    # Define strength criteria
    length_criteria = len(password) >= 8
    complexity_criteria = (
        re.search(r'[a-z]', password) and  # at least one lowercase letter
        re.search(r'[A-Z]', password) and  # at least one uppercase letter
        re.search(r'[0-9]', password) and  # at least one digit
        re.search(r'[\W_]', password)      # at least one special character
    )
    
    # Check for common passwords
    common_passwords = set([
        "password", "123456", "123456789", "12345678", "12345", "1234567",
        "qwerty", "abc123", "football", "monkey", "letmein", "welcome",
        "iloveyou", "admin", "123123", "password1", "qwertyuiop"
    ])
    
    uniqueness_criteria = password.lower() not in common_passwords

    # Calculate overall strength
    strength_score = 0
    if length_criteria:
        strength_score += 1
    if complexity_criteria:
        strength_score += 1
    if uniqueness_criteria:
        strength_score += 1

    # Determine strength level
    if strength_score == 3:
        strength_level = "Strong"
    elif strength_score == 2:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"

    return {
        "length": length_criteria,
        "complexity": complexity_criteria,
        "uniqueness": uniqueness_criteria,
        "strength_level": strength_level
    }

# Example usage
password = input("Enter a password to assess: ")
assessment = assess_password_strength(password)

print("Password Assessment:")
print(f"Length criteria met: {assessment['length']}")
print(f"Complexity criteria met: {assessment['complexity']}")
print(f"Uniqueness criteria met: {assessment['uniqueness']}")
print(f"Overall strength level: {assessment['strength_level']}")
