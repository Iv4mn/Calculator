Operación = input("Elige una opción 1. Sumar 2. Restar 3. Multiplicar 4. Dividir: ")

Valor1 = int(input("Escribe tu primer valor: "))
Valor2 = int(input("Escribe tu segundo valor: "))

if Operación == ("1"):
    print(Valor1 + Valor2)
    
elif Operacion == ("2"):
    print(Valor1 - Valor2)
    
elif Operacion == ("3"):
    print(Valor1 * Valor2)
    
elif Operacion == ("4"):
    print(Valor1 / Valor2)
    
else:
    print("Tienes que elegir una de las opciones anteriormente mencionadas")
    
    
