print("Inserisci il valore del prezzo lordo")
prezzolordo = float(input())
print("Inserisci il valore della percentuale dell'IVA")
percentualeiva = float(input())
prezzonetto = prezzolordo / (1 + percentualeiva / 100)

# Questo perchè la formula è:
# LORDO = NETTO + IVA% NETTO
# LORDO = NETTO (1+IVA che è 0,19)
# NETTO = LORDO/1+IVA
print("Il valore del prezzo netto è:")
print(prezzonetto)