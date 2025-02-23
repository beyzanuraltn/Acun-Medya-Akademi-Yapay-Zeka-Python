from human import Human
import matematik as math

math.bol(10,2)

faiz =1.59
vade = "36"
krediAdi = "ihtiyaç kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
#print(int(krediAdi))
faiz=str (faiz)
print(type(faiz))

#kullanıcıdan girdi almayı sağlayan fonksiyon input
vade=int(input("lütfen istediğiniz vade sayısısnı girin: "))
print(type(vade))
vade = vade + 12

#string interpolation
#seçtiğiniz vade sonucu ortaya çıkan vade:
print("seçtiğiniz vade sonucu ortaya çıkan vade: " +str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade:{vadeSayisi} " .format(vadeSayisi=vade))

isim =input("isminizi giriniz: ")
metin = "merhaba {name}".format(name=123)
print(metin)

#f-string
metin =f"hoşgeldiniz {1+1}"
print(metin)

#  listeler
#  döngüler 
#  fonksiyonlar

krediler= ["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]

print(type(krediler))

print(krediler[0])

print(len(krediler))
# print(krediler[3]) hata verir index 0'dan başladığı için eleman sayısının 1 eksiğini alırız.
#len:uzunluğu kaç eleman olduğunu verir.

krediler.append("özel kredi")
#liste sonuna eleman ekler:append
print(krediler)

krediler.append("x kredisi")
print(krediler)

krediler.pop(0)
#liste sonundan eleman siler.son eleman indeksi: -1.
print(krediler)

krediler.append("taşıt kredisi")
print(krediler)

krediler.remove("taşıt kredisi")
#bu değerde bulduğu ilk elemanı siler
print(krediler)

krediler.extend(["y kredisi","z kredisi"])
print(krediler)

#for 
#i=0 i<10
for i in range(10):
    #i 0'dan başlayıp range sayesinde birer birer artıyor.
      print("xx")   
      print(i)
print("***********")
for i in range (5,11):
            print(i)
print("***********")
for i in range (0,51,10):
    print(i)
print("***********")
# for i in range (0.1,0.5):
#        print(i)

krediler= ["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]
for kredi in krediler:
    print(krediler)
print("***********")
for i in range (len(krediler)):
       print(krediler[i])
print("***********")    
#sonsuz döngü   
i=0 
while i<10:
    print("x")
    i+=1
print("y")

print("***********")

while True:
    print("x")  
    break

print("*****Son döngü******")
krediler= ["ihtiyaç kredisi","taşıt kredisi","konut kredisi"]   
i=0
while i<len(krediler):
     i+=1
     print(i)
     print(krediler[i])
     if krediler[i]=="konut kredisi":
         break
     
 #fonksiyonlar

fiyat = 100
indirim = 20
#definiton define
def calculate():
      print(100-20)

def calculateWithParams(fiyat,indirim):
      print(fiyat-indirim)

def sayHello(name):
      print(f"merhaba {name}")


calculate()
calculateWithParams(50,10) 
calculateWithParams(100,30)
sayHello("beyza")
sayHello("enes")
sayHello("esra")

def calculateAndReturn(fiyat,indirim):
      return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat+10)

def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return price-discount

print("***********")
# fonk1 = calculatePrice(100,50)
fonk2 = calculatePrice(300,100)
# print("159.satır:{fonk1}")
print("160.satır:{fonk2}")    
print("***********")

#sınıflar = classlar
#modules
#paket yöneticisi
#self = this

#instance = örnek
human1 = Human("enes")
human1.talk("merhaba")
human1.walk()
print(human1)

human2 = Human("halit")
human2.talk("selam")
human2.walk()
print(human2)   

     
     