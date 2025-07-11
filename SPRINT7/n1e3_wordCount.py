import os
import re
from cli_funcs import sys, has_cli_param, \
    argc, args, showHelp, scriptName

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

# Si se le pasa un texto por parámetros, leerlo. Si no, preguntar
data = ' '.join(sys.argv) if len(sys.argv) else input("Fichero o texto a contar:")

if os.path.isfile(data):
    with (open(data, 'r') as fileToRead):
        strToCount = fileToRead.read().lower()
else:
    strToCount = data.lower()   # Rosa y rosa son la misma palabra...

# regex para quitar lo que no sean caracteres alfanuméricos, pero dejando acentos.
words = re.sub(
    r"(\b\d+\b|[^a-zA-Z0-9ÁÄÃÂÀÉËÊÈÍÏÎÓÖÕÔÒÚÜÛÙÑáäãâàéëêèíïîóöõôòúüûùñ @])",
    ' ',
    strToCount,
    flags=re.MULTILINE)

def word_count(text, skip_once_words: bool=False):
    words = re.sub(r"\s{2,}", ' ', text).split()

    distinctWords = set(words)  # el set() elimina automáticamente los duplicados...
    max_word_len = len(max(distinctWords, key=len))

    template = "La palabra {} aparece {} {}"
    template = "{} aparece {} {}"

    for w in distinctWords:
        wc = words.count(w)

        if wc == 1 and skipOneCount:
            continue

        print(template.format(w, wc, "vez" if wc == 1 else "veces"))

word_count(words)
