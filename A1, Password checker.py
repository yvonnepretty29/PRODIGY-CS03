import re

def assess_password_strength(password):
    """
    Assess the strength of a given password and provide feedback.
    
    :param password: The password string to be assessed.
    :return: A string with feedback on the password's strength.
    """
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    feedback = []

    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should include at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    if score == 5:
        return "Password is strong. Good job!"
    elif score == 4:
        return "Password is moderate. Consider adding more variety."
    elif score == 3:
        return "Password is weak. Please improve by adding more complexity."
    else:
        return "Password is very weak. It needs significant improvement."

def main():
    print("Welcome to the Password Strength Assessment Tool")
    password = input("Enter a password to assess its strength: ")
    feedback = assess_password_strength(password)
    print(feedback)

if __name__ == '__main__':
    main()
