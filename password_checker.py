import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long.")

    # Rule 2: Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    # Rule 3: Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    # Rule 4: Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Rule 5: Special character check
    if re.search(r"[@$!%*?&#]", password):
        score += 1
    else:
        feedback.append("Include a special character (e.g., @, $, !, %, *, ?, &, #).")

    # Determine final strength
    if score == 5:
        return "Strong", "Great job! Password is secure."
    elif score >= 3:
        return "Medium", " ".join(feedback)
    else:
        return "Weak", " ".join(feedback)
    
# This must be flush with the left margin
if __name__ == "__main__":
    # These must be indented by 4 spaces
    print("--- Password Strength Checker ---")
    user_password = input("Enter a password to test: ")
    
    strength, tips = check_password_strength(user_password)
    
    print(f"\nStrength: {strength}")
    if strength != "Strong":
        print(f"Tips to improve: {tips}")