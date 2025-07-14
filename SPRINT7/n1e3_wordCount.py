import os
import re
from cli_funcs import sys, has_cli_param, \
    argc, args, showHelp, scriptName
LF = "\n"

if showHelp:
    exit(f'''
        N1:E3 - Word Count

        Usage:

        {scriptName} [-s | --skip-once-word] [filename | <text>]

        Use '-s'  to skip words that appear only once in the text.

        You can pass a filepath as parameter. If it exists, it will try to read
        it and use its contents as text and process it.

        You can write anything after the script name and it will be processed.

        Or, you can use it without parameters and it will ask for the text to
        process.

    ''')

skipOneCount = has_cli_param('-s', args) \
    or has_cli_param('--skip-once-word', args) \
    or has_cli_param('--skip-word-once', args)
verbose      = has_cli_param('v', args) or has_cli_param('--verbose', args)

def word_count(data, skip_once_words: bool=False):
    response = []
    global skipOneCount

    skip_unique = skipOneCount or skip_once_words or False

    if os.path.isfile(data):
        with (open(data, 'r') as fileToRead):
            strToCount = fileToRead.read()
    else:
        strToCount = data

    # Elimina caracteres no alfabéticos, y también los números sueltos
    words         = re.sub(r"(\b\d+\b)|[^a-zA-Z0-9ÁÄÃÂÀÉËÊÈÍÏÎÓÖÕÔÒÚÜÛÙÑáäãâàéëêèíïîóöõôòúüûùñ @]", ' ', strToCount).split()
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
