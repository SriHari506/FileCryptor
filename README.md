# FileCryptor
A Desktop Application for Protecting the data from breaches by domestic cyber attacks.
# Project Overview
File Cryptor is a desktop application designed to enhance the security of personal and important files by encrypting them before transmission and decrypting them using a secret key. This application helps protect your data from unauthorized access, particularly when files are shared via platforms like WhatsApp or email.

# Purpose
With the increasing concern about data privacy, this project aims to prevent unauthorized users from accessing your personal and sensitive information. For example, if you lend your phone to a friend, they might try to log into your WhatsApp on their device to monitor your messages and shared files without your knowledge. This application ensures that even if someone gains access to your files, they won't be able to understand the content without the correct decryption key.

# Features
File Encryption: Encrypts various types of files (documents, images, videos) with a chosen encoding format.
File Decryption: Decrypts files using the corresponding secret key and encoding format.
Text Encryption: Encrypts plain text input and saves it to a file.
Text Decryption: Decrypts encrypted text files and displays the plain text.
Progress Dialog: Displays a progress bar dialog during encryption and decryption processes.
User-Friendly Interface: A simple and intuitive GUI built with CustomTkinter.
# Technologies Used
Python
CustomTkinter (for GUI)
Base64, BinHex, Gzip, and other encoding/decoding libraries

# Installation
Clone the repository:



git clone https://github.com/your-username/file-cryptor.git
cd file-cryptor
Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Usage
Run the application:
python main.py

Follow the on-screen instructions to:

Upload a file or enter text to encrypt or decrypt.
Select the desired encoding format.
Enter a secret key for encryption/decryption.
Monitor the progress through the progress dialog.
Save the encrypted/decrypted file to the desired location.

![image](https://github.com/user-attachments/assets/be82e53d-b18d-4c17-8c77-77fc339d395a)
