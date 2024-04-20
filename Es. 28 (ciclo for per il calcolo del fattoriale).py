print("Inserisci il numero di cui desideri sapere il fattoriale")
n = int(input())
print("Il fattoriale del numero inserito è (leggere solo l'ultimo risultato):")
fattoriale = 1
i = 1
for i in range(1, n + 1, 1):
    fattoriale = fattoriale * i
    print(fattoriale)