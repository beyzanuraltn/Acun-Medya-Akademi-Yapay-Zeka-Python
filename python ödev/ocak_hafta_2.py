# tek mi çift mi?
sayi = int(input("Bir sayı girin: "))
if sayi % 2 == 0:
    print(f"{sayi} çift bir sayıdır.")
else:
    print(f"{sayi} tek bir sayıdır.")

    print("************************************")

# harf notu hesaplama
notu = int(input("Notunuzu girin: "))

if 90 <= notu <= 100:
    harf_notu = "A"
elif 80 <= notu <= 89:
    harf_notu = "B"
elif 70 <= notu <= 79:
    harf_notu = "C"
elif 60 <= notu <= 69:
    harf_notu = "D"
elif 0 <= notu <= 59:
    harf_notu = "F"
else:
    harf_notu = "Geçersiz not"

print(f"Notunuz: {harf_notu}")

