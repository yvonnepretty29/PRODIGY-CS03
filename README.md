# Password Strength Assessment Tool

## Description
The Password Strength Assessment Tool is a Python-based application that evaluates the strength of a user-provided password. The tool provides feedback on various criteria such as length, use of uppercase and lowercase letters, inclusion of digits, and special characters, helping users create stronger and more secure passwords.

## Features
- **Length Validation:** Ensures the password is at least 8 characters long.
- **Character Checks:** Validates the presence of uppercase letters, lowercase letters, digits, and special characters.
- **Scoring System:** Assigns a score based on password complexity.
- **Feedback:** Provides detailed suggestions to improve password strength.

## Usage
### Prerequisites
- Python 3.6 or higher installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-tool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-strength-tool
   ```

### Running the Tool
1. Run the script:
   ```bash
   python password_strength_tool.py
   ```
2. Enter a password when prompted to receive feedback on its strength.

## Example
```
Welcome to the Password Strength Assessment Tool
Enter a password to assess its strength: Password123!
Password is strong. Good job!
```

## Code Overview
### Main Functionality
The core logic resides in the `assess_password_strength` function, which evaluates the password based on:
- Length (minimum 8 characters)
- Inclusion of uppercase and lowercase letters
- Inclusion of digits
- Inclusion of special characters

The tool then provides feedback or suggestions for improvement based on the criteria that were not met.

### File Structure
```
password-strength-tool/
├── password_strength_tool.py  # Main script
```

## Contributing
Contributions are welcome! If you have ideas for additional features or improvements, feel free to fork the repository and create a pull request.

## License
This project is open source .

## Author
- **Yvonne Otuoniyo** 
  Connect with me on [email](yvonneotuoniyo2@gmail.com) or check out my other projects on [GitHub](https://github.com/yvonnepretty29).

## Acknowledgments
- Inspired by prodigy info tech.

