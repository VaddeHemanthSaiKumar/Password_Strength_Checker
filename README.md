# 🔐 Password Strength Checker

A comprehensive GUI-based password strength evaluation tool built with Python and tkinter. This application provides real-time password strength analysis with detailed feedback to help users create secure passwords.

## 📋 Table of Contents
- [Features](#-features)
- [Demo](#-demo)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Code Structure](#-code-structure)
- [Security Criteria](#-security-criteria)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## ✨ Features

- **Real-time Password Analysis**: Instant strength evaluation as you type
- **5-Point Security Validation**: Comprehensive checking against industry standards
- **Visual Strength Indicators**: Color-coded strength levels (Weak/Medium/Strong)
- **Detailed Feedback**: Specific requirements and missing criteria
- **Password Visibility Toggle**: Show/hide password functionality for usability
- **Professional GUI**: Clean, intuitive interface with modern design elements
- **Comprehensive Error Reporting**: Clear guidance on password improvement
- **Cross-platform Compatibility**: Works on Windows, macOS, and Linux

## 🎯 Demo

The application evaluates passwords in real-time and provides immediate visual feedback:

- 🔴 **Weak** (0-2 criteria): Basic passwords needing significant improvement
- 🟡 **Medium** (3-4 criteria): Good passwords with minor weaknesses  
- 🟢 **Strong** (5 criteria): Secure passwords meeting all requirements


## 🛠️ Technologies Used

- **Python 3.13** - Core programming language
- **tkinter** - GUI framework for cross-platform desktop application
- **re (Regular Expressions)** - Pattern matching for character validation
- **Event-driven Programming** - Real-time user input handling

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- tkinter (usually included with Python)

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   cd password-strength-checker
   ```

2. **Verify Python installation**
   ```bash
   python --version
   ```

3. **Run the application**
   ```bash
   python password_checker.py
   ```

*Note: tkinter comes pre-installed with most Python distributions. If you encounter import errors, install tkinter using your system's package manager.*

## 💻 Usage

1. **Launch the application**
   ```bash
   python password_checker.py
   ```

2. **Enter your password** in the input field
   - The strength indicator updates in real-time
   - Color changes based on password strength

3. **Use the visibility toggle** 
   - Click "👁 Show" to reveal the password
   - Click "🙈 Hide" to mask the password

4. **Check detailed feedback**
   - Click "Check Strength" for comprehensive analysis
   - View specific missing requirements in popup window

## 🏗️ Code Structure

```
password-strength-checker/
│
├── password_checker.py          # Main application file
├── README.md                   # Project documentation
└── screenshots/                # Application screenshots
    ├── weak_password.png
    ├── medium_password.png
    └── strong_password.png
```

### Core Functions

- **`evaluate_password(password)`**: Core validation logic returning score and errors
- **`update_strength(event=None)`**: Real-time strength indicator updates
- **`check_password()`**: Detailed feedback popup display
- **`toggle_password()`**: Password visibility toggle functionality

## 🔒 Security Criteria

The application evaluates passwords against 5 essential security requirements:

| Criteria | Requirement | Points |
|----------|-------------|---------|
| **Length** | Minimum 8 characters | 1 |
| **Numbers** | At least one digit (0-9) | 1 |
| **Uppercase** | At least one capital letter (A-Z) | 1 |
| **Lowercase** | At least one small letter (a-z) | 1 |
| **Special Characters** | At least one symbol (!@#$%^&*()) | 1 |

### Strength Levels
- **Weak (0-2 points)**: Vulnerable to basic attacks
- **Medium (3-4 points)**: Moderately secure but improvable
- **Strong (5 points)**: Meets current security standards


## 🚧 Future Enhancements

### Security Improvements
- [ ] **Dictionary Attack Prevention**: Check against common password databases
- [ ] **Sequential Character Detection**: Identify patterns like "123" or "abc"
- [ ] **Repeated Character Limits**: Prevent excessive character repetition
- [ ] **Entropy Calculation**: Advanced randomness measurement

### Feature Additions
- [ ] **Password Generator**: Secure password creation tool
- [ ] **Strength History**: Track password attempts and improvements
- [ ] **Custom Rules**: Configurable validation criteria
- [ ] **Export Reports**: Save password analysis results
- [ ] **Multi-language Support**: Internationalization capabilities

### Technical Enhancements
- [ ] **Unit Testing**: Comprehensive test coverage
- [ ] **Configuration File**: Customizable security parameters
- [ ] **Logging System**: Application usage and security event logging
- [ ] **Database Integration**: Password attempt tracking and analysis

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Coding Standards
- Follow PEP 8 Python style guidelines
- Add comments for complex logic
- Include docstrings for functions
- Write unit tests for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Vadde Hemanth Sai Kumar** - saikumarjoey123@gmail.com

**Project Link**: https://github.com/VaddeHemanthSaiKumar/Password_Strength_Checker/

**LinkedIn**:https://www.linkedin.com/in/vadde-hemanth-sai-kumar/

---

### 🌟 Show Your Support

If you found this project helpful, please consider giving it a ⭐ on GitHub!

### 📚 Learning Resources

This project demonstrates several key programming concepts:
- GUI Development with Python tkinter
- Regular Expression Pattern Matching
- Event-Driven Programming Architecture
- Input Validation and Security Principles
- Real-time Data Processing
- User Experience Design

Perfect for developers learning desktop application development and cybersecurity fundamentals.

---

*Built with ❤️ for better password security*
