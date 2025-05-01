from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("450x500")
root.resizable(FALSE,FALSE)

#equation hafızamız olur.
islem= ""
 
def hesapla(tus):
    global islem
    if tus in "0123456789":
        ekran.insert(END,tus)
        islem = islem + tus

    if tus in "+-/*":
        ekran.insert(END,tus)
        islem = islem + tus

    if tus == "=":
        ekran.delete(0,END)
        hesap = eval(islem, {"__builtins__": None}, {})
        islem = str(hesap)
        ekran.insert(END,islem)

    #islem tamamlandıktan sonra yeni işlem içn islemi sıfırladık islem="" şeklinde
    if tus == "C":
        ekran.delete(0,END)
        islem =""



ekran = Entry(width=30,justify=RIGHT)
ekran.grid(row=0,column=0,columnspan=3,ipadx=8, ipady=20, padx=10, pady=10)

#hesap makinesi görünümünü vermek için listeye atayım for döngüsünü kurduk
liste =["0","1","2","3","4","5","6","7","8","9",".","+","-","*","/","=","C"]

sira =1
sutun = 0

#x'i döngüdeki i ye eşledik
#commandı komut lamba fonksiyonuna attık
# Bu yapı sayesinde, örneğin i = "3" olduğunda, buton basıldığında hesapla("3") çalışır.

for i in liste:
    komut = lambda x=i: hesapla(x)
    Button(text=i,width=8,height=2,relief=GROOVE,font=("Arial"),command=komut).grid(row=sira,column=sutun)
    sutun += 1
    if sutun > 2:
        sutun = 0
        sira +=1


mainloop()