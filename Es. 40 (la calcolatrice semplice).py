print("Che operazione vuoi fare? (differenza/addizione): ")
operazione = input()
print("Inserisci il primo numero: ")
num1 = float(input())
print("Inserisci il secondo numero: ")
num2 = float(input())
if operazione == "differenza":
    op = num1 - num2
    print("Il risultato è: ")
    print(op)
else:
    if operazione == "addizione":
        op = num1 + num2
        print("Il risultato è: ")
        print(op)
    else:
        print("Scelta non valida. Puoi scegliere solo tra la differenza o l'addizione. Riprova riavviando il programma da capo")