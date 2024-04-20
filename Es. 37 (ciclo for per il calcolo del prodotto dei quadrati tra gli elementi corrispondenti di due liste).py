lista1 = [0] * (3)
lista2 = [0] * (3)
quadrati1 = [0] * (3)
quadrati2 = [0] * (3)

print("Inserisci 3 elementi (numeri) per la lista n°1 (un numero a messaggio)")
for i in range(0, 2 + 1, 1):
    lista1[i] = int(input())
print("Inserisci 3 elementi (numeri) per la lista n°2 (un numero a messaggio)")
for i in range(0, 2 + 1, 1):
    lista2[i] = int(input())
print("Il calcolo dei quadrati tra gli elementi corrispondenti delle liste è:")
for i in range(0, 2 + 1, 1):
    quadrati1[i] = lista1[i] ** 2
    print(quadrati1[i])
    quadrati2[i] = lista2[i] ** 2
    print(quadrati2[i])
print("Il calcolo del prodotto dei quadrati tra gli elementi corrispondenti delle liste è:")
for i in range(0, 2 + 1, 1):
    prodotto = quadrati1[i] * quadrati2[i]
    print(prodotto)