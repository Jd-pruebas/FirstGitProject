def addition(num1, num2):
    print("La suma es: " + str(num1 + num2))


def subtraction(num1, num2):
    print("La resta es: " + str(num1 - num2))


def multiplication(num1, num2):
    print("La multiplicación es: " + str(num1 * num2))


def divison(num1, num2):
    if num2 == 0:
        print("No es posible dividir entre '0'")
    else:
        print("La división es: " + str(num1 / num2))


def run():
    print("\nEsta es una mini calculadora\nA continuación ingresa dos números para hacer operaciones\n")
    a = int(input("Digita el primer número: "))
    b = int(input("Digita el segundo número: "))
    opcion = 0
    menu = """
    
    Opciones:

1 - suma            (número 1 + número 2)
2 - resta           (número 1 - número 2)
3 - multiplicación  (número 1 x número 2)
4 - división        (número 1 ÷ número 2)

Elige una opcion: """

    while opcion < 1 or opcion > 4:
        opcion = int(input(menu))
        if opcion < 1 or opcion > 4:
            menu = "¡Elegiste una opción incorrecta! Selecciona de nuevo: "


if __name__ == '__main__':
    run()
