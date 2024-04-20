numerotrovato = False
divisore = 2
print("Inserisci il numero primo N da cui si desidera sapere il quadrato")
numero = float(input())
while divisore < numero:
    if numero % divisore == 0:
        numerotrovato = True
    divisore = divisore + 1
if numerotrovato == False:
    print("Il numero scritto è primo")
    print("Il quadrato di questo numero primo è:")
    for i in range(0, 0 + 1, 1):
        quadrato = numero ** 2
        print(quadrato)
else:
    print("Il numero scritto non è primo")
    print("Riavvia il programma e inserisci un numero primo per sapere il suo quadrato")