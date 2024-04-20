numeri = [0] * (5)

numeri[0] = 0
numeri[1] = 0
numeri[2] = 0
numeri[3] = 0
numeri[4] = 0
fattoriale = 1
print("Inserisci 5 numeri di cui desideri sapere il fattoriale e il quadrato (un numero a messaggio)")
for i in range(0, 4 + 1, 1):
    numeri[i] = float(input())
print("I fattoriali dei numeri inseriti sono:")
for i in range(0, 4 + 1, 1):
    fattoriale = 1
    for k in range(1, numeri[i] + 1, 1):
        fattoriale = fattoriale * k
    print(fattoriale)
print("I quadrati dei numeri inseriti sono: ")
for i in range(0, 4 + 1, 1):
    print(numeri[i] ** 2)