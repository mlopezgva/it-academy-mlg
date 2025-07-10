import sys

debug = False

def hasCliParam(item, args, remove=True):
    '''
    Comprueba si existe un elemento concreto (normalmente un 'flag') entre los
    argumentos de la línea de comandos.Devuelve True o False.

    item   Elemento a buscar
    args   Lista de elementos donde buscar (normalmente `sys.argv`)
    remove Si es `True` elimina el elemento encontrado de la lista
    '''

    response = False

    if item in args:
        response = True
        if remove:
            args.pop(args.index(item))

    return response

def askNumValue(string):
    '''
    Pide al usuario un valor numérico.
    Comprueba que lo sea antes de devolverlo, y muestra un error
    si no lo es, antes de finalizar el script.
    '''

    try:
        iVal = input(string)
        return float(iVal)
    except ValueError:
        exit(f"'{iVal}' no se puede interpretar como un número!")
    except:
        exit("Error inesperado")

def IMC(peso, altura):
    '''
    Calcula el índice de masa corporal (IMC)
    con base al peso en kg y la altura en metros
    Si la altura no es un float y supera los 50
    asume que son cm y realiza la conversión.
    '''

    if altura > 50:
        altura /= 100

    try:
        if debug:
            print("\nPeso:  ", peso, "kg\nAltura:", altura, 'm')

        imc = peso / (altura ** 2)
        if debug:
            print(
                f"\n      {peso:6.2f}",
                f"IMC = —————— = {imc:.2f}",
                f"      {altura: 6.2f}²\n",
                # f"IMC = {imc:.2f}\n",
                sep="\n")

    except ValueError:
        exit("El valor del peso o la altura son inválidos.")

    except TypeError:
        exit("El valor del peso o la altura no son del tipo esperado (float|int)")

    else:
        return imc

def informeImc(imc: float):
    info  = f"En base al peso y altura indicados, su IMC es de {imc:03.2f}.\n"
    clase = "Este índice le sitúa en el rango de "
    imccl = clasificaIMC(imc)
    imcclass = [
        "bajo peso",
        "peso normal",
        "sobrepeso",
        "Obesidad"
    ]
    # print(f"Su IMC: {imc:.2f}")
    return info + clase + imcclass[imccl]

def clasificaIMC(imc):

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

args       = sys.argv
scriptName = args.pop(0)
debug      = hasCliParam('-v', args) or hasCliParam('--verbose', args)
showHelp   = hasCliParam('-h', args) or hasCliParam('--help',    args)
argc       = len(args)
# Llegados aquí, args tiene solo los argumentos que se le puedan haber pasado
# y argc el número de argumentos "real" (descontando el nombre del script) o
# los parámetros (-d, --debug, -h o --help)

def main():
    if showHelp:
        print (f"""
            Uso:
                {scriptName}
                {scriptName}
                {scriptName} -h           muestra esta ayuda
                {scriptName} --help       muestra esta ayuda
                {scriptName} -v           muestra detalles del cálculo del IMC
                {scriptName} --verbose    muestra detalles del cálculo del IMC
                {scriptName} <peso en kg>
                {scriptName} <peso en kg> <altura en m>

            Ambos parámetros son opcionales. Si solo se informa del primer
            valor este será el peso, y se le preguntará por la altura.  Si no
            se indica ningún valor, se le preguntará por ambos.

            Para mostrar esta ayuda, use -h o --help
            """)
        exit()

    peso   = float(args[0]) if argc > 0 else askNumValue("Peso: ")
    altura = float(args[1]) if argc > 1 else askNumValue("Altura: ")

    imc = IMC(peso, altura)
    print("\n"+informeImc(imc))

if __name__ == "__main__":
    main()
