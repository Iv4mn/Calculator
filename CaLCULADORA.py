Operación = input("Elige una opción 1. Sumar 2. Restar 3. Multiplicar 4. Dividir: ")

if Operación == ("1"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))

    print(Valor1 + Valor2)
if Operación == ("2"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))

    print(Valor1 - Valor2)
if Operación == ("3"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))

    print(Valor1 * Valor2)
if Operación == ("4"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))

    print(Valor1 / Valor2)
else:
    print("Elige una de las opciones anteriormente mencionadas.")



