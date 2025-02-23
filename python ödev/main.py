print("kodlamio")
baslik = "taşıt kredisi"
print(baslik)
#string=metinsel ifade
baslik = "ihtiyaç kredisi"
print(baslik)
#integer=tam sayı
vade = 36
ekvade = 6
vade2 = "36"
#float,decimal,double=ondalıklı sayı
aylikOdeme = 200.50
#bool,booelan = true,false değeri tutar.karar yapılarında kullanılır.
yukselisteMi = False
#matematiksel operatörler

# +
print(5+5)
print(vade +12)
print(vade+ ekvade)
print(36+6)
# -
print(5-5)
print(vade - 12)
print(vade - ekvade)
print(36-6)
# *
print(5*5)
print(vade*2)
print(vade *ekvade)
print(10*10)
# /
print(5/5)
print(vade/2)
print(vade /ekvade)
print(10/2)

yeniVade =vade/2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % = mod operatörü
print(10 % 2)
print(vade %5 )
print(vade % ekvade)
print(30 % 10)

#mantıksal operatörler:çıktısı booelan değer verir.
print(1 == 1)
print(1 == 2)

#CTRL K + CTRL C
print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1!=1)
print(1!=2)

# or and 

#or(veya) kullanlırsa 1'i doğru olsa bile tüm operatörün döneceği  değer doğru olur.
print(1>2 or 5>2)

#and(ve) operatöründe iki değerde true ise true çıktısı verir.
print(1>2 and 5>2)
#her iki taraf ayrı değerlendirilir,soldan başlanarak karşılaştırılır.
print(1>2 or 5>2 and 3>2)
print(1>2 and 5>2 and 3>2)#false değer verir çünkü her iki değişkende true çıktısını vermedi.
print(2>1 or 1>2 and 3>2)#true döner çünkü or kısmında bir doğru ve and kısmında 2 doğru var.

#karar yapıları
#if else

sayi1 = 15
sayi2 = 15
#sayi1 sayi2den büyükse ekrana sayi1 daha büyüktür yazdır.

#indent(if bloğunun içinde olması için print'in önüne tab'la boşluk koyulur.)
if sayi1<=sayi2:
    print("sayi1 sayi2'den küçüktür.")
  
elif sayi1 == sayi2:
    print("iki sayı eşittir.")
#eğer if ve else bloklarından hiçbirine girmezse
else:
    print("sayi1 sayi2'den büyüktür.")

print("burası if bloğunun dışıdır.")

print("****************")

if sayi1<=sayi2:
    print("sayi1 sayi2'den küçüktür.")
if sayi1 == sayi2:
    print("iki sayı eşittir.")
else:
    print("sayi1 sayi2'den büyüktür.")
    
print("burası if bloğunun dışıdır.")