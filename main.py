# importa o modulo
import os
from modulo import *

if __name__ == '__main__':
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')

        match opcao:
            case '1':
                os.system('cls')
                b = int(input("base do quadrilatero: "))
                h = int(input("altura do quadrilatero: "))

                print(f"Área: {calcular_quadrilateros(b, h)}")
                continue
            case '2':
                os.system('cls')
                r = int(input("raio do circulo: "))
                print(f"Área: {calcular_circulo(r)}")
                continue

            case '3':
                os.system('cls')
                b = int(input("base do triangulo: "))
                h = int(input("altura do triangulo: "))
                print(f"Área: {calcular_triangulo(b, h)}")
                continue

            case '4':
                os.system('cls')
                b_menor = int(input("base menor do trapezio: "))
                b_maior = int(input("base maior do trapezio: " ))
                h = int(input("altura do trapezio"))
                print(f"Área: {calcular_trapezio(b_menor, b_maior, h)}")
                continue

            case '5':
                os.system('cls')
                print("ENCERRANDO O PROGRAMA")
                break

            case _:
                os.system('cls')
                print("opção inválida")
                continue
