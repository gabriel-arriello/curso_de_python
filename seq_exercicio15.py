


qtd_horas = float(input("Quantas horas você trabalhou este mês? "))

vlr_horas = float(input("Quanto você ganha por hora? "))

salario_bruto = qtd_horas * vlr_horas

imposto_renda = 0.11 * salario_bruto
imposto_inss = 0.08 * salario_bruto
imposto_sindicato = 0.05 * salario_bruto
impostos = imposto_renda + imposto_inss + imposto_sindicato

salario_liquido = salario_bruto - impostos

print("Salário bruto: R$",round(salario_bruto,2),"\r\n"
"Desconto IR: R$",round(imposto_renda,2),"\r\n"
"Desconto INSS: R$",round(imposto_inss,2),"\r\n"
"Desconto Sindicato R$",round(imposto_sindicato,2),"\r\n"
"Salário líquido: R$",round(salario_liquido,2))