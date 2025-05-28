#Esta validación es para solicitar solo numeros.
try:
    import sys
    import math

    validar = 0

    #Este bloque es para determinar si se ingresa un argumento al ejecutar el programa, o pedir datos si no se ingresó argumento.
    if len(sys.argv) == 1:
        sol = float(input("Ingrese el valor de 1 peso chileno, en soles peruanos:  "))
        arg = float(input("Ingrese el valor de 1 peso chileno, en pesos argentinos:  "))
        dol = float(input("Ingrese el valor de 1 peso chileno, en dólares americanos:  "))
        peso_cl = int(input("Ingrese el monto en pesos chilenos que desea tasar: $"))
        validar = 1

    elif len(sys.argv) == 5 :
        sol = float(sys.argv[1])
        arg = float(sys.argv[2])
        dol = float(sys.argv[3])
        peso_cl = int(sys.argv[4])
        validar = 1
    #Si no se ingresan la  cantidad de argumentos necesarios, no se "valida" la operación
    else :
        validar = 0
    
    #Cálculo de conversión
    sol_conv = sol * peso_cl
    arg_conv = arg * peso_cl
    dol_conv = dol * peso_cl
    
    #Evaluación del IMC
    if validar == 0 :
        print("Error en el ingreso de datos. \nPuedes ingresar <python conversiones.py> para inicar, o \n <python conversoines.py [valor de $1 CLP en soles peruanos] [valor de $1 CLP en pesos argentinos] [valor de $1 CLP en dólares americanos] [cantidad de pesos chilenos (CLP) a tasar]")
    else :
        print(f"Los {peso_cl} pesos equivalen a: \n {sol_conv:.1f} soles peruanos. \n {arg_conv:.1f} pesos argentinos. \n {dol_conv:.1f} dólares americanos.")

except ValueError:
    print("Has ingresado datos que no son numéricos. \nPuedes ingresar <python conversiones.py> para inicar, o \n <python conversoines.py [valor de $1 CLP en soles peruanos] [valor de $1 CLP en pesos argentinos] [valor de $1 CLP en dólares americanos] [cantidad de pesos chilenos (CLP) a tasar]")