print("Inserisci il valore numerico dei soldi in dollari")
dollari = float(input())
print("Inserisci il valore numerico dei soldi in sterline")
sterline = float(input())
dollariconversione = 0.85
sterlineconversione = 1.15
euroindollari = dollari * dollariconversione
euroinsterline = sterline * sterlineconversione
eurototali = euroindollari + euroinsterline
print("Il valore dei soldi in dollari in euro è:")
print(euroindollari)
print("Il valore dei soldi in sterline in euro è:")
print(euroinsterline)
print("Il valore della somma dei soldi di entrambe le valute in euro è:")
print(eurototali)