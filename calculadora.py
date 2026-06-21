# Función principal para la calculadora
def calculadora():
    print("==== Calculadora ====")
    print("Escriba 'salir' para cerrar\n")
    
    # Mantiene la calculadora funcionando hasta que el usuario decida salir
    while True:
        # Solicita la operación matemática que se desea realizar
        operacion = input("Operación (+, -, *, /): ").strip()

        # Permite cerrar el programa escribiendo "salir"
        if operacion.lower() == "salir":
            print("Cerrando calculadora....")
            break

        # Valida que la operación ingresada sea de las permitidas
        if operacion not in ("+", "-", "*", "/"):
            print("Operación invalida. Usa: +, -, *, /\n")
            continue

        try:
            # Solicita los números y los convierte a tipo float
            numero1 = float(input("Primer número: "))
            numero2 = float(input("Segundo número: "))

        # Captura errores cuando el usuario no ingresa valores numéricos
        except ValueError:
            print("Solo ingrese números válidos.\n")
            continue

        # Evita la división entre cero
        if operacion == "/" and numero2 == 0:
            print("Error: no se puede dividir entre cero.\n")
            continue

        # Diccionario que almacena el resultado de cada operación
        operaciones = {
            "+": numero1 +  numero2,
            "-": numero1 - numero2,
            "*": numero1 * numero2,
            "/": numero1 / numero2,
        }
        
        
        # Obtiene el resultado correspondiente a la operación elegida
        resultado = operaciones[operacion]

        # Muestra enteros sin decimales innecesarios
        if resultado == int(resultado):
            print(f"Resultado: {int(resultado)}\n")
        else:
            print(f"Resultado: {resultado}\n")

# Inicia la calculadora
calculadora()
