print("Inserisci il primo numero: ")
num1 = float(input())
print("Inserisci il secondo numero: ")
num2 = float(input())
print("Scegli una delle due opzioni per l'azione che si desidera fare: somma o differenza")
scelta = input()
if scelta == "somma":
    print("Il risultato della operazione è:")
    risultato = num1 + num2
    print(risultato)
else:
    if scelta == "differenza":
        print("Il risultato della operazione è:")
        risultato = num1 - num2
        print(risultato)
    else:
        print("Scelta invalida. Riprova riavviando il programma da capo. Puoi scegliere soltanto tra somma e differenza")
