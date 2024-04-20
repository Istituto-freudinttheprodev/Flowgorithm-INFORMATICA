print("Inserisci 2 elementi (numeri) di cui si scambiaranno reciprocamente il loro valore (un numero a messaggio)")
a = float(input())
b = float(input())
if a > b:
    variabilediscambio = a
    a = b
    b = variabilediscambio
else:
    variabilediscambio = b
    b = a
    a = variabilediscambio
print("I valori dei 2 numeri inseriti scambiati reciprocamente sono:")
print(a)
print(b)