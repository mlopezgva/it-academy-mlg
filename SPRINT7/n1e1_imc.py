import sys

def askNumValue(string):
    try:
        iVal = input(string)
        return float(iVal)
    except ValueError:
        exit(f"'{iVal}' no se puede interpretar como un número!")
    except:
        exit("Error inesperado")

def imc(peso, altura):
    '''
    Calcula el índice de masa corporal (IMC)
    con base al peso en kg y la altura en metros
    Si la altura no es un float y supera los 50
    asume que son cm y realiza la conversión.
    '''

    if altura > 50:
        altura /= 100
    
    try:
        imc = peso / (altura ** 2)
    
    except ValueError:
        exit("El valor del peso o la altura son inválidos.")

    except TypeError:
        exit("El valor del peso o la altura no son del tipo esperado (float|int)")

    else:
        return imc

def informeImc(imc):
    info  = f"Basándose en el peso y altura indicados, su IMC es de {imc}.\n"
    clase = "Este índice le sitúa en el rango de "
    imccl = clasificaIMC(imc)
    imcclass = [
        "bajo peso",
        "peso normal",
        "sobrepeso",
        "Obesidad"
    ]
    return info + clase + imcclass[imccl]

def clasificaIMC(imc):
    print(type(imc))

    try:
        match imc:
            case x if x < 18.5:
                return 0
            case x if x < 24.9:
                return 1
            case x if x < 29.9:
                return 2
            case _:
                return 3
        print("It's OK")
    except ValueError:
        exit("El valor del peso o la altura son inválidos.")

    except TypeError:
        exit("El valor del peso o la altura no son del tipo esperado (float|int)")

args = sys.argv
scriptName = args.pop(0)
argc = len(args)
# Llegados aquí, args tiene solo los argumentos que se le puedan haber pasado
# y argc el número de argumentos "real" (descontando el nombre del script)

print (argc)

if argc == 1 and sys.argv[0] in ["-h", "--help"]:
    print (f"""
        Uso:
            {sys.argv[0]}
            {sys.argv[0]} -h
            {sys.argv[0]} --help
            {sys.argv[0]} <peso en kg>
            {sys.argv[0]} <peso en kg> <altura en m>

        Ambos argumentos son opcionales. Si solo se informa del primer valor
        este será el peso, y se le preguntará por la altura.
        Si no se indica ningún valor, se le preguntará por ambos.

        Para mostrar esta ayuda, use -h o --help
        """)
    exit()

peso   = args[0] if argc > 0 else askNumValue("Peso: ")
altura = args[1] if argc > 1 else askNumValue("Altura: ")

print("Peso:", peso, "\nAltura", altura)
imc = imc(peso, altura)
informeImc(imc)