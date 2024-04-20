numeri = [0] * (3)

print("Inserisci 3 numeri di cui desideri sapere il quadrato (un numero a messaggio)")
for i in range(0, 2 + 1, 1):
    numeri[i] = float(input())
print("I quadrati dei numeri inseriti sono: ")
for i in range(0, 2 + 1, 1):
    quadrato = numeri[i] ** 2
    print(quadrato)