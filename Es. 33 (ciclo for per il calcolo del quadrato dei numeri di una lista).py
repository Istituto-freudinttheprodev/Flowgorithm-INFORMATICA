numeri = [0] * (5)

print("Inserisci cinque numeri interi di cui vuoi sapere il quarato (un numero a messaggio)")
for i in range(0, 4 + 1, 1):
    numeri[i] = int(input())
print("I numeri che hai inserito prima al quadrato sono:")
for i in range(0, 4 + 1, 1):
    print(numeri[i] ** 2)