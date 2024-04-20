import random
random.seed()   #Prepare random number generator

numeroscritto = 0

# Il + 1 serve perchè qualsiasi linguaggio di programmazione parte da 0 e allora cambierebbe il range perchè non sarebbe più da 1 a 100, ma da 0 a 100
numerocasuale = int(random.random() * 100) + 1

# Questa condizione serve perchè se il numero casuale è pari a 100 verrebbe ridotto di 1 e quindi non sarebbe 101, ma rimarebbe 100
if numerocasuale == 101:
    numerocasuale = numerocasuale - 1
print("Prova ad indovinare un numero da 1 a 100, che la fortuna sia con te, inseriscilo qui sotto")
while numeroscritto != numerocasuale:
    numeroscritto = int(input())
    if numeroscritto == numerocasuale:
        print("Hai inserito il numero corretto, complimenti!")
    else:
        if numeroscritto > numerocasuale:
            print("Hai inserito un numero troppo alto, riprova inserendone uno più basso")
        else:
            print("Hai inserito un numero troppo basso, riprova inserendone uno più alto")
print("Sei riuscito a indovinare il numero perciò sei il vincitore di questo gioco, complimenti davvero!")
print("Grazie per aver giocato")
