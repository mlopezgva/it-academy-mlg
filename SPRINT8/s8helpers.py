import configparser
import mysql.connector
import pandas as pd

LF="\n"

def is_defined(varname):
    return varname in globals()

# Conectar con la base de datos. Datos de la conexión en db.ini
# Devuelve la variable `db` para poder usarla en otros ambientes
# (al definirla en el módulo, no es visible fuera, así que la devuelve
# para que esté disponible para quien ha pedido la conexión)
def db_connect():
    try:
        cfgFp = open('db.ini', mode='r')
        iniFp = configparser.ConfigParser()
        iniFp.read_file(cfgFp)
        dbCfg = dict(iniFp.items('database'))

        # print(dbCfg, dbCfg['host'])

        if not is_defined('db') or not db.is_connected():
            db = mysql.connector.connect(
                host=dbCfg['host'],
                database=dbCfg['database'],
                user=dbCfg['user'],
                password=dbCfg['password']
            )
            print("Conectado!")

        return db

    except Exception as e:
        exit("Error:", e)

# Funciones para el color de barras y otros posibles usos
def get_color(number, color_map):
    '''
    #### Helper function for `column_colors()`
    @param number     int   Number to check which color would be
    @param color_map  dict  KEY is a numeric value to check `number` against
                            or literal `else` for the highest values
                            The dict will be sorted numerically, so is it not
                            necessary (but better for legibility) to create it
                            already sorted.
    @returns str   Hex color code or color name
    '''
    sorted_keys = sorted(key for key in color_map.keys() if isinstance(key, int))

    # Primero los valores extremos...
    if number < sorted_keys[0]:
        return color_map[sorted_keys[0]]
    elif number > sorted_keys[-1]:
        return color_map['else']

    # Ahora los valores de las keys
    for key in sorted_keys:
        if number < key:
            return color_map[key]

    return color_map[sorted_keys[-1]]

# Funciones para crear listas de colores para columnas
def list_dividers(numbers, n):
    max_value = max(numbers)
    print(max_value)
    next_multiple_of_5 = math.ceil(max_value / 5) * 5

    points = []

    for i in range(1, n):
        point = int((i / n) * next_multiple_of_5)
        points.append(point)

    return points

def color_list_to_dict(values, color_list):
    keys      = list_dividers(values, len(color_list))
    color_map = dict(zip(keys+['else'], color_list))
    return color_map

def column_colors(values, color_map: dict):
    '''
    Returns a list of colors for a given list of values, setting the color
    for that value from a dictionary.

    The 'else' key sets the color for any value greater than the last defined.

    Usage:
        values = [2,4,5,7,9]
        colormap1 = {4: 'red', 8: 'amber', 'else': 'green'}
        colormap2 = {3: 'orange', 5: 'amber', 8: 'cyan', 'else': 'green'}

        column_color(values, colormap1)

        Would return

        ['red', 'amber', 'amber', 'amber', 'green']

        While

        column_color(values, colormap2)

        Should return

        ['orange', 'amber', 'amber', 'cyan', 'green']
    '''
    cc = []

    for n in values:
        cc.append(get_color(n, color_map))
    return cc


def fullname(row):
    return f"{row['name']} {row['surname']}"
