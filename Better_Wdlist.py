from itertools import product
import string

min_letras = int(input("• Enter min length of password: "))
max_letras = int(input("• Enter max length of password: "))
file_name = input("\n • Insert the file name: ")
arq_txt = open(file_name, 'w')
lista1 = str(input("\n • Do you wanna a personal list?  [y/n]"))
cont = 0
if lista1 == 'y':
    nome = str(input("\n • Insert the fist name [Skip Press Enter]"))
    sobrenome = str(input("\n • Insert the middle or last name [Skip Press Enter]"))
    dia = str(input("\n • Insert the Birthday [Skip Press Enter]"))
    mes = str(input("\n • Insert Month [Skip Press Enter]"))
    animal = str(input("\n • Insert the pet name [Skip Press Enter]"))
    letras = nome + sobrenome + dia + mes + animal
else:
    letras = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

for i in range(int(min_letras), int(max_letras) + 1):
       for j in product(letras, repeat=i):
           word = "".join(j)
           arq_txt.write(word + '\n')
           cont += 1

print("Wordlist of {} passwords created".format(cont))

