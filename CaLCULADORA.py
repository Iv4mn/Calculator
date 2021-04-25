# Here the code request you to choose an option
Operación = input("Elige una opción 1. Sumar 2. Restar 3. Multiplicar 4. Dividir 5. Potenciación: ")

# Here are the different options and code request you the value for the numbers that you want to calculate

# --ADD--
if Operación == ("1"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))
    int= Valor1 + Valor2
    print("Tu resultado es",int)

# --ABSTRACT--
elif Operación == ("2"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))
    int= Valor1 - Valor2
    print("Tu resultado es",int)

# --MULTIPLICATE--
elif Operación == ("3"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))
    int = Valor1 * Valor2
    print("Tu resultado es",int)

# --DIVIDE--
elif Operación == ("4"):
    Valor1 = int(input("Escribe tu primer valor: "))
    Valor2 = int(input("Escribe tu segundo valor: "))
    int = Valor1 / Valor2
    print("Tu resultado es",int)

# --POTENTIATION--
elif Operación == ("5"):
    Valor1= int(input("Escribe tu primer valor: "))
    Valor2= int(input("Escribe la potenciación: "))
    int = Valor1 ** Valor2
    print("Tu resultado es",int)

# And here the code tells you that you need to choose the correct option if you hadn't chosen it correctly.

else:
    print("Elige una de las opciones anteriormente mencionadas.")
