print("Inserisci il valore di a")
a = float(input())
print("Inserisci il valore di b")
b = float(input())
print("I dati inseriti sono corretti? (rispondere solo con si o no)")
risposta = input()
if risposta == "si":
    if a == 0 and b == 0:
        print("L'equazione lineare è indeterminata, infatti: 0x = 0")
    else:
        if a == 0:
            print("L'equazione lineare è impossibile, infatti: 0x = b")
        else:
            print("Passaggi per risolvere l'equazione lineare: ")
            print("1) Dividi entrambi i lati per a, quindi l'equazione lineare diventa:")
            print("ax + b = 0 diventa x = -b/a")
            print("2) La soluzione della equazione lineare quindi è:")
            x = -b / a
            print(x)
else:
    if risposta == "no":
        print("Riavviare il programma da capo per poter inserire nuovamente i dati, procedura di arresto in corso...")
        print("Grazie per avere usato questo programma!")
    else:
        print("Risposta non riconosciuta, riavviare il programma da capo per poter inserire nuovamente i dati, procedura di arresto in corso...")
        print("Grazie per avere usato questo programma!")
print("Si desidera risolvere un'altra equazione lineare? (rispondere solo con si o no)")
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