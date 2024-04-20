print("Inserisci il primo numero: ")
num1 = float(input())
print("Inserisci il secondo numero: ")
num2 = float(input())
if num1 > num2:
    print("Il primo numero è maggiore del secondo")
else:
    if num1 == num2:
        print("Il primo numero è uguale al secondo")
    else:
        if num1 < num2:
            print("Il primo numero è minore del secondo")