import random
from tkinter import *


def password_generator(min_length=8, max_length=15):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    all_chars = letters + numbers
    return ''.join(random.choice(all_chars) for _ in range(random.randint(min_length, max_length)))


def generate_and_display_password():
    password = password_generator(8, 15)
    entry.delete(0, END)
    entry.insert(0, password)


window = Tk()
window.title("Password Generator")
window.geometry("400x300")
window.resizable(False, False)
window.configure(bg="#2C3E50")

title_label = Label(
    window,
    text="Strong Password Generator",
    font=("Helvetica", 18, "bold"),
    bg="#2C3E50",
    fg="#ECF0F1"
)
title_label.pack(pady=20)


entry = Entry(
    window,
    width=25,
    font=("Courier", 18),
    justify="center",
    bg="#ECF0F1",
    fg="#2C3E50",
    relief=FLAT
)
entry.pack(pady=10)


button = Button(
    window,
    text="Generate Password",
    font=("Helvetica", 16, "bold"),
    bg="#1ABC9C",
    fg="white",
    padx=10,
    pady=5,
    relief=FLAT,
    command=generate_and_display_password
)
button.pack(pady=20)


window.mainloop()

entry = Entry(window, width=30, font=("Arial", 20), bg="lightblue", fg="black")
entry.pack()

button = Button(window, text="Generate Password", font=("Arial", 20), bg="black", fg="white", command=generate_and_display_password)
button.pack()


mainloop()