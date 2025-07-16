#!/usr/bin/python3
from cli_funcs import has_cli_param, \
    ask_num_value, argc, args, showHelp, scriptName

# Definir diccionario de escala, nombrey símbolo para interpretar entrada
# Define conversiones de y a Kelvin para realizar las conversiones
scales = {
    "celsius":    {
        "symbol":   "ºC",
        'name':     "Celsius",
        'longName': 'grados Celsius',
        'to_k':     (lambda temp: 273.15 + temp),
        'from_k':   (lambda temp: temp - 273.15)
    },
    "fahrenheit": {
        "symbol":   "ºF",
        'name':     "Fahrenheit",
        'longName': 'grados Fahrenheit',
        'to_k':     (lambda temp: ((temp - 32) / 1.8) + 273.15),
        'from_k':   (lambda temp: ((temp - 273.15) * 1.8) + 32)
    },
    "kelvin":     {
        "symbol":   "K",
        'name':     "Kelvin",
        'longName': 'Kelvins',
        'to_k':     (lambda temp: temp),
        'from_k':   (lambda temp: temp)
    },
    "rankine":    {
        "symbol":   "R",
        'name':     "Rankine",
        'longName': 'Rankines',
        'to_k':     (lambda temp: temp / 1.8),
        'from_k':   (lambda temp: temp * 1.8)
    },
    "reaumur":    {
        "symbol":   "ºR",
        'name':     "Réaumur",
        'longName': 'grados Réaumur',
        'to_k':     (lambda temp: (temp * 1.25) + 273.15),
        'from_k':   (lambda temp: (temp - 273.15) / 1.25)
    }
}
def get_scale_info(attr, value):
    '''
    Returns the desired attr (eg. the name or the symbol) of a scale,
    based on any of the values in the row.

    get_scale_info('symbol', 'Celsius')
    returns `ºC`
    '''
    # "Aplana" el diccionario anterior ("comprehension", se llama esto...)
    Scales = [
        {"code": name, **attributes} for name, attributes in scales.items()
    ]

    for scale in Scales:
        if value in scale.values():
            return scale[attr] if attr in scale else ''
    return ''

def convert_to(
        fromValue: float,
        fromScale: str,
        toScale:   str):

    return scales[toScale]['from_k'](
        scales[fromScale]['to_k'](fromValue)
    )

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

showScales = has_cli_param('-s', args) or has_cli_param('--show-scales', args)
verbose    = has_cli_param('-v', args) or has_cli_param('--verbose',     args)

def print_conversion(tempValue, fromScale, toScale, result, verbose):
    if verbose:
        print(f"{tempValue:.2f} {get_scale_info('symbol', fromScale)}",
              f"({get_scale_info('longName', fromScale)})",
              f"son {result:.2f} {get_scale_info('symbol', toScale)}",
              f"({get_scale_info('longName', toScale)}).")
    else:
        print(f"{tempValue}{get_scale_info('symbol', fromScale)} = {result:.2f}{get_scale_info('symbol', toScale)}")


def main():
    if showHelp:
        print(f"""
            N1:E2 - Conversor de Temperatura
            --------------------------------
            {helpInfo}

            Uso:
                {scriptName}               El programa pedirá la información
                {scriptName} -h            Muestra esta ayuda
                {scriptName} --help        Muestra esta ayuda
                {scriptName} -s            Muestra la lista de escalas.
                {scriptName} --show-scales Muestra la lista de escalas.
                {scriptName} <temperatura>
                {scriptName} <temperatura> <escala de origen>
                {scriptName} <temperatura> <escala de origen> <escala destino>

            Los valores son opcionales, pero se leerán siempre en orden.
            Es decir, el primer argumento será la temperatura a convertir.
            Si no se dan más parámetros, se le pedirán las escalas de origen
            y destino; si se da también la escala de origen, se pedirá solo la
            de destino.

            Para referirse a una escala se puede utilizar cualquiera de los
            elementos de la lista de escalas ({scriptName} --show-scales).

            Ejemplos:

                {scriptName}               # el programa pedirá los tres valores
                {scriptName} celsius       # error: no es un valor numérico!
                {scriptName} 36.6          # se pedirán origen y destino
                {scriptName} 32 ºC         # se pedirá la escala de destino
                {scriptName} 32 celsius ºF # hará el cálculo cd ºC a ºF

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

    tempValue = float(args[0]) if argc() > 0 else ask_num_value("Temperatura a convertir: ")
    fromScale = args[1]        if argc() > 1 else input("Escala de origen (ver ayuda para opciones): ")
    toScale   = args[2]        if argc() > 2 else input("Convertir a\n(ver ayuda para opciones, <Enter> para convertir a todas las escalas): ")

    fromScale = get_scale_info('code', fromScale) if len(fromScale) < 3 else fromScale
    toScale   = get_scale_info('code', toScale)   if len(toScale)   < 3 else toScale

    if not toScale:
        for to_scale in scales.keys():
            # print(f"Convierte de {fromScale} a {to_scale}")
            if fromScale == to_scale:
                continue
            result = convert_to(tempValue, fromScale, to_scale)
            print_conversion(tempValue, fromScale, to_scale, result, verbose)
    else:
        result = convert_to(tempValue, fromScale, toScale)
        print_conversion(tempValue, fromScale, toScale, result, verbose)

if __name__ == "__main__":
    main()
