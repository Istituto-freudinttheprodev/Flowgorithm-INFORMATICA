print("Inserisci il primo numero")
numero1 = float(input())
print("Inserisci il secondo numero")
numero2 = float(input())
if numero1 > numero2:
    print("I numeri ordinati dal minore al maggiore sono:")
    print(numero2)
    print(numero1)
else:
    if numero2 > numero1:
        print("I numeri ordinati dal minore al maggiore sono:")
        print(numero1)
        print(numero2)
    else:
        print("I due numeri sono uguali")