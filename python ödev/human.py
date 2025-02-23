class Human:
    #built-in #constructor #init = initialize
    def __init__(self,name):
      self.name = name
      print("bir human instance üretildi")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
         print(f"{self.name}: {sentence}")      
    def walk(self):
          print(f"{self.name}: is walking...")