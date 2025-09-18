import re

def password_checker(password):
    score = 0
    errors = []

    # Rule 1: Length
    if len(password) >= 8:
        score += 1
    else:
        errors.append("• At least 8 characters long")

    # Rule 2: Number
    if any(char.isdigit() for char in password):
        score += 1
    else:
        errors.append("• At least one number")

    # Rule 3: Uppercase
    if any(char.isupper() for char in password):
        score += 1
    else:
        errors.append("• At least one uppercase letter")

    # Rule 4: Lowercase
    if any(char.islower() for char in password):
        score += 1
    else:
        errors.append("• At least one lowercase letter")

    # Rule 5: Special Character
    if re.search(r'[!@#$%^&*()]', password):
        score += 1
    else:
        errors.append("• At least one special character (!@#$%^&*())")

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score in (3, 4):
        strength = "Medium"
    else:
        strength = "Strong"

    # Display results
    print(f"\n🔐 Password Strength: {strength}")
    if errors:
        print("❌ Missing requirements:")
        for e in errors:
            print(e)
    else:
        print("✅ Your password meets all requirements!")

# Main program
if __name__ == "__main__":
    user_password = input("Enter the password: ")
    password_checker(user_password)
