

numeros = [float(input("Número: ")) for i in range(3)]

contas = [((2*numeros[0]) * (numeros[1]/2)), (3*numeros[0] + numeros[2]), (numeros[2]**3)]


print(
"O produto do dobro do primeiro com metade do segundo:", contas[0], "\r\n" 
"A soma do triplo do primeiro com o terceiro:", contas[1], "\r\n" 
"O terceiro elevado ao cubo:", contas[2])
