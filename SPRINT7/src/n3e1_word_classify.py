from cli_funcs import argc, args, showHelp, scriptName
from n1e3_wordCount import word_count, sortByFreq
from operator import itemgetter

if showHelp:
    exit(f'''
        {scriptName} [-s|--skip-words-once] [-f|--sort-by-freq] <text>|<filename>

        Use '-s' para ignorar palabras que solo aparecen una vez en el texto.

        Use '-f' para ordenar la lista resultante por frecuencia de aparición
        de cada palabra.

        El parámetro obligatorio es o bien un texto, o el nombre (ruta/fichero)
        del fichero a leer y procesar:

        {scriptName} -s fichero_de_ejemplo.txt
    ''')

def classify_word_count(text: str):
    palabras = word_count(text)

    if sortByFreq:
        palabras = sorted(palabras, key=itemgetter(1))
    else:
        list.sort(palabras)

    letras = [chr(x) for x in range(ord('a'), ord('z'))]
    lista  = {}

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

def main():
    text = args[0] if argc() else input("Texto o fichero a procesar: ")

    print(classify_word_count(text))

if __name__ == "__main__":
    main()
