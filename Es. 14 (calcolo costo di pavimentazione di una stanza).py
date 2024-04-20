print("Inserisci il valore del costo unitario, cioè il costo di un singolo metro quadrato di pavimentazione")
costounitario = float(input())
print("Inserisci il valore della larghezza della stanza in metri")
larghezzastanza = float(input())
print("Inserisci il valore della lunghezza della stanza in metri")
lunghezzastanza = float(input())
areastanza = larghezzastanza * lunghezzastanza
print("Il valore dell'area della stanza è:")
print(areastanza)
costototale = costounitario * areastanza
print("Il valore del costo totale della stanza è:")
print(costototale)