print("Inserisci il valore di a")
a = float(input())
print("Inserisci il valore di b")
b = float(input())
print("I dati inseriti sono corretti? (rispondere solo con si o no)")
risposta = input()
if risposta == "si":
    if a == 0 and b == 0:
        print("L'equazione è indeterminata, infatti: 0x = 0")
    else:
        if a == 0:
            print("L'equazione è impossibile, infatti: 0x = b")
        else:
            print("Passaggi per risolvere l'equazione: ")
            print("1) Per prima cosa sottrai b da entrambi i lati dell'equazione")
            print("2) Poi bisogna fare ax + b - b = 0 - b")
            x = -b / a
            print("4) Adesso bisogna dividere entrambi i lati per a")
            print("5) Poi bisogna fare x = -b/a")
            print("6) Adesso bisogna calcolare il valore di x")
            print("7) Quindi alla fine il risultato è:")
            print(x)
else:
    if risposta == "no":
        print("Riavviare il programma da capo per poter inserire nuovamente i dati, procedura di arresto in corso...")
        print("Grazie per avere usato questo programma!")
    else:
        print("Risposta non riconosciuta, riavviare il programma da capo per poter inserire nuovamente i dati, procedura di arresto in corso...")
        print("Grazie per avere usato questo programma!")
print("Si desidera risolvere un'altra equazione? (rispondere solo con si o no)")
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