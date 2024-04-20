lista1 = [0] * (3)
lista2 = [0] * (3)

print("Inserisci 3 elementi (numeri) per la lista n°1 (un numero a messaggio)")
for i in range(0, 2 + 1, 1):
    lista1[i] = int(input())
print("Inserisci 3 elementi (numeri) per la lista n°2 (un numero a messaggio)")
for i in range(0, 2 + 1, 1):
    lista2[i] = int(input())
print("Il calcolo dei prodotti tra gli elementi corrispondenti delle liste è:")
for i in range(0, 2 + 1, 1):
    prodotto = lista1[i] * lista2[i]
    print(prodotto)
