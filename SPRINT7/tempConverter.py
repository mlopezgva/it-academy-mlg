#!/usr/bin/python3.10
import sys

# Definir diccionario de escala, nombre y símbolo para interpretar entrada
scale = {
    "Celsius":    {"symbol": "ºC", "code": "celsius",    'longName': 'grados Celsius'},
    "Fahrenheit": {"symbol": "ºF", "code": "fahrenheit", 'longName': 'grados Fahrenheit'},
    "Kelvin":     {"symbol": "K",  "code": "kelvin",     'longName': 'Kelvins'},
    "Rankine":    {"symbol": "R",  "code": "rankine",    'longName': 'Rankines'},
    "Réaumur":    {"symbol": "ºR", "code": "reaumur",    'longName': 'grados Réaumur'}
}
# "Aplana" el diccionario anterior ("comprehension", se llama esto...)
Scales = [
    {"name": name, **attributes} for name, attributes in scale.items()
]

def get_scale_info(attr, value):
    '''
    Returns the desired attr (eg. the name or the symbol) of a scale,
    based on any of the values in the row.

    getScale('symbol', 'Celsius')
    returns `ºC`
    '''
    for scale in Scales:
        if value in scale.values():
            return scale[attr] if attr in scale else None
    return None

def has_cli_param(item, args, remove=True):
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

def ask_num_value(string):
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

def convert_to(
        fromScale: str,
        fromValue: float,
        toScale:   str):

    match fromScale.lower():
        case 'celsius':
            match toScale.lower():
                case 'celsius':
                    return fromValue
                case 'fahrenheit':
                    return fromValue * 1.8 + 32
                case 'kelvin':
                    return fromValue - 273.15
                case 'rankine':
                    return (fromValue + 273.15) * 1.8
                case 'reaumur':
                    return 0.8 * fromValue
        case 'fahrenheit':
            match toScale.lower():
                case 'celsius':
                    return (fromValue - 32) / 1.8
                case 'fahrenheit':
                    return fromValue
                case 'kelvin':
                    return ((fromValue - 32) / 1.8) + 273.15
                case 'rankine':
                    return fromValue + 459.67
                case 'reaumur':
                    return (fromValue * 1.8) + 32
        case 'kelvin':
            match toScale.lower():
                case 'celsius':
                    return fromValue + 273.15
                case 'fahrenheit':
                    return ((fromValue - 273.15) * 1.8) + 32
                case 'kelvin':
                    return fromValue
                case 'rankine':
                    return fromValue / 1.8
                case 'reaumur':
                    return (fromValue - 273.15) / 1.25
        case 'rankine':
            match toScale.lower():
                case 'celsius':
                    return (fromValue - 491.67) / 1.8
                case 'fahrenheit':
                    return fromValue - 459.67
                case 'kelvin':
                    return fromValue / 1.8
                case 'rankine':
                    return fromValue
                case 'reaumur':
                    return (fromValue - 491.67) / 2.25
        case 'reaumur':
            match toScale.lower():
                case 'celsius':
                    return fromValue / 0.8
                case 'fahrenheit':
                    return (fromValue - 32) / 2.25
                case 'kelvin':
                    return (fromValue * 1.25) + 273.15
                case 'rankine':
                    return (fromValue * 2.25) + 491.67
                case 'reaumur':
                    return fromValue


# definir función para usar convertTo()

helpInfo = '''\
En este programa se pueden utilizar las siquientes escalas:

  ºC  Celsius   Escala originalmente con el 0 en la ebullición del agua y el 100
                en la solidificación, que luego se invirtió y quedó como la
                conocemos hoy en día.
   K  Kelvin    Basada en la Celsius, sitúa sin embargo el punto 0 en el llamado
                Cero Absoluto, a -273,15ºC. Es la unidad de temperatura del
                Sistema Internacional de Medidas, con la Celsius como accesoria.
  ºF  Farenheit Utilizada casi que exclusivamente en los EUA, Canadá o UK.
   R  Rankine   Basada en la escala Farenheit, sitúa, como la Kelvin, su punto 0
  Ra            en el 0 absoluto, a -459,67ºF. Aún se emplea para hacer estudios
                termodinámicos en UK (creada en Escocia) y Estados Unidos.
  ºR  Réaumur   Escala del s. XVII prácticamente en desuso, va de 0ºR a 80ºR
 ºRé            también del punto de fusión del agua al de ebullición.
    '''

args       = sys.argv
scriptName = args.pop(0)
showScales = has_cli_param('-s', args) or has_cli_param('--show-scales', args)
verbose    = has_cli_param('-v', args) or has_cli_param('--verbose',     args)
showHelp   = has_cli_param('-h', args) or has_cli_param('--help',        args)
argc       = len(args)

def main():
    if showHelp:
        print(f"""
            {helpInfo}

            Uso:
                {scriptName}              el programa pedirá la información
                {scriptName} -h           muestra esta ayuda
                {scriptName} --help       muestra esta ayuda
                {scriptName} <temperatura>
                {scriptName} <temperatura> <escala de origen>
                {scriptName} <temperatura> <escala de origen> <escala destino>

            Los valores son opcionales, pero se leerán siempre en orden.
            Es decir, el primer argumento será la temperatura a convertir.
            Si no se dan más parámetros, se le pedirán las escalas de origen
            y destino; si se da también la escala de origen, se pedirá
            solo la de destino.

            Ejemplos:

                {scriptName}               # el programa pedirá los tres valores
                {scriptName} celsius       # error: no es un valor numérico!
                {scriptName} 36.6          # se pedirán las escalas de origen y destino
                {scriptName} 32 ºC         # se pedirá la escala de destino
                {scriptName} 32 celsius ºF # hará el cálculo

            Para mostrar esta ayuda, use -h o --help
            """)
        exit()

    if showScales:
        print(helpInfo)

        # Tabla de escalas
        print(f"{'Scale':^10} | {'Symbol':^7} | {'Alternate':^10}")
        print("-" * 32)
        for name, attributes in scale.items():
            print(f"{name:<10} | {attributes['symbol']:^7} | {attributes['code']:<10}")

        exit()

    tempValue = float(args[0]) if argc > 0 else ask_num_value("Temperatura a convertir: ")
    fromScale = args[1]        if argc > 1 else input("Escala de origen (ver ayuda para opciones): ")
    toScale   = args[2]        if argc > 2 else input("Convertir a (ver ayuda para opciones): ")

    fromScale = get_scale_info('code', fromScale) if len(fromScale) < 3 else fromScale
    toScale   = get_scale_info('code', toScale)   if len(toScale)   < 3 else toScale

    result = convert_to(fromScale, tempValue, toScale)

    if verbose:
        print(f"{tempValue:.2f} {get_scale_info('symbol', fromScale)}",
              f"({get_scale_info('longName', fromScale)})",
              f"son {result:.2f} {get_scale_info('symbol', toScale)}",
              f"({get_scale_info('longName', toScale)}).")
    else:
        print(f"{result:.2f}{get_scale_info('symbol', toScale)}")

if __name__ == "__main__":
    main()
