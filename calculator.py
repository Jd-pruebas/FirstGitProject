def addition(num1, num2):
    print(f'El resultado es: {num1} + {num2} = {num1 + num2}\n')


def subtraction(num1, num2):
    print(f'El resultado es: {num1} - {num2} = {num1 - num2}\n')


def multiplication(num1, num2):
    print(f'El resultado es: {num1} x {num2} = {num1 * num2}\n')


def division(num1, num2):
    if num2 == 0:
        print("No es posible dividir entre '0'\n")
    else:
        print(f'El resultado es: {num1} ÷ {num2} = {num1 / num2}\n')


def run():
    print("\n¡Bienvenido! Este es un demo de calculadora\nA continuación ingresa dos números para hacer operaciones básicas\n")
    a = int(input("Digita el primer número: "))
    b = int(input("Digita el segundo número: "))
    opcion = 0
    menu = """
    
    Opciones:

1 - Suma            (número 1 + número 2)
2 - Resta           (número 1 - número 2)
3 - Multiplicación  (número 1 x número 2)
4 - División        (número 1 ÷ número 2)

Elige una opcion: """

    while opcion < 1 or opcion > 4:
        opcion = int(input(menu))
        if opcion < 1 or opcion > 4:
            menu = "¡Elegiste una opción incorrecta! Selecciona de nuevo: "

    if opcion == 1:
        addition(a, b)
    elif opcion == 2:
        subtraction(a, b)
    elif opcion == 3:
        multiplication(a, b)
    else:
        division(a, b)


if __name__ == '__main__':
    run()
