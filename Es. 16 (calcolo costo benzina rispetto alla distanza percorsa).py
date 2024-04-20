print("Inserisci il valore del costo della benzina al litro")
costobenzinaallitro = float(input())
print("Inserisci il valore del consumo al litro")
distanzaallitro = float(input())
print("Inserisci il valore della distanza percorsa")
distanza = float(input())
consumo = distanza / distanzaallitro
costototale = costobenzinaallitro * consumo
print("Il valore del costo del consumo in litri per coprire la distanza percorsa è:")
print(costototale)