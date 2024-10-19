import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, direction='encrypt'):
    result = ""
    if direction == 'decrypt':
        shift = -shift

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def process_text():
    text = text_entry.get("1.0", "end-1c")
    shift = shift_entry.get()
    
    if not shift.isdigit():
        messagebox.showerror("Error", "Shift must be a number.")
        return
    
    shift = int(shift)
    operation = mode_var.get()

    if operation not in ['encrypt', 'decrypt']:
        messagebox.showerror("Error", "Please select 'Encrypt' or 'Decrypt'.")
        return

    processed_text = caesar_cipher(text, shift, operation)
    result_text.delete("1.0", "end")
    result_text.insert("1.0", processed_text)

def clear_fields():
    text_entry.delete("1.0", "end")
    result_text.delete("1.0", "end")
    shift_entry.delete(0, "end")

# Create main window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("500x450")
root.resizable(False, False)

# Set background color and font style
root.configure(bg="#2c3e50")

# Define custom font
title_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 10, "bold")

# Add title label
title_label = tk.Label(root, text="Caesar Cipher Encryption/Decryption", font=title_font, fg="white", bg="#2c3e50")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Input text area
tk.Label(root, text="Enter text:", font=label_font, bg="#2c3e50", fg="white").grid(row=1, column=0, sticky="w")
text_entry = tk.Text(root, height=5, width=50, bg="#ecf0f1", fg="#2c3e50", font=label_font)
text_entry.grid(row=2, column=0, columnspan=2)

# Shift input
tk.Label(root, text="Enter shift (1-25):", font=label_font, bg="#2c3e50", fg="white").grid(row=3, column=0, sticky="w")
shift_entry = tk.Entry(root, bg="#ecf0f1", fg="#2c3e50", font=label_font)
shift_entry.grid(row=3, column=1, sticky="w")

# Operation selection (Encrypt/Decrypt)
mode_var = tk.StringVar(value="encrypt")
encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt", bg="#2c3e50", fg="white", selectcolor="#1abc9c", font=label_font)
encrypt_radio.grid(row=4, column=0, sticky="w")

decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt", bg="#2c3e50", fg="white", selectcolor="#e74c3c", font=label_font)
decrypt_radio.grid(row=4, column=1, sticky="w")

# Process button
process_button = tk.Button(root, text="Process", command=process_text, bg="#1abc9c", fg="white", font=button_font, width=15)
process_button.grid(row=5, column=0, columnspan=2)

# Result text area
tk.Label(root, text="Result:", font=label_font, bg="#2c3e50", fg="white").grid(row=6, column=0, sticky="w")
result_text = tk.Text(root, height=5, width=50, bg="#ecf0f1", fg="#2c3e50", font=label_font)
result_text.grid(row=7, column=0, columnspan=2)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_fields, bg="#e74c3c", fg="white", font=button_font, width=15)
clear_button.grid(row=8, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
