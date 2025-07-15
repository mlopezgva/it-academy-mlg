'''
Extracción de las funciones comunes a todos los scripts para
administrar los parámetros de línea de comandos.
'''
import sys

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

def argc():
    global args
    return len(args)

args       = sys.argv
scriptName = args.pop(0)
showHelp   = has_cli_param('-h', args) or has_cli_param('--help', args)

