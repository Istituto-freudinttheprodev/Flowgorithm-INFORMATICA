print("dammi numero 1")
num1 = float(input())
print("dammi numero 2")
num2 = float(input())
if num1 == num2 ** 2:
    print("numero 1 è uguale numero 2 alla seconda")
else:
    if num2 == num1 ** 2:
        print("numero 2 è uguale numero 1 alla seconda")
    else:
        print("nessuno dei due è quadrato dell'altro")