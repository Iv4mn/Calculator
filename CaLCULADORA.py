Operación = input("Elige una opción 1. Sumar 2. Restar 3. Multiplicar 4. Dividir: ")

#Here are the different options and code request you the value for the numbers that you want to calculate
if Operación == ("1"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))

    print(Valor1 + Valor2)
elif Operación == ("2"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))

    print(Valor1 - Valor2)
elif Operación == ("3"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))

    print(Valor1 * Valor2)
elif Operación == ("4"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))

    print(Valor1 / Valor2)
    
#And here the code tells you that you need to choose the correct option if you hadn't chosen it correctly.

else:
    print("Elige una de las opciones anteriormente mencionadas.")
