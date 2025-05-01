import random

print("1-100 arasinda sence tahmin ettiğim sayiyi bulabilecek misin?")
print("Haydi baslayalim, 5 sansin var")

tahmin_edilen = random.randint(1,100)

chance = 5
tahmin_sayisi = 0

while tahmin_sayisi< chance:

    tahmin_sayisi +=1
    tahmin = int(input("Tahminini gir: "))

    if tahmin == tahmin_edilen:
        print("Tekbrikler , sayiyi dogru tahmin ettiniz")
        break

    elif  tahmin_sayisi >= chance and tahmin != tahmin_edilen:
        print("Sayiyi bilemedin tekrar dene")

    elif tahmin > tahmin_edilen:
        print("Your guess is higher")

    elif tahmin < tahmin_edilen:
        print("Your guess is lesser")