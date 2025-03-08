# 1'den 100'e kadar sayıları yazdırma döngüsü
for sayi in range(1, 101):
    print(sayi)

print("************************************")   

# 1'den 100'e kadar sadece çift sayıları yazdırmak için
for sayi in range(1, 101):
    if sayi % 2 == 0:
        print(sayi)

print("************************************")   

#Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan program:
sayi = int(input("Bir sayı girin: "))
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i  # Faktoriyel hesaplama
print(f"{sayi}! = {faktoriyel}")

print("************************************")   

# 1'den 100'e kadar olan tüm asal sayıları bulan program:
for sayi in range(2, 101):  
    asal = True
    for i in range(2, int(sayi ** 0.5) + 1):  
            asal = False
            break
    if asal:
        print(sayi)

