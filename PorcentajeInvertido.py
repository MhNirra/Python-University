text = "Bienvenido al banco!"
print("====================")
print(text)
print("====================")
print("")

get = int(input("Ingrese la capital a invertir: "))
aumento = 2
algot = get * (aumento / 100)
valorAum = algot + get
valorSeis = valorAum * 6
print("La cantidad que va a invertir es de:", + get, "pesos")
print("============================================")
print("")
print("Lo que aumentarĂ¡ mes a mes su ganancia es de:", algot, "pesos y quedarĂ¡ con:", valorAum, "pesos")
print("")
print("La ganancia total que tendrĂ¡ es 6 meses incluyendo la capital invertida es de:", valorSeis, "pesos")
