import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isupper():
            start = ord('A')
            if mode == 'encrypt':
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                result += chr((ord(char) - start - shift + 26) % 26 + start)
        elif char.islower():
            start = ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                result += chr((ord(char) - start - shift + 26) % 26 + start)
        else:
            result += char
    return result

def process_text(mode):
    if mode == 'encrypt':
        text = entry_text_encrypt.get()
        shift = entry_shift_encrypt.get()
    else:
        text = entry_text_decrypt.get()
        shift = entry_shift_decrypt.get()

    if not shift.isdigit():
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    shift = int(shift)
    result_text = caesar_cipher(text, shift, mode)
    if mode == 'encrypt':
        entry_result_encrypt.delete(0, tk.END)
        entry_result_encrypt.insert(0, result_text)
        messagebox.showinfo("Result", f"Encrypted Text: {result_text}")
    else:
        entry_result_decrypt.delete(0, tk.END)
        entry_result_decrypt.insert(0, result_text)
        messagebox.showinfo("Result", f"Decrypted Text: {result_text}")

def clear_fields():
    for entry in [entry_text_encrypt, entry_shift_encrypt, entry_result_encrypt,
                  entry_text_decrypt, entry_shift_decrypt, entry_result_decrypt]:
        entry.delete(0, tk.END)

# Creating the main window
root = tk.Tk()
root.title("Caesar Cipher")
root.config(bg='#F0F0F0')

# Common styles
card_bg = '#FFFFFF'
card_border = '#DDDDDD'
entry_bg = '#EFEFEF'

# Card view for encryption
frame_encrypt = tk.Frame(root, bg=card_bg, bd=2, relief='groove', padx=10, pady=10)
frame_encrypt.grid(row=0, column=0, padx=20, pady=10, sticky='ew')

tk.Label(frame_encrypt, text="Encryption", bg=card_bg, font=('Helvetica', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(frame_encrypt, text="Enter the text to encrypt:", bg=card_bg).grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_text_encrypt = tk.Entry(frame_encrypt, width=50, bg=entry_bg)
entry_text_encrypt.grid(row=1, column=1, padx=10, pady=5)
tk.Label(frame_encrypt, text="Enter the shift value:", bg=card_bg).grid(row=2, column=0, padx=10, pady=5, sticky='w')
entry_shift_encrypt = tk.Entry(frame_encrypt, width=50, bg=entry_bg)
entry_shift_encrypt.grid(row=2, column=1, padx=10, pady=5)
tk.Button(frame_encrypt, text="Encrypt", command=lambda: process_text('encrypt'), bg='#4CAF50', fg='white').grid(row=3, column=0, columnspan=2, padx=10, pady=10)
tk.Label(frame_encrypt, text="Encrypted Result:", bg=card_bg).grid(row=4, column=0, padx=10, pady=5, sticky='w')
entry_result_encrypt = tk.Entry(frame_encrypt, width=50, bg=entry_bg)
entry_result_encrypt.grid(row=4, column=1, padx=10, pady=5)

# Card view for decryption
frame_decrypt = tk.Frame(root, bg=card_bg, bd=2, relief='groove', padx=10, pady=10)
frame_decrypt.grid(row=1, column=0, padx=20, pady=10, sticky='ew')

tk.Label(frame_decrypt, text="Decryption", bg=card_bg, font=('Helvetica', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(frame_decrypt, text="Enter the text to decrypt:", bg=card_bg).grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_text_decrypt = tk.Entry(frame_decrypt, width=50, bg=entry_bg)
entry_text_decrypt.grid(row=1, column=1, padx=10, pady=5)
tk.Label(frame_decrypt, text="Enter the shift value:", bg=card_bg).grid(row=2, column=0, padx=10, pady=5, sticky='w')
entry_shift_decrypt = tk.Entry(frame_decrypt, width=50, bg=entry_bg)
entry_shift_decrypt.grid(row=2, column=1, padx=10, pady=5)
tk.Button(frame_decrypt, text="Decrypt", command=lambda: process_text('decrypt'), bg='#F44336', fg='white').grid(row=3, column=0, columnspan=2, padx=10, pady=10)
tk.Label(frame_decrypt, text="Decrypted Result:", bg=card_bg).grid(row=4, column=0, padx=10, pady=5, sticky='w')
entry_result_decrypt = tk.Entry(frame_decrypt, width=50, bg=entry_bg)
entry_result_decrypt.grid(row=4, column=1, padx=10, pady=5)

# Clear button
tk.Button(root, text="Clear", command=clear_fields, bg='#2196F3', fg='white').grid(row=2, column=0, padx=20, pady=10)

# Running the main loop
root.mainloop()
