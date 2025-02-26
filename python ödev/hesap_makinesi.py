kullanici = input("Lütfen adınızı girin: ")  # Kullanıcıdan özelleştirme için isim aldım.
print("Hesap makinesi programına hoşgeldiniz, " + kullanici)

def hesap_makinesi(sayi1,sayi2,islem):#fonksiyon oluşturuyorum
#girilen işleme göre işlem yapılacak
    if islem == "+":
        return (f"İşleminiz: {sayi1} + {sayi2} Sonucunuz {sayi1 + sayi2}")
    elif islem == "-":
        return(f"İşleminiz: {sayi1} - {sayi2} Sonucunuz: {sayi1 - sayi2}")
    elif islem == "*":
        return(f"İşleminiz: {sayi1} * {sayi2} Sonucunuz: {sayi1 * sayi2}")
    elif islem == "/":
        if sayi2 == 0:
            return("Bölme işlemi için ikinci sayı 0 olamaz!")
        return(f"İşleminiz: {sayi1} / {sayi2} Sonucunuz: {sayi1 / sayi2}")
    else:
        return("Geçersiz işlem Tekrar deneyin!")
#kullanıcıdan giriş alıyorum
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
islem = input("Yapmak istediğiniz işlemi girin (+, -, *, /): ")

sonuc=hesap_makinesi(sayi1,sayi2,islem)#fonksiyonu bir değişkene atıyorum
print(sonuc)#sonucu yazdırıyorum