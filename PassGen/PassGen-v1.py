# Libs
from time import sleep
from random import choice

# Colors
ciano = '\033[1;36m'
branco = '\033[1;97m'
vermelho = '\033[1;31m'

print(branco + "=" * 50)
print(ciano + "-- PassGen --".center(50))
print(branco + "=" * 50)

print(ciano + "Escolha os tipos de caracteres da senha e tamanho.")

print(branco + "=" * 50)


# Def Gen
def GenPass(password, passlen, passtype):
    type1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    type2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    type3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    type4 = ["!", "@", "#", "$", "%", "&", "*"]
    
    contador_caracteres = 0
    if passtype == "1":
        contador_caracteres += 1
        
    if passtype == "2":
        contador_caracteres += 1
    
    if passtype == "3":
        contador_caracteres += 1

    if passtype == "4":
        contador_caracteres += 1

    if passtype == "12":
        contador_caracteres += 2

    if passtype == "123":
        contador_caracteres += 3

    if passtype == "1234":
        contador_caracteres += 4
    
    if passtype == "13":
        contador_caracteres += 2

    if passtype == "14":
        contador_caracteres += 2

    if passtype == "23":
        contador_caracteres += 2

    if passtype == "24":
        contador_caracteres += 2

    lenpass = passlen / contador_caracteres

    for x in range(0, int(lenpass)):
        if passtype == "1":
            password += choice(type1)
        
        elif passtype == "2":
            password += choice(type2)
        
        elif passtype == "3":
            password += choice(type3)

        elif passtype == "4":
            password += choice(type4)

        elif passtype == "12":
            password += choice(type1)
            password += choice(type2)

        elif passtype == "123":
            password += choice(type1)
            password += choice(type2)
            password += choice(type3)

        elif passtype == "1234":
            password += choice(type1)
            password += choice(type2)
            password += choice(type3)
            password += choice(type4)
        
        elif passtype == "13":
            password += choice(type1)
            password += choice(type3)

        elif passtype == "14":
            password += choice(type1)
            password += choice(type4)

        elif passtype == "23":
            password += choice(type2)
            password += choice(type3)

        elif passtype == "24":
            password += choice(type2)
            password += choice(type4)

    print(branco + "=" * 50)
    return print(ciano + f"Password: → {password} ←")

# Start gen
password = ""

while True:
    print(ciano + "[ 1 ] abcd")
    print(ciano + "[ 2 ] ABCD")
    print(ciano + "[ 3 ] 1234")
    print(ciano + "[ 4 ] !@#$")

    passtype = str(input("Select numbers: "))
    while passtype != "1" and passtype == "2" and passtype != "3" and passtype != "4" and passtype != "12" and passtype != "123" and passtype != "1234" and passtype != "13" and passtype != "14" and passtype != "23" and passtype != "24":
        passtype = str(input("Select numbers: "))

    passlen = int(input("Size: "))
    while passlen > 100:
        passlen = int(input("Size: "))
    
    try:
        GenPass(password, passlen, passtype)

        print(branco + "=" * 50)

        ## Loop Gen
        print(ciano + "[ 1 ] Sim")
        print(ciano + "[ 2 ] Não")
        
        go = int(input(ciano + "Continue? "))
        while go != 1 and go != 2:
            go = int(input(ciano + "Continue? "))

        if go == 2:
            print(branco + "=" * 50)
            print(ciano + "-- PassGen Close --".center(50))
            print(branco + "=" * 50)
            
            break
        
        else:
            print(branco + "=" * 50)
            print(ciano + "-- PassGen --".center(50))
            print(branco + "=" * 50)
    
    except Exception as erro:
        print(branco + "=" * 50)
        print(vermelho + f"Erro: {erro}")
        print(branco + "=" * 50)
