# Keylogger
A Python-based keylogging script with advanced features including keystroke logging, screenshot capture, email delivery of logs, and optional persistence by adding to startup programs. Ideal for educational purposes and security testing in controlled environments.

![Keylogger Banner](banner.png)

Enhanced Keylogger is a Python-based keylogging script with additional features like screenshot capture and email delivery of logs.

## Features

- Logs keystrokes to a file (`keylog.txt`).
- Captures screenshots on ESC key press.
- Encrypts and sends log file via email.
- Option to enable persistence by adding to startup programs.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/enhanced-keylogger.git
   cd enhanced-keylogger
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables for email credentials:
   ```bash
   export EMAIL=your_email@example.com
   export RECIPIENT_EMAIL=recipient_email@example.com
   export EMAIL_PASSWORD=your_password
   ```

4. Run the keylogger with persistence enabled:
   ```bash
   python3 keylogger.py --persist
   ```

## Contributing

Contributions are welcome! Fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

### 3. Include Dependencies

Create a `requirements.txt` file listing the Python dependencies used by your script. If your script requires specific libraries (e.g., `pynput`, `PIL`, `cryptography`), include them in this file:

```
pynput
Pillow
cryptography
art
```

### 4. Git Ignore File

Create a `.gitignore` file to specify files and directories that should not be tracked by Git. For Python projects, include typical entries like:

```
__pycache__/
*.pyc
*.log
*.key
screenshots/
```




### Example Project


By following these steps, you'll effectively organize and publish your enhanced keylogger project on GitHub, making it accessible and understandable for others who may be interested in using or contributing to it.
