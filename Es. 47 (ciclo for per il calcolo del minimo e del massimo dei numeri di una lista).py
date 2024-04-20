minimo = 0
massimo = 0
print("Quanti numeri desideri inserire nella lista?")
listadinumeri = int(input())
listadinumeri = listadinumeri - 1
for i in range(0, listadinumeri + 1, 1):
    print("Inserisci un numero della lista")
    numerodellalista = float(input())
    if i == 0:
        minimo = numerodellalista
        massimo = numerodellalista
    else:
        if numerodellalista > massimo:
            massimo = numerodellalista
        else:
            if numerodellalista < minimo:
                minimo = numerodellalista
print("Il numero massimo della lista è:")
print(massimo)
print("Il numero minimo della lista è:")
print(minimo)