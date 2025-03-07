def write_to_file(filename):
    with open(filename, 'w') as file:
      text = input("Bir metin giriniz: ")
      file.write(text)
      print("Girdiğiniz metin dosyaya yazıldı.\n")

def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read
        print("Dosya içeriği:")
        print(content)

def write_multiple_lines(filename):
    with open(filename, 'w') as file:
        print("Lütfen 5 farklı satır giriniz:")
        for i in range (5):
            line = input(f"Satır {i+1}: ")
            file.write(line + "\n")
            print("Girdiğiniz metinler dosyaya yazıldı.\n")

def read_lines(filename):
    with open(filename,"r") as file:
        print("Dosyadaki satırlar:")
        for line in file:
            print(line.strip())

filename = "output.txt"
write_to_file(filename)
read_from_file(filename)

filename_lines = "lines.txt"
write_multiple_lines(filename_lines)
read_lines(filename_lines)