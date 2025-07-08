import math
import sys
import argparse # queremos más flexibilidad en esto

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

def convertTo(*,
        fromScale: str='Celsius',
        fromValue: float = 0.0,
        toScale: str):
    pass

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
                    return (fromValue - 32)/1.8
                case 'fahrenheit':
                    return fromValue
                case 'kelvin':
                    return ((fromValue - 32)/1.8) + 273.15
                case 'rankine':
                    return fromValue + 459.67
                case 'reaumur':
                    return (fromValue * 1.8) + 32
        case 'kelvin':
            match toScale.lower():
                case 'celsius':
                    return fromValue + 273.15
                case 'fahrenheit':
                    return ((fromValue - 273.15)*1.8) + 32
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

# Definir diccionario de escala, nombre y símbolo para interpretar entrada

# definir función para usar convertTo()

# definir argumentos y parámetros del programa con argparse

def helpInfo():
    print('''\
        En este programa se pueden utilizar las siquientes escalas:

          Celsius - Escala originalmente con el 0 en la ebullición
                    del agua y el 100 en la solidificación, que luego
                    se invirtió y quedó como la conocemos ahora.
          Kelvin    Basada en la Celsius, sitúa sin embargo el punto 0
                    en el llamado Cero Absoluto, a -273,15ºC.
                    Es la unidad de temperatura del Sistema Internacional
                    de Medidas.
          Farenheit Utilizada casi que exclusivamente en los EUA
          Rankine   Basada en la escala Farenheit, sitúa, como la Kelvin,
                    su punto 0 en el 0 absoluto, a -459,67ºF. Aún se emplea
                    para hacer estudios termodinámicos en Inglaterra y Estados
                    Unidos.
          Réaumur   Escala del s. XVII prácticamente en desuso, va de 0ºR a 80ºR
                    también del punto de fusión del agua al de ebullición.
    ''')
