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

    if opcion == 1:
        addition(a, b)
    elif opcion == 2:
        subtraction(a, b)
    elif opcion == 3:
        multiplication(a, b)
    else:
        divison(a, b)


if __name__ == '__main__':
    run()
