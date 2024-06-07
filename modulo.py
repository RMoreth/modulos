from datetime import date

# função menu


def exibir_menu():
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f"data de hoje {dia}\{mes}\{ano}")
    print('1 - calcular quadrilatero')
    print('2 - calcular circulo')
    print('3 - calcular triangulo')
    print('4 - calcular trapezio')
    print('5 - sair do programa')


# Função do quadrilatero

def calcular_quadrilateros(b, h):
    a = b * h
    return a
# função da circunferencia


def calcular_circulo(r):
    a = 3.14 * r**2
    return a

# função do triangulo


def calcular_triangulo(b, h):
    a = b * h / 2
    return a

# função do trapézio


def calcular_trapezio(b_menor, b_maior, h):
    a = ((b_menor + b_maior) * h / 2)
    return a
