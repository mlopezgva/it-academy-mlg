import sys
from cli_funcs import has_cli_param, \
    ask_num_value, argc, args, showHelp, scriptName

verbose = False

def IMC(peso, altura):
    '''
    Calcula el índice de masa corporal (IMC)
    con base al peso en kg y la altura en metros
    Si la altura no es un float y supera los 50
    asume que son cm y realiza la conversión.
    '''

    if altura > 50:
        altura /= 100

    if altura > 2.5:
        exit(f"Una altura de {altura}m parece ser excesiva para un humano.")

    try:
        if verbose:
            print(f"\nPeso:  {peso: 6.2f} kg\nAltura: {altura: 6.2f} m")

        imc = peso / (altura ** 2)
        if verbose:
            print(
                f"\n      {peso:6.2f}",
                f"IMC = —————— = {imc:.2f}",
                f"      {altura: 6.2f}²\n",
                # f"IMC = {imc:.2f}\n",
                sep="\n")

    except ValueError:
        exit("El valor del peso o la altura son inválidos.")

    except TypeError:
        exit("El valor no es del tipo esperado (float|int)")

    else:
        return imc

def informeImc(imc: float):
    info     = f"En base al peso y altura indicados, su IMC es de {imc:03.2f}.\n"
    clase    = "Este índice le sitúa en el rango de "
    imccl    = clasificaIMC(imc)
    imcclass = [
        "riesgo de anorexia",
        "bajo peso",
        "peso normal",
        "sobrepeso",
        "Obesidad"
    ]
    # print(imcclass, f"Su IMC: {imc:.2f}")    # debug code
    return info + clase + imcclass[imccl]

def clasificaIMC(imc):
    try:
        match imc:
            case x if x < 17.5:
                return 0
            case x if x < 18.5:
                return 1
            case x if x < 24.9:
                return 2
            case x if x < 29.9:
                return 3
            case _:
                return 4

    except ValueError:
        exit("El valor del peso o la altura son inválidos.")

    except TypeError:
        exit("El valor del peso o la altura no son del tipo esperado (float|int)")

verbose = has_cli_param('-v', args) or has_cli_param('--verbose', args)

def main():
    if showHelp:
        print (f"""
            N1:E1 - Cálculo de IMC
            ----------------------
            
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

    peso   = float(args[0]) if argc() > 0 else ask_num_value("Peso: ")
    altura = float(args[1]) if argc() > 1 else ask_num_value("Altura: ")

    print("\n" + informeImc(IMC(peso, altura)))

if __name__ == "__main__":
    main()
