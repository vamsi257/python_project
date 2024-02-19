import os
import time
from flask import Flask, render_template, request
import pyautogui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_and_copy():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    # Save the file to a temporary directory
    # temp_path = os.path.join('temp', file.filename)
    temp_path = file.filename
    file.save(temp_path)

    # Simulate keypresses to open the file dialog, type the file path, and press Enter
    pyautogui.hotkey('ctrl', 'o')  # Open file dialog
    time.sleep(1)
    pyautogui.write(temp_path, interval=0.1)  # Adjust the interval if needed
    pyautogui.press('enter')
    time.sleep(2)

    # Simulate keypresses for copying and pasting data (replace with your logic)
    pyautogui.hotkey('ctrl', 'a')  # Select all data
    pyautogui.hotkey('ctrl', 'c')  # Copy
    pyautogui.hotkey('ctrl', 'pgdn')  # Move to another sheet
    pyautogui.hotkey('ctrl', 'v')  # Paste data

    return "Excel file uploaded and data copied successfully."

if __name__ == '__main__':
    app.run(debug=True)
