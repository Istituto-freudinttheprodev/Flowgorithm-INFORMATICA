print("Inserisci il primo numero")
numero1 = float(input())
print("Inserisci il secondo numero")
numero2 = float(input())
print("Inserisci il terzo numero")
numero3 = float(input())
if numero1 <= numero2 and numero1 <= numero3:
    if numero2 <= numero3:
        minore = numero1
        medio = numero2
        maggiore = numero3
    else:
        if numero1 <= numero3:
            minore = numero1
            medio = numero3
            maggiore = numero2
        else:
            minore = numero3
            medio = numero1
            maggiore = numero2
else:
    if numero2 <= numero1 and numero2 <= numero3:
        if numero1 <= numero3:
            minore = numero2
            medio = numero1
            maggiore = numero3
        else:
            minore = numero2
            medio = numero3
            maggiore = numero1
    else:
        if numero1 <= numero2:
            minore = numero3
            medio = numero1
            maggiore = numero2
        else:
            minore = numero3
            medio = numero2
            maggiore = numero1
if numero1 == numero2 and numero2 == numero3:
    print("I tre numeri sono uguali")
else:
    print("I numeri ordinati dal minore al maggiore sono:")
    print(minore)
    print(medio)
    print(maggiore)