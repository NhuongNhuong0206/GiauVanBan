import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import secrets
import base64

def generate_aes_key():
    return secrets.token_bytes(32)

def save_key_to_file(file_path, key):
    key_base64 = base64.b64encode(key).decode('utf-8')
    with open(file_path, 'w') as file:
        file.write(key_base64)

def read_key_from_file(file_path):
    with open(file_path, 'r') as file:
        key_base64 = file.read()
        return base64.b64decode(key_base64)

def encrypt_file_with_auto_key(input_file_path, output_file_path):
    key = generate_aes_key()
    save_key_to_file('encryption_key.txt', key)

    with open(input_file_path, 'rb') as file:
        plaintext = file.read()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB8(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    ciphertext_base64 = base64.b64encode(ciphertext).decode('utf-8')

    with open(output_file_path, 'w') as file:
        file.write(base64.b64encode(iv).decode('utf-8') + '\n')
        file.write(ciphertext_base64)

def decrypt_file_with_key(input_file_path, output_file_path):
    key_file_path = 'encryption_key.txt'
    if not os.path.exists(key_file_path):
        messagebox.showerror("Error", "Encryption key file not found.")
        return

    key = read_key_from_file(key_file_path)

    with open(input_file_path, 'r') as file:
        iv_base64 = file.readline().strip()
        ciphertext_base64 = file.read()

    iv = base64.b64decode(iv_base64)[:16]  # Chỉ lấy 16 byte đầu của IV

    # Thêm dấu '=' vào cuối chuỗi để đảm bảo độ dài của chuỗi là bội số của 4
    while len(ciphertext_base64) % 4 != 0:
        ciphertext_base64 += '='

    ciphertext = base64.b64decode(ciphertext_base64)

    cipher = Cipher(algorithms.AES(key), modes.CFB8(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    with open(output_file_path, 'wb') as file:
        file.write(plaintext)

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Choose a file")
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def encrypt_button_clicked():
    input_file_path = entry_file_path.get()
    if input_file_path:
        output_file_path = input_file_path + "_encrypted"
        encrypt_file_with_auto_key(input_file_path, output_file_path)
        messagebox.showinfo("Encryption Complete", "File encrypted successfully!")

def decrypt_button_clicked():
    input_file_path = entry_file_path.get()
    if input_file_path:
        output_file_path = input_file_path + "_decrypted"
        decrypt_file_with_key(input_file_path, output_file_path)
        messagebox.showinfo("Decryption Complete", "File decrypted successfully!")

# Tkinter window setup
root = tk.Tk()
root.title("File Encryption Tool")

label_file_path = tk.Label(root, text="File Path:")
label_file_path.pack(pady=5)

entry_file_path = tk.Entry(root, width=50)
entry_file_path.pack(pady=5)

button_browse = tk.Button(root, text="Browse", command=open_file_dialog)
button_browse.pack(pady=5)

button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_button_clicked)
button_encrypt.pack(pady=10)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_button_clicked)
button_decrypt.pack(pady=10)

root.mainloop()
