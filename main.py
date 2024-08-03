# main.py
import customtkinter as ctk
from ui import setup_ui

def main():
    root = ctk.CTk()
    root.title("File Cryptor")
    #root.geometry("400x600")
    root.minsize(600, 400)
    # Define the variables
    code = ctk.StringVar()
    text1 = ctk.CTkTextbox(root, wrap="word", font=("Arial", 15))
    
    # Setup the UI
    setup_ui(root, code, text1)

    root.mainloop()

if __name__ == "__main__":
    main()
