a = 0
b = 1
c = 0
risultato = 0
fibonacci = 0
iteratore = 0
print("Inserisci il numero di cui desideri calcolare l'n-esimo numero di Fibonacci")
n = int(input())
if n <= 0:
    print("Impossibile eseguire il calcolo perchè il numero deve essere maggiore di 0. Riavvia il programma per inserire un nuovo numero")
else:
    if n == 1:
        risultato = 0
        print(risultato)
    else:
        for iteratore in range(fibonacci, n - 2 + 1, 1):
            c = a + b
            a = b
            b = c
            risultato = c
            print(risultato)