import random
from tkinter import *

window= Tk()
window.title("Password Generator")
window.geometry("400x400")
window.resizable(FALSE,FALSE)

letters = 'abcdefghijklmnopqrstuvwxyz'
letters += letters.upper()
numbers = '0123456789'

#creat a pasword just numbers and letter no special characters
def password_generator(min_length=8,max_length=15):
    password =""

    for x in range(min_length,max_length):
        password += random.choice(letters + numbers)#burda iki listeyi birleştirip randomdan alıyoruz
    return password



def generate_and_display_password():
    password = password_generator(8, 15)
    entry.delete(0, END)  # önceki şifreyi 0ıncı indexten sonuncu indekse kadar siler
    entry.insert(0, password)  # Yeni şifreyi ekle



# print(password_generator(8,15))#burda min ve max uzunluğu veriyoruz


entry = Entry(window, width=30, font=("Arial", 20), bg="white", fg="black")
entry.pack()

button = Button(window, text="Generate Password", font=("Arial", 20), bg="black", fg="white", command=generate_and_display_password)
button.pack()


mainloop()