
from math import ceil

area_pintura = float(input("Informe o tamanho em metros quadrados da área a ser pintada: "))

qtd_tinta = area_pintura / 3

qtd_latas = qtd_tinta / 18

vlr_lata = 80
custo = qtd_latas * vlr_lata


print("Serão necessárias",ceil(qtd_latas),f'latas de tinta para pintar esta área e custará R$ {custo:.2f}')