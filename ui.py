# ui.py
import customtkinter as ctk
from tkinter import messagebox, filedialog
from tkinter.simpledialog import askstring
from file_operations import read_file, write_file, encrypt_data, decrypt_data, get_key, set_key

uploaded_file_path = None  # Initialize the global variable

def setup_ui(screen, code, text1):
    header_label = ctk.CTkLabel(screen, text="PROTECT FROM DOMESTIC CYBER ATTACKS", font=("Arial", 30, "bold"))
    header_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='nsew')

    text1.grid(row=1, column=0, columnspan=2, padx=250, pady=10, sticky='nsew')

    label_key = ctk.CTkLabel(screen, text="ENTER SECRET KEY", font=("Arial", 25, "bold"))
    label_key.grid(row=2, column=0, columnspan=2, pady=10, padx=300, sticky='nsew')

    entry_key = ctk.CTkEntry(screen, textvariable=code, show="*", font=("Arial", 25))
    entry_key.grid(row=3, column=0, columnspan=2, pady=10, padx=300, sticky='nsew')

    button_styles = [
        {"text": "UPLOAD FILE", "command": lambda: upload_file(screen, code)},
        {"text": "ENCRYPT FILE", "command": lambda: encrypt_file(screen, code)},
        {"text": "DECRYPT FILE", "command": lambda: decrypt_file(screen, code)},
        {"text": "ENCRYPT TEXT", "command": lambda: encrypt_text(screen, code, text1)},
        {"text": "DECRYPT TEXT", "command": lambda: decrypt_text(screen, code, text1)},
        {"text": "RESET", "command": lambda: reset(screen, code, text1)}
    ]

    button_colors = ["#4CAF50", "#2196F3", "#FF5722", "#9C27B0", "#FFC107", "#607D8B"]

    for index, (style, color) in enumerate(zip(button_styles, button_colors)):
        ctk.CTkButton(screen, text=style["text"], command=style["command"], font=("Arial", 25), corner_radius=6).grid(row=4 + index, column=0, columnspan=2, padx=300, pady=10, sticky='ew')

    screen.grid_rowconfigure(0, weight=0)
    screen.grid_rowconfigure(1, weight=1)
    screen.grid_rowconfigure(2, weight=0)
    screen.grid_rowconfigure(3, weight=0)
    screen.grid_rowconfigure(4, weight=0)
    screen.grid_rowconfigure(5, weight=0)
    screen.grid_rowconfigure(6, weight=0)
    screen.grid_rowconfigure(7, weight=0)
    screen.grid_columnconfigure(0, weight=1)
    screen.grid_columnconfigure(1, weight=1)

def upload_file(screen, code):
    global uploaded_file_path
    uploaded_file_path = filedialog.askopenfilename(filetypes=[
        ("All Files", "*.*"),
        ("Document Files","*.docx;*doc;*pdf;*txt"),
        ("PowerPoint Files", "*.ppt;*.pptx"),
        ("Image Files", "*.jpg;*.jpeg;*.png"),
        ("Video Files", "*.mp4;*.mkv")
    ])
    if uploaded_file_path:
        messagebox.showinfo("File Uploaded", f"File '{uploaded_file_path}' successfully uploaded!")
    else:
        messagebox.showerror("Error", "No file selected. Please select a file.")

def encrypt_file(screen, code):
    if uploaded_file_path:
        password=code.get()
        if password == "hari506":
            try:
            
                encoding_format = askstring("Input", "Select encoding format (url, html, base64, ascii_hex, hex, octal, binary):")
                if encoding_format not in ['url', 'html', 'base64', 'ascii_hex', 'hex', 'octal', 'binary']:
                    raise ValueError("Invalid encoding format selected.")
            
                key_str = askstring("Input", "Enter a secret key:")
                if not key_str:
                    raise ValueError("Key cannot be empty.")
            
                message = read_file(uploaded_file_path)
                if not message:
                    raise ValueError("No message found in file.")

                encrypted_message = encrypt_data(message, key_str, encoding_format)
                save_path = filedialog.asksaveasfilename(defaultextension=f".{encoding_format}", filetypes=[(f"{encoding_format.capitalize()} Files", f"*.{encoding_format}")])
                if save_path:
                    write_file(save_path, encrypted_message)
                    set_key(save_path, key_str)
                    messagebox.showinfo("Success", f"File encrypted successfully and saved to '{save_path}'!")
                else:
                    messagebox.showerror("Error", "File not saved. Please select a valid path.")
            except ValueError as ve:
                messagebox.showerror("Error", str(ve))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to encrypt file: {e}")
        elif password =="":
            messagebox.showerror("Error", "Please enter the Password")
        elif password != "hari506":
            messagebox.showerror("Oops", "Invalid Password")
        
    else:
        messagebox.showerror("Error", "No file selected for encryption. Please upload a file first.")

def decrypt_file(screen, code):
    if uploaded_file_path:
        password=code.get()
        if password == "hari506":
            try:
                encoding_format = askstring("Input", "Select encoding format (url, html, base64, ascii_hex, hex, octal, binary):")
                if encoding_format not in ['url', 'html', 'base64', 'ascii_hex', 'hex', 'octal', 'binary']:
                    raise ValueError("Invalid encoding format selected.")
            
                key_str = askstring("Input", "Enter the secret key for decryption:")
                if not key_str:
                    raise ValueError("Key cannot be empty.")
            
                saved_key = get_key(uploaded_file_path)
                if saved_key is None or saved_key != key_str:
                    raise ValueError("Invalid or missing secret key.")

                encrypted_message = read_file(uploaded_file_path)
                if not encrypted_message:
                    raise ValueError("No encrypted message found in file.")
            
                decrypted_message = decrypt_data(encrypted_message, key_str, encoding_format)
                save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"),("All Files", "*.*")])
                if save_path:
                    write_file(save_path, decrypted_message)
                    messagebox.showinfo("Success", f"File decrypted successfully and saved to '{save_path}'!")
                else:
                    messagebox.showerror("Error", "File not saved. Please select a valid path.")
            except ValueError as ve:
                messagebox.showerror("Error", str(ve))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to decrypt file: {e}")
        elif password =="":
            messagebox.showerror("Error", "Please enter the Password")
        elif password != "hari506":
            messagebox.showerror("Oops", "Invalid Password")
    else:
        messagebox.showerror("Error", "No file selected for decryption. Please upload a file first.")

def encrypt_text(screen, code, text1):
    password=code.get()
    if password == "hari506":
        try:
            encoding_format = askstring("Input", "Select encoding format (url, html, base64, ascii_hex, hex, octal, binary):")
            if encoding_format not in ['url', 'html', 'base64', 'ascii_hex', 'hex', 'octal', 'binary']:
                raise ValueError("Invalid encoding format selected.")
        
            key_str = askstring("Input", "Enter a secret key:")
            if not key_str:
                raise ValueError("Key cannot be empty.")

            text = text1.get(1.0, 'end-1c').encode('utf-8')
            if not text:
                raise ValueError("No text entered for encryption.")
        
            encrypted_text = encrypt_data(text, key_str, encoding_format)
            save_path = filedialog.asksaveasfilename(defaultextension=f".{encoding_format}", filetypes=[(f"{encoding_format.capitalize()} Files", f"*.{encoding_format}")])
            if save_path:
                write_file(save_path, encrypted_text)
                set_key(save_path, key_str)
                messagebox.showinfo("Success", f"Text encrypted successfully and saved to '{save_path}'!")
            else:
                messagebox.showerror("Error", "File not saved. Please select a valid path.")
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encrypt text: {e}")
    elif password =="":
        messagebox.showerror("Error", "Please enter the Password")
    elif password != "hari506":
        messagebox.showerror("Oops", "Invalid Password")
def decrypt_text(screen, code, text1):
    password = code.get()
    if password == "hari506":
        try:
            encoding_format = askstring("Input", "Select encoding format (url, html, base64, ascii_hex, hex, octal, binary):")
            if encoding_format not in ['url', 'html', 'base64', 'ascii_hex', 'hex', 'octal', 'binary']:
                raise ValueError("Invalid encoding format selected.")
        
            key_str = askstring("Input", "Enter the secret key for decryption:")
            if not key_str:
                raise ValueError("Key cannot be empty.")
        
            saved_key = get_key(uploaded_file_path)
            if saved_key is None or saved_key != key_str:
                raise ValueError("Invalid or missing secret key.")
        
            encrypted_text = read_file(uploaded_file_path)
            if not encrypted_text:
                raise ValueError("No encrypted text found in file.")
        
            decrypted_text = decrypt_data(encrypted_text, key_str, encoding_format).decode('utf-8')
            text1.delete(1.0, 'end')
            text1.insert('end', decrypted_text)
            messagebox.showinfo("Success", "Text decrypted successfully!")
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt text: {e}")
    elif password =="":
        messagebox.showerror("Error", "Please enter the Password")
    elif password != "hari506":
        messagebox.showerror("Oops", "Invalid Password")
def reset(screen, code, text1):
    global uploaded_file_path
    uploaded_file_path = None
    text1.delete(1.0, 'end')
    code.set("")
    messagebox.showinfo("Reset", "Application reset successfully!")
