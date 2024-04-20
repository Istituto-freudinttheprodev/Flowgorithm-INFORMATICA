print("Scegli peso o lunghezza")
risposta = input()
if risposta == "lunghezza":
    print("Scegli se trasformare piedi o metri")
    unita = input()
    if unita == "metri":
        print("Dammi un numero di metri da trasformare in piedi")
        numero = float(input())
        conversione = numero * 3.28084
        print(conversione)
    else:
        print("Dammi un numero di piedi da trasformare in metri")
        numero = float(input())
        conversione = numero / 3.28084
        print(conversione)
else:
    if risposta == "peso":
        print("Scegli se trasformare chili o libbre")
        unita = input()
        if unita == "chili":
            print("Dammi un numero di chili da trasformare in libbre")
            numero = float(input())
            conversione = numero * 2.20462
            print(conversione)
        else:
            print("Dammi un numero di libbre da trasformare in chili")
            numero = float(input())
            conversione = numero / 2.20462
            print(conversione)
    else:
        print("Scelta non valida, puoi scegliere solo tra peso o lunghezza")