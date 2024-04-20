print("Inserisci il valore di a")
a = float(input())
print("Inserisci il valore di b")
b = float(input())
print("I dati inseriti sono corretti? (rispondere solo con si o no)")
risposta = input()
if risposta == "si":
    if a == 0:
        print("La disequazione non è di primo grado")
    else:
        print("Passaggi per risolvere la disequazione: ")
        print("1) Dividi entrambi i lati per a, ricordando di invertire il segno della disequazione, quindi la disequazione diventa:")
        print("ax + b>0 diventa x>x")
        print("2) La soluzione della disequazione quindi è:")
        x = -b / a
        print(x)
else:
    if risposta == "no":
        print("Riavviare il programma da capo per poter inserire nuovamente i dati, procedura di arresto in corso...")
        print("Grazie per avere usato questo programma!")
    else:
        print("Risposta non riconosciuta, riavviare il programma da capo per poter inserire nuovamente i dati, procedura di arresto in corso...")
        print("Grazie per avere usato questo programma!")
print("Si desidera risolvere un'altra disequazione? (rispondere solo con si o no)")
scelta = input()
if scelta == "si":
    print("Riavviare il programma da capo per poter inserire nuovamente i dati, procedura di arresto in corso...")
    print("Grazie per avere usato questo programma!")
else:
    if scelta == "no":
        print("Grazie per avere usato questo programma! Il programma si chiuderà automaticamente")
    else:
        print("Risposta non riconosciuta, riavviare il programma da capo per poter inserire nuovamente i dati, procedura di arresto in corso...")
        print("Grazie per avere usato questo programma!")