def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2

oper = ""
while(oper != "salir"):
    oper = input("Indique la operación matemática (suma - resta) o salir: ")
    if oper in globals():
        if callable(globals()[oper]):
            valor1 = eval(input("Dime el primer numero: "))
            valor2 = eval(input("Dime el segundo numero: "))
            resultado = (globals()[oper](valor1, valor2))
            print(("La " + oper + " es " + str(resultado)))
    else:
        if oper != "salir":
            print(("La operación " + oper + " no existe"))
print("Gracias por usar la calculadora.")
