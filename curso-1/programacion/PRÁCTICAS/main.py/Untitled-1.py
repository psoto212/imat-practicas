opcion_numero = 0
historial_operaciones = dict()

while opcion_numero != 9:

    print("******** Calculadora iMAT ********")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print(" ")
    print("5. Valor absoluto")
    print("6. Redondeo de un número al alza")
    print("7. Valor ASCII de un carácter")
    print("8. Carácter de un código ASCII")
    print("")
    print("9. Salir")
    print("10. Historial de operaciones")
    print("11. Repetir operación")
    print("**********************************")

    opcion = input("Operación: ")
    opcion_numero = int(opcion)  

    if opcion_numero > 0 and opcion_numero < 5:  # +, -, *, %...   
        """
        Iteración II: el tipo de dato coincida con lo introducido
        """
        tipo_dato = input("Tipo de dato: ")
        while tipo_dato != "int" and tipo_dato != "float" and tipo_dato != "complex":
            print("Tipo de dato no válido")
            tipo_dato = input("Tipo de dato: ")

        """
        Iteración III: el tipo de dato coincida con lo introducido
        """
        error_entrada_tipo = True
        while error_entrada_tipo == True:
            numero1_str = input("Número #1: ")
            numero2_str = input("Número #2: ")

            if tipo_dato == "int":
                if numero1_str.isdecimal() and numero2_str.isdecimal():
                    numero1 = int(numero1_str)
                    numero2 = int(numero2_str) 
                    error_entrada_tipo = False
                else:
                    error_entrada_tipo = True
            elif tipo_dato == "float":
                if numero1_str.count(".") == 1 and numero2_str.count(".") == 1:
                    numero1 = float(numero1_str)
                    numero2 = float(numero2_str)
                    error_entrada_tipo = False
                else:
                    error_entrada_tipo = True
            elif tipo_dato == "complex": 
                if numero1_str.count("+") == 1 and numero1_str.count("j") == 1 \
                        and numero2_str.count("+") == 1 and numero2_str.count("j") == 1:
                    numero1 = complex(numero1_str)
                    numero2 = complex(numero2_str)
                    error_entrada_tipo = False
                else:
                    error_entrada_tipo = True 

            if error_entrada_tipo:
                print(f"Error: los números introducidos no son {tipo_dato}")

        if opcion_numero == 1:  #sumar
            resultado = numero1 + numero2
            caracter_operacion = "+"
        elif opcion_numero == 2:  #restar
            resultado = numero1 - numero2
            caracter_operacion = "-"  
        elif opcion_numero == 3:  #multiplicar
            resultado = numero1 * numero2
            caracter_operacion = "*"
        elif opcion_numero == 4:  #dividir
            resultado = numero1 / numero2
            caracter_operacion = "/"

        print("---------------------------------------------")
        salida = f"{numero1} {caracter_operacion} {numero2} = {resultado}"
        print(salida)  
        clave = len(historial_operaciones) + 1
        historial_operaciones[clave] = (numero1, caracter_operacion, numero2, resultado)
        print("---------------------------------------------")
    elif opcion_numero == 5:  # abs
        numero1_str = input("Número #1: ") 
        numero1 = int(numero1_str)
        resultado = abs(numero1)
        print("---------------------------------------------")
        salida = f"El valor absoluto de {numero1} es {resultado}"
        print(salida)
        clave = len(historial_operaciones) + 1
        historial_operaciones[clave] = (numero1, "abs", resultado)
        print("---------------------------------------------")
    elif opcion_numero == 6:  # Rendondeo de un float
        numero1_str = input("Número decimal: ") 
        numero1 = float(numero1_str)
        resultado = round(numero1)
        print("---------------------------------------------")
        salida = f"El valor redondeado de {numero1} es {resultado}"
        print(salida)
        clave = len(historial_operaciones) + 1
        historial_operaciones[clave] = (numero1, "round", resultado)
        print("---------------------------------------------")
    elif opcion_numero == 7:  # char to ascii
        char = input("Carácter: ") 
        resultado = ord(char)
        print("---------------------------------------------")
        salida = f"El valor ASCII de {char} es {resultado}"
        print(salida)
        clave = len(historial_operaciones) + 1
        historial_operaciones[clave] = (char, "ord", resultado)        
        print("---------------------------------------------")
    elif opcion_numero == 8:  # ascii to char
        numero1_str = input("Valor ASCII: ") 
        numero1 = int(numero1_str)
        resultado = chr(numero1)
        print("---------------------------------------------")
        salida = f"El carácter de valor ASCII {numero1_str} es {resultado}"
        print(salida)
        clave = len(historial_operaciones) + 1
        historial_operaciones[clave] = (numero1_str, "chr", resultado) 
        print("---------------------------------------------")
    elif opcion_numero == 9:  # Bye
        print("Bye!")
    elif opcion_numero == 10:  # Historial
        print(f"{'Historial':^20}")
        print("=" * 20)
        for clave, operacion in historial_operaciones.items():
            print(f"· {clave}: INPUT: {operacion[:-1]} -> OUTPUT: {operacion[-1:][0]}")
    elif opcion_numero == 11:  # Repetir
        clave_str = input("Clave de la operación: ")
        clave = int(clave_str)
        operacion = historial_operaciones[clave]
        salida = ""
        for i in range(0, len(operacion)):
            if i == len(operacion)-1:
                salida += " ="
            salida += " " + str(operacion[i])

