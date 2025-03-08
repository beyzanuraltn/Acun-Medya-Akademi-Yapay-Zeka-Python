# Kullanıcıdan adını, yaşını ve doğum yılını alan program
ad = input("Adınızı girin: ")
yas = int(input("Yaşınızı girin: "))
dogum_yili = int(input("Doğum yılınızı girin: "))
print(f"Merhaba {ad}! {yas} yaşındasın ve {dogum_yili} yılında doğmuşsun.")


# Kullanıcıdan iki sayı alıp hesaplama yapan program
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
bolum = sayi1 / sayi2 if sayi2 != 0 else "Bölme hatası (0'a bölünemez)"  # Bölme hatasını kontrol ediyoruz

print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")
