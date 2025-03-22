def hesap_makinesi(sayi1, sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum = sayi1 / sayi2 if sayi2 != 0 else "Tanımsız"
    return toplam, fark, carpim, bolum

s1, s2 = 10, 5
sonuclar = hesap_makinesi(s1, s2)
print(f"Toplam: {sonuclar[0]}, Fark: {sonuclar[1]}, Çarpım: {sonuclar[2]}, Bölüm: {sonuclar[3]}")


def palindrom_kontrol(kelime):
    return kelime == kelime[::-1]

kelime = "kek"
print(f"'{kelime}' kelimesi palindrom mu? {palindrom_kontrol(kelime)}")


def yas_hesapla(dogum_yili):
    mevcut_yil = 2025
    yas = mevcut_yil - dogum_yili
    kac_yil_sonra = 100 - yas if yas < 100 else 0
    return kac_yil_sonra

dogum_yili = 1990
print(f"100 yaşına ulaşmana {yas_hesapla(dogum_yili)} yıl kaldı.")
