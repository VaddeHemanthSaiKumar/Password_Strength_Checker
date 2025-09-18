# 🔐 Password Strength Checker (CLI Version)

A simple yet effective command-line password strength evaluation tool built with Python. This application analyzes password security using industry-standard criteria and provides clear feedback on password strength and missing requirements.

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Security Criteria](#-security-criteria)
- [Code Structure](#-code-structure)
- [Examples](#-examples)
- [Potential Enhancements](#-potential-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

This password strength checker evaluates passwords against 5 essential security criteria and provides immediate feedback on password quality. Built as a learning project to demonstrate Python programming fundamentals, regular expressions, and cybersecurity awareness.

## ✨ Features

- **5-Point Security Validation**: Comprehensive checking against industry standards
- **Instant Feedback**: Clear strength categorization (Weak/Medium/Strong)
- **Detailed Error Reporting**: Specific guidance on missing requirements
- **Clean CLI Interface**: User-friendly command-line experience
- **Lightweight & Fast**: Minimal dependencies with efficient processing
- **Educational Value**: Perfect for learning password security principles

## 🎮 Demo

```bash
$ python password_checker.py
Enter the password: mypassword

🔐 Password Strength: Weak
❌ Missing requirements:
• At least one number
• At least one uppercase letter
• At least one special character (!@#$%^&*())
```

```bash
$ python password_checker.py
Enter the password: MySecure123!

🔐 Password Strength: Strong
✅ Your password meets all requirements!
```

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- No additional packages required (uses built-in libraries)

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/password-strength-checker-cli.git
   cd password-strength-checker-cli
   ```

2. **Verify Python installation**
   ```bash
   python --version
   ```

3. **Run the application**
   ```bash
   python password_checker.py
   ```

## 💻 Usage

### Basic Usage
```bash
python password_checker.py
```

### Interactive Mode
1. Run the script
2. Enter your password when prompted
3. Receive instant strength analysis and feedback

### Integration in Other Projects
```python
from password_checker import password_checker

# Get password strength analysis
strength, errors = password_checker("YourPassword123!")

if not errors:
    print("Password is secure!")
else:
    print(f"Password strength: {strength}")
    for error in errors:
        print(error)
```

## 🔒 Security Criteria

The application evaluates passwords against 5 essential security requirements:

| Criteria | Requirement | Weight | Example |
|----------|-------------|---------|---------|
| **Length** | Minimum 8 characters | 1 point | `Password123` ✅ |
| **Numbers** | At least one digit (0-9) | 1 point | `Pass1word` ✅ |
| **Uppercase** | At least one capital letter (A-Z) | 1 point | `Password` ✅ |
| **Lowercase** | At least one small letter (a-z) | 1 point | `password` ✅ |
| **Special Characters** | At least one symbol (!@#$%^&*()) | 1 point | `Pass@word` ✅ |

### Strength Classification
- **🔴 Weak (0-2 points)**: Vulnerable to basic attacks, needs immediate improvement
- **🟡 Medium (3-4 points)**: Moderately secure but has room for enhancement  
- **🟢 Strong (5 points)**: Meets all current security standards

## 🏗️ Code Structure

```
password-strength-checker-cli/
│
├── password_checker.py         # Main application file
├── README.md                   # Project documentation
└── examples/                   # Usage examples (optional)
    └── integration_example.py
```

### Core Function

```python
def password_checker(password):
    """
    Evaluates password strength based on 5 security criteria.
    
    Args:
        password (str): The password to evaluate
    
    Returns:
        tuple: (strength_level, list_of_missing_requirements)
    """
```

### Key Components
- **Rule Validation**: Individual checks for each security criterion
- **Score Calculation**: Points system for strength assessment
- **Error Tracking**: Detailed feedback on missing requirements
- **Strength Classification**: Clear categorization based on score

## 📸 Examples

### Example 1: Weak Password
```
Input: "password"
Output: Weak (2/5 points)
Missing: Numbers, Uppercase, Special characters
```

### Example 2: Medium Password
```
Input: "Password123"
Output: Medium (4/5 points)
Missing: Special characters
```

### Example 3: Strong Password
```
Input: "MySecure123!"
Output: Strong (5/5 points)
All requirements met!
```

## 🚧 Potential Enhancements

### Security Improvements
- [ ] **Dictionary Attack Prevention**: Check against common password lists
- [ ] **Pattern Detection**: Identify sequences like "123" or "abc"
- [ ] **Repeated Character Analysis**: Limit excessive character repetition
- [ ] **Entropy Calculation**: Advanced randomness measurement
- [ ] **Password History**: Prevent reuse of recent passwords

### Feature Additions
- [ ] **Batch Processing**: Analyze multiple passwords from file
- [ ] **Password Generation**: Suggest secure alternatives
- [ ] **Configuration Options**: Customizable rules and weights
- [ ] **Export Reports**: Save analysis results to file
- [ ] **Interactive Mode**: Menu-driven interface

### Technical Enhancements
- [ ] **Unit Testing**: Comprehensive test coverage
- [ ] **Logging System**: Track usage and security events
- [ ] **API Integration**: RESTful service for web applications
- [ ] **GUI Version**: Desktop application with tkinter
- [ ] **Web Interface**: Flask/Django web application

## 🧪 Testing

### Manual Testing
```bash
# Test various password scenarios
python password_checker.py

# Test cases to try:
# - "weak" (very weak)
# - "Password1" (medium)
# - "MySecure123!" (strong)
# - "a1A!" (short but complex)
```

### Automated Testing (Future Enhancement)
```python
import unittest
from password_checker import password_checker

class TestPasswordChecker(unittest.TestCase):
    def test_weak_password(self):
        strength, errors = password_checker("weak")
        self.assertEqual(strength, "Weak")
        self.assertEqual(len(errors), 4)
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 Python style guidelines
- Add docstrings for new functions
- Include test cases for new features
- Update documentation as needed
- Maintain backward compatibility

### Ideas for Contributors
- Add more sophisticated password analysis algorithms
- Implement additional security criteria
- Create a web-based version
- Add support for multiple languages
- Develop a password generator feature

## 📚 Educational Value

This project demonstrates several important programming concepts:

### Python Fundamentals
- **Function Design**: Clean, reusable function structure
- **Control Flow**: Conditional statements and loops
- **Data Structures**: Lists for error tracking
- **String Methods**: Character analysis and validation

### Security Awareness
- **Password Security**: Industry-standard validation criteria
- **Risk Assessment**: Understanding vulnerability levels
- **User Education**: Clear feedback and guidance

### Software Development
- **Code Organization**: Modular design principles
- **User Experience**: Intuitive command-line interface
- **Error Handling**: Comprehensive feedback system

## 🔧 Technical Details

### Dependencies
- **Built-in Libraries Only**: `re` (regular expressions)
- **Python Version**: 3.6+
- **Platform**: Cross-platform compatible

### Performance
- **Memory Usage**: Minimal (< 1MB)
- **Execution Time**: < 1ms for typical passwords
- **Scalability**: Suitable for batch processing

### Security Considerations
- **No Password Storage**: Passwords are not saved or logged
- **Memory Safety**: No sensitive data persistence
- **Local Processing**: No network communication required

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

** Vadde Hemanth Sai Kumar** - saikumarjoey123@gmail.com

**Project Link**: https://github.com/VaddeHemanthSaiKumar/Password_Strength_Checker

**LinkedIn**:https://www.linkedin.com/in/vadde-hemanth-sai-kumar/

---

### 🌟 Show Your Support

If you found this project helpful, please consider:
- ⭐ Starring the repository
- 🍴 Forking for your own improvements
- 🐛 Reporting issues or bugs
- 💡 Suggesting new features

### 📖 Related Projects

- [Password Strength Checker GUI](../password-checker-gui) - Tkinter-based desktop version
- [Password Generator](../password-generator) - Secure password creation tool
- [Security Tools Collection](../security-tools) - Additional cybersecurity utilities

---

*Built with ❤️ for better password security education and awareness*

### 🎓 Learning Resources

Perfect for developers learning:
- **Python Programming**: Functions, conditionals, string processing
- **Regular Expressions**: Pattern matching and validation
- **Cybersecurity**: Password security principles and best practices
- **CLI Development**: Command-line interface design
- **Code Documentation**: Professional README creation
