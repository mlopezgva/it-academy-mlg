import os
import re
from operator import itemgetter
from cli_funcs import sys, has_cli_param, args, showHelp, scriptName
LF = "\n"

if showHelp:
    exit(f'''
        N1:E3 - Word Count

        Usage:

        {scriptName} [-s|--skip-words-once] [-f|--sort-by-freq] <text>|<filename>

        Use '-s' to skip words that appear only once in the text.

        Use '-f' to sort the output by word frequency.

        You can pass a filepath as parameter. If it exists, it will try to read
        it and use its contents as text and process it.

        You can write anything after the script name and it will be processed.

        Or, you can use it without parameters and it will ask for the text to
        process.

    ''')

skipOneCount = has_cli_param(['-s','--skip-once-word','--skip-word-once'],args)
verbose      = has_cli_param(['-v', '-verbose'], args)
sortByFreq   = has_cli_param(['-f', '--sort-by-freq'], args)

def word_count(data, skip_once_words: bool=False):
    response = []
    global skipOneCount

    skip_unique = skipOneCount or skip_once_words or False

    if os.path.isfile(data):
        if verbose:
            print("Reading file", data)

        with (open(data, 'r') as fileToRead):
            strToCount = fileToRead.read()
    else:
        strToCount = data

    # Elimina caracteres no alfabéticos, y también los números sueltos
    words = re.sub(
        r"(\b\d+\b)|[^a-zA-Z0-9ÁÄÃÂÀÉËÊÈÍÏÎÓÖÕÔÒÚÜÛÙÑáäãâàéëêèíïîóöõôòúüûùñ @]",
        ' ',
        strToCount.lower()).split()
    distinctWords = set(words)

    for w in distinctWords:
        wc = words.count(w)

        if wc == 1 and skip_unique:
            continue

        response.append([w, wc])
    return response

def show_wc(distinct_words: list):
    response = []
    template = "{} - aparece {} {}"

    if sortByFreq:
        palabras = sorted(palabras, key=itemgetter(1))
    else:
        list.sort(palabras)

    for w in distinct_words:
        word, wc = w

        response.append(template.format(word, wc, "vez" if wc == 1 else "veces"))

    return LF.join(response)

def main():
    # Si se le pasa un texto por parámetros, leerlo. Si no, preguntar
    data = ' '.join(sys.argv) if len(sys.argv) else input("Fichero o texto a contar:")

    print(show_wc(word_count(data, skipOneCount)))

if __name__ == "__main__":
    main()
