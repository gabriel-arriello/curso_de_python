

from math import ceil

area_pintura = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))

qtd_tinta = area_pintura / 6

vlr_lata = 80
vlr_galao = 25

#ORÇAMENTO LATAS E GALÕES SEPARADOS
qtd_latas = qtd_tinta / 18
qtd_galoes = qtd_tinta / 3.6

custo_latas = ceil(qtd_latas) * vlr_lata
custo_galoes = ceil(qtd_galoes) * vlr_galao

#ORÇAMENTO MISTURANDO LATAS E GALÕES PARA MENOR DESPERDÍCIO E ACRESCENTANDO 10% DE FOLGA
qtd_tinta_folga = qtd_tinta + qtd_tinta*0.1
mistura_latas = (qtd_tinta_folga) // 18
mistura_galoes = (qtd_tinta_folga % 18) / 3.6

custo_lat_mistura = ceil(mistura_latas) * vlr_lata
custo_gal_mistura = ceil(mistura_galoes) * vlr_galao
custo_latgal_mistura = custo_lat_mistura + custo_gal_mistura

print("Para pintar a área de",area_pintura,f"m2 será necessário {qtd_tinta:.2f}","litros de tinta.\r\n"
"Você pode optar por latas, galões ou ambos:\r\n"
"-",ceil(qtd_latas),"latas de tinta de 18L\r\n"
"Custo: R$",float(round(custo_latas,2)),"\r\n"
"-",ceil(qtd_galoes),"galões de tinta de 3,6L\r\n"
"Custo: R$",float(round(custo_galoes,2)),"\r\n"
"-",ceil(mistura_latas),"latas de 18L e",ceil(mistura_galoes),"galões de 3,6L (acrescentando 10% de folga:",round(qtd_tinta_folga,2),"L)\r\n"
"Custo: R$",float(round(custo_latgal_mistura,2)))
