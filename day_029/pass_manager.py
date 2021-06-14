import tkinter as tk
import json
from tkinter import messagebox

from day_005.utils import generate_password


def on_generate_click():
    password = generate_password(20)
    password_input.insert(0, password)


def on_save_click():
    website = website_input.get()
    login = login_input.get()
    password = password_input.get()

    if not website:
        messagebox.showwarning(title='Website', message='Fill in website.')
    elif not login:
        messagebox.showwarning(title='Email/username', message='Fill in email/username.')
    elif not password:
        messagebox.showwarning(title='password', message='Fill in password.')

    new_entry = {
        'website': website,
        'login': login,
        'password': password,
    }

    is_ok = messagebox.askokcancel(title='Password entry', message=f'Website: {website}\nEmail/username: {login}\n'
                                                                   f'Password: {password}\n Is that right?')
    if is_ok:
        with open('data.txt', 'a') as f:
            f.write(f'{json.dumps(new_entry)}\n')
        website_input.delete(0, tk.END)
        login_input.delete(0, tk.END)
        password_input.delete(0, tk.END)


window = tk.Tk()
window.config(padx=40, pady=20)
window.title("Password Manager")

website_label = tk.Label(text="Website: ")
website_label.grid(column=0, row=0)
website_input = tk.Entry(width=38)
website_input.grid(column=1, row=0, columnspan=2)

login_label = tk.Label(text="Email/username: ")
login_label.grid(column=0, row=1)
login_input = tk.Entry(width=38)
login_input.grid(column=1, row=1, columnspan=2)

password_label = tk.Label(text="Password: ")
password_label.grid(column=0, row=2)
password_input = tk.Entry(width=21)
password_input.grid(column=1, row=2)

password_button = tk.Button(text="Generate and copy", width=13, command=on_generate_click)
password_button.grid(column=2, row=2)

save_button = tk.Button(text="Save", width=30, command=on_save_click)
save_button.grid(column=1, row=3, columnspan=2)

window.mainloop()
