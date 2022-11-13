from statistics import mean

nota1 = int(input("Primeira nota:"))
nota2 = int(input("Segunda nota:"))
nota3 = int(input("Terceira nota:"))
nota4 = int(input("Quarta nota:"))

nota_total = (nota1,nota2,nota3,nota4)

print("Sua média bimestral foi:",(mean(nota_total)))
