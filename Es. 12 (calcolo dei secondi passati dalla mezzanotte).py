print("Inserisci il valore dell'ora")
ora = float(input())
print("Inserisci il valore dei minuti")
minuti = float(input())
print("Inserisci il valore dei secondi")
secondi = float(input())
secondipassatidallamezzanotte = ora * 3600 + minuti * 60 + secondi
print("Il valore dei secondi passati dalla mezzanotte è:")
print(secondipassatidallamezzanotte)