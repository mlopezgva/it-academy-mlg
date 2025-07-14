from cli_funcs import has_cli_param, \
    ask_num_value, argc, args, showHelp, scriptName
from n1e3_wordCount import word_count, skipOneCount

if showHelp:
    exit(f'''
        {scriptName} [-s|--skip-words-once] <text>|<filename>

        Use '-s' para ignorar palabras que solo aparecen una vez en el texto.

        El parámetro obligatorio es o bien un texto, o el  nombre (ruta/fichero)
        a leer y procesar:

        {scriptName} -s fichero_de_ejemplo.txt
    ''')

def classify_word_count(text: str):
    palabras = word_count(text)
    list.sort(palabras)

    letras   = [chr(x) for x in range(ord('a'), ord('z'))]
    lista    = {}

    for char in letras:
        lista[char] = {}

    for (palabra, contador) in palabras:
        letra = palabra[0].lower()
        # Ignorar "palabras" que no empiezan por una letra
        if letra not in letras:
            continue
        # print({letra: (palabra, contador)})
        lista[letra].update({palabra: contador})

    return lista

text = args[0] if argc() else input("Texto o fichero a procesar: ")

print(text)

print(classify_word_count(text))
