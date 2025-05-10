from tkinter import *

root = Tk()
root.title("🧮 Modern Calculator")
root.geometry("360x500")
root.resizable(False, False)
root.configure(bg="#2C3E50")  

islem = ""

def hesapla(tus):
    global islem
    if tus in "0123456789.":
        ekran.insert(END, tus)
        islem += tus
    elif tus in "+-*/":
        ekran.insert(END, tus)
        islem += tus
    elif tus == "=":
        try:
            sonuc = eval(islem, {"__builtins__": None}, {})
            ekran.delete(0, END)
            ekran.insert(END, str(sonuc))
            islem = str(sonuc)
        except:
            ekran.delete(0, END)
            ekran.insert(END, "Error")
            islem = ""
    elif tus == "C":
        ekran.delete(0, END)
        islem = ""

ekran = Entry(root, width=16, font=("Courier New", 28), bd=0, bg="#ECF0F1", fg="#2C3E50", justify=RIGHT, relief=FLAT)
ekran.grid(row=0, column=0, columnspan=4, ipady=20, pady=20, padx=10)

button_bg = "#34495E"
button_fg = "#ECF0F1"
button_active = "#1ABC9C"


butonlar = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    ".", "0", "=", "+",
    "C"
]


row = 1
col = 0
for btn in butonlar:
    komut = lambda x=btn: hesapla(x)
    b = Button(root, text=btn, font=("Helvetica", 20, "bold"), fg=button_fg, bg=button_bg,
               activebackground=button_active, activeforeground="white",
               width=4, height=2, bd=0, relief=FLAT, command=komut)
    b.grid(row=row, column=col, padx=8, pady=8)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()