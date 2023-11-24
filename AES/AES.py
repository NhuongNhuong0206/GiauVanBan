# # # # import pyAesCrypt
# # # # keysize = 64*1024 #64kb size of file
# # # #
# # # # #get password from user input
# # # #
# # # # password=input("Nhập password để mã hoá và giải mã file của bạn: ")
# # # #
# # # # #get option from user input to encrypt by typing E,e or D,d to decrypt
# # # # EorD = str(input("nhập E để mã hoá file hoặc nhập D để giải mã file: ")).upper()
# # # #
# # # # if(EorD=="E"):
# # # #     # encypt
# # # #     try:
# # # #         pyAesCrypt.encryptFile("data.txt","data.txt.aes",password,keysize)
# # # #         print("file đã được mã hoá thành công !!! ")
# # # #     except EOFError as err:
# # # #         print(err)
# # # # elif(EorD=="D"):
# # # #     # decrypt
# # # #     try:
# # # #         pyAesCrypt.decryptFile("data.txt.aes","dataout.txt",password,keysize)
# # # #         print("file đã được giải mã thành công !!!")
# # # #     except EOFError as err:
# # # #         print(err)
# # # # else:
# # # #     print("Please chosse E,e OR D,d !! ")
# # # import tkinter as tk
# # # from tkinter import filedialog, messagebox
# # # import pyAesCrypt
# # #
# # # # def encrypt_file(input_file_path, output_file_path, password, keysize):
# # # #     try:
# # # #         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
# # # #         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
# # # #     except Exception as e:
# # # #         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
# # #
# # # # def decrypt_file(input_file_path, output_file_path, password, keysize):
# # # #     try:
# # # #         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
# # # #         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
# # # #     except Exception as e:
# # # #         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
# # # # def decrypt_file(input_file_path, output_file_path, password, keysize):
# # # #     try:
# # # #         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
# # # #         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
# # # #     except Exception as e:
# # # #         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
# # # #
# # # #
# # # # def open_file_dialog(entry_var):
# # # #     file_path = filedialog.askopenfilename(title="Chọn một file")
# # # #     if file_path:
# # # #         entry_var.set(file_path)
# # # #
# # # # def main():
# # # #     keysize = 64 * 1024  # 64kb size of file
# # # #
# # # #     root = tk.Tk()
# # # #     root.title("Mã hóa/Giải mã File")
# # # #
# # # #     input_file_label = tk.Label(root, text="File đầu vào:")
# # # #     input_file_label.pack(pady=5)
# # # #
# # # #     input_file_entry_var = tk.StringVar()
# # # #     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
# # # #     input_file_entry.pack(pady=5)
# # # #
# # # #     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
# # # #     input_file_button.pack(pady=5)
# # # #
# # # #     password_label = tk.Label(root, text="Mật khẩu:")
# # # #     password_label.pack(pady=5)
# # # #
# # # #     password_entry_var = tk.StringVar()
# # # #     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
# # # #     password_entry.pack(pady=5)
# # # #
# # # #     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
# # # #         input_file_entry_var.get(), input_file_entry_var.get() + ".aes", password_entry_var.get(), keysize))
# # # #     encrypt_button.pack(pady=10)
# # # #
# # # #     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
# # # #         input_file_entry_var.get() + ".aes", "decrypted_" + input_file_entry_var.get(), password_entry_var.get(), keysize))
# # # #     decrypt_button.pack(pady=10)
# # # #
# # # #     root.mainloop()
# # # #
# # # # if __name__ == "__main__":
# # # #     main()
# # #
# # # # import tkinter as tk
# # # # from tkinter import filedialog, messagebox
# # # # import pyAesCrypt
# # # #
# # # # def encrypt_file(input_file_path, output_file_path, password, keysize):
# # # #     if not password:
# # # #         messagebox.showerror("Lỗi mã hóa", "Vui lòng nhập mật khẩu!")
# # # #         return
# # # #
# # # #     try:
# # # #         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
# # # #         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
# # # #     except Exception as e:
# # # #         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
# # # #
# # # # def decrypt_file(input_file_path, output_file_path, password, keysize):
# # # #     if not password:
# # # #         messagebox.showerror("Lỗi giải mã", "Vui lòng nhập mật khẩu!")
# # # #         return
# # # #
# # # #     try:
# # # #         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
# # # #         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
# # # #     except Exception as e:
# # # #         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
# # # #
# # # # def open_file_dialog(entry_var):
# # # #     file_path = filedialog.askopenfilename(title="Chọn một file")
# # # #     if file_path:
# # # #         entry_var.set(file_path)
# # # #
# # # # def main():
# # # #     keysize = 64 * 1024  # 64kb size of file
# # # #
# # # #     root = tk.Tk()
# # # #     root.title("Mã hóa/Giải mã File")
# # # #
# # # #     input_file_label = tk.Label(root, text="File đầu vào:")
# # # #     input_file_label.pack(pady=5)
# # # #
# # # #     input_file_entry_var = tk.StringVar()
# # # #     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
# # # #     input_file_entry.pack(pady=5)
# # # #
# # # #     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
# # # #     input_file_button.pack(pady=5)
# # # #
# # # #     password_label = tk.Label(root, text="Mật khẩu:")
# # # #     password_label.pack(pady=5)
# # # #
# # # #     password_entry_var = tk.StringVar()
# # # #     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
# # # #     password_entry.pack(pady=5)
# # # #
# # # #     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
# # # #         input_file_entry_var.get(), input_file_entry_var.get() + ".aes", password_entry_var.get(), keysize))
# # # #     encrypt_button.pack(pady=10)
# # # #
# # # #     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
# # # #         input_file_entry_var.get() + ".aes", "decrypted_" + input_file_entry_var.get(), password_entry_var.get(), keysize))
# # # #     decrypt_button.pack(pady=10)
# # # #
# # # #     root.mainloop()
# # # #
# # # # if __name__ == "__main__":
# # # #     main()
# # #
# # #
# # # #
# # # # import tkinter as tk
# # # # from tkinter import filedialog, messagebox
# # # # import pyAesCrypt
# # # #
# # # # def encrypt_file(input_file_path, output_file_path, password, keysize):
# # # #     if not password:
# # # #         messagebox.showerror("Lỗi mã hóa", "Vui lòng nhập mật khẩu!")
# # # #         return
# # # #
# # # #     try:
# # # #         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
# # # #         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
# # # #     except Exception as e:
# # # #         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
# # # #
# # # # def decrypt_file(input_file_path, output_file_path, password, keysize):
# # # #     if not password:
# # # #         messagebox.showerror("Lỗi giải mã", "Vui lòng nhập mật khẩu!")
# # # #         return
# # # #
# # # #     try:
# # # #         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
# # # #         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
# # # #     except Exception as e:
# # # #         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
# # # #         print(f"Error details: {e}")
# # # #
# # # #
# # # #
# # # # def open_file_dialog(entry_var):
# # # #     file_path = filedialog.askopenfilename(title="Chọn một file")
# # # #     if file_path:
# # # #         entry_var.set(file_path)
# # # #
# # # # def main():
# # # #     keysize = 64 * 1024  # 64kb size of file
# # # #
# # # #     root = tk.Tk()
# # # #     root.title("Mã hóa/Giải mã File")
# # # #
# # # #     input_file_label = tk.Label(root, text="File đầu vào:")
# # # #     input_file_label.pack(pady=5)
# # # #
# # # #     input_file_entry_var = tk.StringVar()
# # # #     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
# # # #     input_file_entry.pack(pady=5)
# # # #
# # # #     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
# # # #     input_file_button.pack(pady=5)
# # # #
# # # #     password_label = tk.Label(root, text="Mật khẩu:")
# # # #     password_label.pack(pady=5)
# # # #
# # # #     password_entry_var = tk.StringVar()
# # # #     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
# # # #     password_entry.pack(pady=5)
# # # #
# # # #     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
# # # #         input_file_entry_var.get(), input_file_entry_var.get() + ".aes", password_entry_var.get(), keysize))
# # # #     encrypt_button.pack(pady=10)
# # # #
# # # #     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
# # # #         input_file_entry_var.get() + ".aes", "decrypted_" + input_file_entry_var.get(), password_entry_var.get(), keysize))
# # # #     decrypt_button.pack(pady=10)
# # # #
# # # #     root.mainloop()
# # # #
# # # # if __name__ == "__main__":
# # # #     main()
# # #
# # # # import tkinter as tk
# # # # from tkinter import filedialog, messagebox
# # # # import pyAesCrypt
# # # #
# # # # def encrypt_file(input_file_path, output_file_path, password, keysize):
# # # #     try:
# # # #         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
# # # #         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
# # # #     except Exception as e:
# # # #         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
# # # #
# # # # def decrypt_file(input_file_path, output_file_path, password, keysize):
# # # #     try:
# # # #         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
# # # #         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
# # # #     except Exception as e:
# # # #         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
# # # #
# # # # def open_file_dialog(entry_var):
# # # #     file_path = filedialog.askopenfilename(title="Chọn một file")
# # # #     if file_path:
# # # #         entry_var.set(file_path)
# # # #
# # # # def main():
# # # #     keysize = 64 * 1024  # 64kb size of file
# # # #
# # # #     root = tk.Tk()
# # # #     root.title("Mã hóa/Giải mã File")
# # # #
# # # #     input_file_label = tk.Label(root, text="File đầu vào:")
# # # #     input_file_label.pack(pady=5)
# # # #
# # # #     input_file_entry_var = tk.StringVar()
# # # #     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
# # # #     input_file_entry.pack(pady=5)
# # # #
# # # #     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
# # # #     input_file_button.pack(pady=5)
# # # #
# # # #     password_label = tk.Label(root, text="Mật khẩu:")
# # # #     password_label.pack(pady=5)
# # # #
# # # #     password_entry_var = tk.StringVar()
# # # #     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
# # # #     password_entry.pack(pady=5)
# # # #
# # # #     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
# # # #         input_file_entry_var.get(), input_file_entry_var.get() + ".aes", password_entry_var.get(), keysize))
# # # #     encrypt_button.pack(pady=10)
# # # #
# # # #     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
# # # #         input_file_entry_var.get() + ".aes", "dataout.txt" + input_file_entry_var.get(), password_entry_var.get(), keysize))
# # # #     decrypt_button.pack(pady=10)
# # # #
# # # #     root.mainloop()
# # #
# # # # if __name__ == "__main__":
# # # #     main()
# # #
# # # # import tkinter as tk
# # # # from tkinter import filedialog, messagebox
# # # # import os  # Thêm import os để sử dụng hàm kiểm tra file tồn tại
# # # # import pyAesCrypt
# # # #
# # # # def file_exists(file_path):
# # # #     return os.path.exists(file_path)
# # # #
# # # # def encrypt_file(input_file_path, output_file_path, password, keysize):
# # # #     if not file_exists(input_file_path):
# # # #         messagebox.showerror("Lỗi mã hóa", "File đầu vào không tồn tại!")
# # # #         return
# # # #
# # # #     try:
# # # #         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
# # # #         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
# # # #     except Exception as e:
# # # #         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
# # # #
# # # # def decrypt_file(input_file_path, output_file_path, password, keysize):
# # # #     if not file_exists(input_file_path):
# # # #         messagebox.showerror("Lỗi giải mã", "File đầu vào không tồn tại!")
# # # #         return
# # # #
# # # #     try:
# # # #         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
# # # #         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
# # # #     except Exception as e:
# # # #         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
# # # #
# # # # def open_file_dialog(entry_var):
# # # #     file_path = filedialog.askopenfilename(title="Chọn một file")
# # # #     if file_path:
# # # #         entry_var.set(file_path)
# # # #
# # # # def main():
# # # #     keysize = 64 * 1024  # 64kb size of file
# # # #
# # # #     root = tk.Tk()
# # # #     root.title("Mã hóa/Giải mã File")
# # # #
# # # #     input_file_label = tk.Label(root, text="File đầu vào:")
# # # #     input_file_label.pack(pady=5)
# # # #
# # # #     input_file_entry_var = tk.StringVar()
# # # #     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
# # # #     input_file_entry.pack(pady=5)
# # # #
# # # #     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
# # # #     input_file_button.pack(pady=5)
# # # #
# # # #     password_label = tk.Label(root, text="Mật khẩu:")
# # # #     password_label.pack(pady=5)
# # # #
# # # #     password_entry_var = tk.StringVar()
# # # #     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
# # # #     password_entry.pack(pady=5)
# # # #
# # # #     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
# # # #         input_file_entry_var.get(), input_file_entry_var.get() + ".aes", password_entry_var.get(), keysize))
# # # #     encrypt_button.pack(pady=10)
# # # #
# # # #     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
# # # #         input_file_entry_var.get() + ".aes", "dataout.txt", password_entry_var.get(), keysize))
# # # #     decrypt_button.pack(pady=10)
# # # #
# # # #     root.mainloop()
# # # #
# # # # if __name__ == "__main__":
# # # #     main()
# # # #
# # # #
# # #
# # # import tkinter as tk
# # # from tkinter import filedialog, messagebox
# # # import pyAesCrypt
# # # import os
# # #
# # # def encrypt_file(input_file_path, output_file_path, password, keysize):
# # #     try:
# # #         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
# # #         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
# # #     except Exception as e:
# # #         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
# # #
# # # def decrypt_file(input_file_path, output_file_path, password, keysize):
# # #     try:
# # #         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
# # #         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
# # #     except Exception as e:
# # #         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
# # #
# # # def open_file_dialog(entry_var):
# # #     file_path = filedialog.askopenfilename(title="Chọn một file")
# # #     if file_path:
# # #         entry_var.set(file_path)
# # #
# # # def main():
# # #     keysize = 64 * 1024  # 64kb size of file
# # #
# # #     root = tk.Tk()
# # #     root.title("Mã hóa/Giải mã File")
# # #
# # #     input_file_label = tk.Label(root, text="File đầu vào:")
# # #     input_file_label.pack(pady=5)
# # #
# # #     input_file_entry_var = tk.StringVar()
# # #     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
# # #     input_file_entry.pack(pady=5)
# # #
# # #     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
# # #     input_file_button.pack(pady=5)
# # #
# # #     password_label = tk.Label(root, text="Mật khẩu:")
# # #     password_label.pack(pady=5)
# # #
# # #     password_entry_var = tk.StringVar()
# # #     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
# # #     password_entry.pack(pady=5)
# # #
# # #     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
# # #         input_file_entry_var.get(), input_file_entry_var.get() + ".aes", password_entry_var.get(), keysize))
# # #     encrypt_button.pack(pady=10)
# # #
# # #     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
# # #         input_file_entry_var.get() + ".aes", "decrypted_" + os.path.basename(input_file_entry_var.get()), password_entry_var.get(), keysize))
# # #     decrypt_button.pack(pady=10)
# # #
# # #     root.mainloop()
# # #
# # # if __name__ == "__main__":
# # #     main()
# # #
# #
# # import os
# # import tkinter as tk
# # from tkinter import filedialog, messagebox
# # import pyAesCrypt
# #
# # def encrypt_file(input_file_path, output_file_path, password, keysize):
# #     try:
# #         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
# #         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
# #     except Exception as e:
# #         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
# #
# # def decrypt_file(input_file_path, output_file_path, password, keysize):
# #     try:
# #         # Kiểm tra xem file đầu vào tồn tại không
# #         if not os.path.exists(input_file_path):
# #             messagebox.showerror("Lỗi giải mã", "File đầu vào không tồn tại!")
# #             return
# #
# #         # Kiểm tra xem file đầu ra đã tồn tại không
# #         if os.path.exists(output_file_path):
# #             messagebox.showwarning("Cảnh báo", "File đầu ra đã tồn tại. Nó sẽ bị ghi đè!")
# #
# #         # Tạo mới file đầu ra nếu chưa tồn tại
# #         open(output_file_path, 'a').close()
# #
# #         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
# #         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
# #     except Exception as e:
# #         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
# #
# # def open_file_dialog(entry_var):
# #     file_path = filedialog.askopenfilename(title="Chọn một file")
# #     if file_path:
# #         entry_var.set(file_path)
# #
# # def main():
# #     keysize = 64 * 1024  # 64kb size of file
# #
# #     root = tk.Tk()
# #     root.title("Mã hóa/Giải mã File")
# #
# #     input_file_label = tk.Label(root, text="File đầu vào:")
# #     input_file_label.pack(pady=5)
# #
# #     input_file_entry_var = tk.StringVar()
# #     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
# #     input_file_entry.pack(pady=5)
# #
# #     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
# #     input_file_button.pack(pady=5)
# #
# #     password_label = tk.Label(root, text="Mật khẩu:")
# #     password_label.pack(pady=5)
# #
# #     password_entry_var = tk.StringVar()
# #     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
# #     password_entry.pack(pady=5)
# #
# #     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
# #         input_file_entry_var.get(), input_file_entry_var.get() + ".aes", password_entry_var.get(), keysize))
# #     encrypt_button.pack(pady=10)
# #
# #     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
# #         input_file_entry_var.get() + ".aes", "decrypted_" + input_file_entry_var.get(), password_entry_var.get(), keysize))
# #     decrypt_button.pack(pady=10)
# #
# #     root.mainloop()
# #
# # if __name__ == "__main__":
# #     main()
#
#
#
# import os
# import tkinter as tk
# from tkinter import filedialog, messagebox
# import pyAesCrypt
#
# def encrypt_file(input_file_path, output_file_path, password, keysize):
#     try:
#         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
#
# def decrypt_file(input_file_path, output_file_path, password, keysize):
#     try:
#         # Kiểm tra xem file đầu vào có tồn tại không
#         if not os.path.exists(input_file_path):
#             messagebox.showerror("Lỗi giải mã", "File đầu vào không tồn tại!")
#             return
#
#         # Tạo mới file đầu ra nếu chưa tồn tại
#         open(output_file_path, 'a').close()
#
#         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
#
# def open_file_dialog(entry_var):
#     file_path = filedialog.askopenfilename(title="Chọn một file")
#     if file_path:
#         entry_var.set(file_path)
#
# def main():
#     keysize = 64 * 1024  # 64kb size of file
#
#     root = tk.Tk()
#     root.title("Mã hóa/Giải mã File")
#
#     input_file_label = tk.Label(root, text="File đầu vào:")
#     input_file_label.pack(pady=5)
#
#     input_file_entry_var = tk.StringVar()
#     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
#     input_file_entry.pack(pady=5)
#
#     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
#     input_file_button.pack(pady=5)
#
#     password_label = tk.Label(root, text="Mật khẩu:")
#     password_label.pack(pady=5)
#
#     password_entry_var = tk.StringVar()
#     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
#     password_entry.pack(pady=5)
#
#     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
#         input_file_entry_var.get(), input_file_entry_var.get() + ".aes", password_entry_var.get(), keysize))
#     encrypt_button.pack(pady=10)
#
#     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
#         input_file_entry_var.get() + ".aes", "decrypted_" + input_file_entry_var.get(), password_entry_var.get(), keysize))
#     decrypt_button.pack(pady=10)
#
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()
#

# import tkinter as tk
# from tkinter import filedialog, messagebox
# import pyAesCrypt
# import os
#
# def encrypt_file(input_file_path, output_file_path, password, keysize):
#     print("Đường dẫn đầu vào:", input_file_path)
#     try:
#         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
#
# def decrypt_file(input_file_path, output_file_path, password, keysize):
#     print("Đường dẫn đầu vào:", input_file_path)
#     try:
#         # Kiểm tra xem file đầu vào có tồn tại không
#         if not os.path.exists(input_file_path):
#             messagebox.showerror("Lỗi giải mã", "File đầu vào không tồn tại!")
#             return
#
#         # Tạo mới file đầu ra nếu chưa tồn tại
#         open(output_file_path, 'a').close()
#
#         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
#
# def open_file_dialog(entry_var):
#     file_path = filedialog.askopenfilename(title="Chọn một file")
#     if file_path:
#         entry_var.set(file_path)
#
# def main():
#     keysize = 64 * 1024  # 64kb size of file
#
#     root = tk.Tk()
#     root.title("Mã hóa/Giải mã File")
#
#     input_file_label = tk.Label(root, text="File đầu vào:")
#     input_file_label.pack(pady=5)
#
#     input_file_entry_var = tk.StringVar()
#     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
#     input_file_entry.pack(pady=5)
#
#     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
#     input_file_button.pack(pady=5)
#
#     password_label = tk.Label(root, text="Mật khẩu:")
#     password_label.pack(pady=5)
#
#     password_entry_var = tk.StringVar()
#     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
#     password_entry.pack(pady=5)
#
#     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
#         input_file_entry_var.get(), input_file_entry_var.get() + ".aes", password_entry_var.get(), keysize))
#     encrypt_button.pack(pady=10)
#
#     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
#         input_file_entry_var.get() + ".aes", "decrypted_" + input_file_entry_var.get(), password_entry_var.get(), keysize))
#     decrypt_button.pack(pady=10)
#
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()

# import tkinter as tk
# from tkinter import filedialog, messagebox
# import pyAesCrypt
# import os
#
# def encrypt_file(input_file_path, output_file_path, password, keysize):
#     try:
#         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
#
# def decrypt_file(input_file_path, output_file_path, password, keysize):
#     try:
#         # Kiểm tra xem file đầu vào có tồn tại không
#         if not os.path.exists(input_file_path):
#             messagebox.showerror("Lỗi giải mã", "File đầu vào không tồn tại!")
#             return
#
#         # Tạo mới file đầu ra nếu chưa tồn tại
#         open(output_file_path, 'a').close()
#
#         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
#
# def open_file_dialog(entry_var):
#     file_path = filedialog.askopenfilename(title="Chọn một file")
#     if file_path:
#         entry_var.set(file_path)
#
# def main():
#     keysize = 64 * 1024  # 64kb size of file
#
#     root = tk.Tk()
#     root.title("Mã hóa/Giải mã File")
#
#     input_file_label = tk.Label(root, text="File đầu vào:")
#     input_file_label.pack(pady=5)
#
#     input_file_entry_var = tk.StringVar()
#     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
#     input_file_entry.pack(pady=5)
#
#     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
#     input_file_button.pack(pady=5)
#
#     password_label = tk.Label(root, text="Mật khẩu:")
#     password_label.pack(pady=5)
#
#     password_entry_var = tk.StringVar()
#     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
#     password_entry.pack(pady=5)
#
#     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
#         input_file_entry_var.get(), input_file_entry_var.get() + ".aes", password_entry_var.get(), keysize))
#     encrypt_button.pack(pady=10)
#
#     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
#         input_file_entry_var.get(), "decrypted_" + input_file_entry_var.get(), password_entry_var.get(), keysize))
#     decrypt_button.pack(pady=10)
#
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()


# import tkinter as tk
# from tkinter import filedialog, messagebox
# import pyAesCrypt
# import os
#
# def encrypt_file(input_file_path, output_file_path, password, keysize):
#     try:
#         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
#
# def decrypt_file(input_file_path, output_file_path, password, keysize):
#     try:
#         # Kiểm tra xem file đầu vào có tồn tại không
#         if not os.path.exists(input_file_path):
#             messagebox.showerror("Lỗi giải mã", "File đầu vào không tồn tại!")
#             return
#
#         # Tạo thư mục đầu ra nếu chưa tồn tại
#         os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
#
#         # Lấy phần tên file của đầu vào để tạo đúng đường dẫn đầu ra
#         output_file_path = os.path.join(os.path.dirname(output_file_path), os.path.basename(output_file_path))
#
#         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
#
#
# def open_file_dialog(entry_var):
#     file_path = filedialog.askopenfilename(title="Chọn một file")
#     if file_path:
#         entry_var.set(file_path)
#
# def main():
#     keysize = 64 * 1024  # 64kb size of file
#
#     root = tk.Tk()
#     root.title("Mã hóa/Giải mã File")
#
#     input_file_label = tk.Label(root, text="File đầu vào:")
#     input_file_label.pack(pady=5)
#
#     input_file_entry_var = tk.StringVar()
#     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
#     input_file_entry.pack(pady=5)
#
#     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
#     input_file_button.pack(pady=5)
#
#     password_label = tk.Label(root, text="Mật khẩu:")
#     password_label.pack(pady=5)
#
#     password_entry_var = tk.StringVar()
#     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
#     password_entry.pack(pady=5)
#
#     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
#         input_file_entry_var.get(), input_file_entry_var.get() + ".aes", password_entry_var.get(), keysize))
#     encrypt_button.pack(pady=10)
#
#     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
#         input_file_entry_var.get(), "decrypted_" + os.path.basename(input_file_entry_var.get()), password_entry_var.get(), keysize))
#     decrypt_button.pack(pady=10)
#
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()
#
# import tkinter as tk
# from tkinter import filedialog, messagebox
# import pyAesCrypt
# import os
#
# def encrypt_file(input_file_path, password, keysize):
#     try:
#         # Tạo file output với đuôi .aes
#         output_file_path = input_file_path + ".aes"
#         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
#
# def decrypt_file(input_file_path, password, keysize):
#     try:
#         # Kiểm tra xem file đầu vào có tồn tại không
#         if not os.path.exists(input_file_path):
#             messagebox.showerror("Lỗi giải mã", "File đầu vào không tồn tại!")
#             return
#
#         # Tạo thư mục đầu ra nếu chưa tồn tại
#         output_file_path = "decrypted_" + os.path.basename(input_file_path).replace(".aes", "")
#         os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
#
#         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
#
# def open_file_dialog(entry_var):
#     file_path = filedialog.askopenfilename(title="Chọn một file")
#     if file_path:
#         entry_var.set(file_path)
#
# def main():
#     keysize = 64 * 1024  # 64kb size of file
#
#     root = tk.Tk()
#     root.title("Mã hóa/Giải mã File")
#
#     input_file_label = tk.Label(root, text="File đầu vào:")
#     input_file_label.pack(pady=5)
#
#     input_file_entry_var = tk.StringVar()
#     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
#     input_file_entry.pack(pady=5)
#
#     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
#     input_file_button.pack(pady=5)
#
#     password_label = tk.Label(root, text="Mật khẩu:")
#     password_label.pack(pady=5)
#
#     password_entry_var = tk.StringVar()
#     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
#     password_entry.pack(pady=5)
#
#     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
#         input_file_entry_var.get(), password_entry_var.get(), keysize))
#     encrypt_button.pack(pady=10)
#
#     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
#         input_file_entry_var.get(), password_entry_var.get(), keysize))
#     decrypt_button.pack(pady=10)
#
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()
# import tkinter as tk
# from tkinter import filedialog, messagebox
# import pyAesCrypt
# import os
#
# def encrypt_file(input_file_path, password, keysize):
#     try:
#         # Tạo file output với đuôi .aes
#         output_file_path = input_file_path + ".aes"
#         pyAesCrypt.encryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Mã hóa thành công", "File đã được mã hóa thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi mã hóa", f"Lỗi: {str(e)}")
#
# def decrypt_file(input_file_path, password, keysize):
#     try:
#         # Print or log the input file path for debugging
#         print("Input file path:", input_file_path)
#
#         # Kiểm tra xem file đầu vào có phải là file mã hóa không
#         if not input_file_path.endswith(".aes"):
#             messagebox.showerror("Lỗi giải mã", "File không có đuôi .aes!")
#             return
#
#         # Kiểm tra xem file đầu vào có tồn tại không
#         if not os.path.exists(input_file_path):
#             messagebox.showerror("Lỗi giải mã", "File đầu vào không tồn tại!")
#             return
#
#         # Tạo thư mục đầu ra nếu chưa tồn tại
#         output_file_path = "decrypted_" + os.path.basename(input_file_path).replace(".aes", "")
#         os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
#
#         pyAesCrypt.decryptFile(input_file_path, output_file_path, password, keysize)
#         messagebox.showinfo("Giải mã thành công", "File đã được giải mã thành công!")
#     except Exception as e:
#         messagebox.showerror("Lỗi giải mã", f"Lỗi: {str(e)}")
#
# def open_file_dialog(entry_var):
#     file_path = filedialog.askopenfilename(title="Chọn một file")
#     if file_path:
#         entry_var.set(file_path)
#
# def main():
#     keysize = 64 * 1024  # 64kb size of file
#
#     root = tk.Tk()
#     root.title("Mã hóa/Giải mã File")
#
#     input_file_label = tk.Label(root, text="File đầu vào:")
#     input_file_label.pack(pady=5)
#
#     input_file_entry_var = tk.StringVar()
#     input_file_entry = tk.Entry(root, textvariable=input_file_entry_var, width=50)
#     input_file_entry.pack(pady=5)
#
#     input_file_button = tk.Button(root, text="Chọn file", command=lambda: open_file_dialog(input_file_entry_var))
#     input_file_button.pack(pady=5)
#
#     password_label = tk.Label(root, text="Mật khẩu:")
#     password_label.pack(pady=5)
#
#     password_entry_var = tk.StringVar()
#     password_entry = tk.Entry(root, textvariable=password_entry_var, show="*")
#     password_entry.pack(pady=5)
#
#     encrypt_button = tk.Button(root, text="Mã hóa", command=lambda: encrypt_file(
#         input_file_entry_var.get(), password_entry_var.get(), keysize))
#     encrypt_button.pack(pady=10)
#
#     decrypt_button = tk.Button(root, text="Giải mã", command=lambda: decrypt_file(
#         input_file_entry_var.get(), password_entry_var.get(), keysize))
#     decrypt_button.pack(pady=10)
#
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()




# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import padding
# import os
#
# def encrypt_file(input_file, output_file, key):
#     with open(input_file, 'rb') as file:
#         plaintext = file.read()
#
#     padder = padding.PKCS7(algorithms.AES.block_size).padder()
#     padded_data = padder.update(plaintext) + padder.finalize()
#
#     # Tạo IV ngẫu nhiên và sử dụng nó trong quá trình mã hóa
#     iv = os.urandom(16)
#     cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
#     encryptor = cipher.encryptor()
#     ciphertext = encryptor.update(padded_data) + encryptor.finalize()
#
#     # Ghi IV + Ciphertext vào file đầu ra
#     with open(output_file, 'wb') as file:
#         file.write(iv + ciphertext)
#
# def decrypt_file(input_file, output_file, key):
#     with open(input_file, 'rb') as file:
#         data = file.read()
#
#     # Trích xuất IV và Ciphertext từ file đầu vào
#     iv = data[:16]
#     ciphertext = data[16:]
#
#     # Sử dụng IV được trích xuất trong quá trình giải mã
#     cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
#     decryptor = cipher.decryptor()
#     decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
#
#     # Bỏ đệm dữ liệu đã giải mã
#     unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
#     plaintext = unpadder.update(decrypted_data) + unpadder.finalize()
#
#     # Ghi văn bản đã giải mã vào file đầu ra
#     with open(output_file, 'wb') as file:
#         file.write(plaintext)
#
# # Sử dụng ví dụ:
# key = os.urandom(32)  # Khóa 256-bit cho AES
# input_file = 'dataout.txt'
# encrypted_file = 'encrypted_file.enc'
# decrypted_file = 'decrypted_file.txt'
#
# # Mã hóa file
# encrypt_file(input_file, encrypted_file, key)
#
# # Giải mã file
# decrypt_file(encrypted_file, decrypted_file, key)

from flask import Flask, render_template, request, redirect, send_from_directory
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

app = Flask(__name__)

# Đường dẫn đến thư mục lưu trữ các file
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Khóa cho AES
key = os.urandom(32)


# Hàm mã hoá file
def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file, 'wb') as file:
        file.write(iv + ciphertext)


# Hàm giải mã file
def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        data = file.read()

    iv = data[:16]
    ciphertext = data[16:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(decrypted_data) + unpadder.finalize()

    with open(output_file, 'wb') as file:
        file.write(plaintext)


# Route để hiển thị trang web
@app.route('/')
def index():
    return render_template('index.html')


# Route để xử lý tải lên và thực hiện mã hoá
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file:
            # Tạo thư mục nếu chưa tồn tại
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            # Đường dẫn đầy đủ
            filename = os.path.join(app.config['UPLOAD_FOLDER'], 'dataout.txt')

            file.save(filename)

            # Mã hoá file sau khi tải lên
            encrypt_file(filename, filename + '.enc', key)

    return redirect(request.url)


# Route để tải về file đã giải mã
@app.route('/download', methods=['GET'])
def download_file():
    # Giải mã file trước khi tải về
    decrypt_file(os.path.join(app.config['UPLOAD_FOLDER'], 'dataout.txt.enc'),
                 os.path.join(app.config['UPLOAD_FOLDER'], 'decrypted_dataout.txt'), key)

    return send_from_directory(app.config['UPLOAD_FOLDER'], 'decrypted_dataout.txt', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)






