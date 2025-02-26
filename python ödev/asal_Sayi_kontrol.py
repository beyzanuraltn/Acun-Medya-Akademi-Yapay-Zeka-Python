kullanici = input("Lütfen adınızı girin: ")  # Kullanıcıdan özelleştirme için isim aldım.
print("Asal Sayı Kontrol Programına Hoşgeldiniz, " + kullanici)

sayi = int(input("Bir sayı girin: "))  # Kullanıcıdan kontrol edilecek sayıyı alıp alıp integer'a çevirdim.

# Asal sayı kontrolü
if sayi > 1: # 1'den büyük sayılar için kontrol yapılmalı.
    for i in range(2, sayi): # 2'den başlayarak sayıya kadar olan sayılarla bölünüp bölünmediğini kontrol ediyorum..
        if sayi % i == 0: # Eğer sayı bölünüyorsa kalan yoksa asal sayı değildir.
            print(sayi, "bir asal sayı değildir.")
            break  
    else:
        print(sayi, "bir asal sayıdır.")
else:
    print(sayi, "bir asal sayı değildir.")

