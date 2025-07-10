import os
import re
from cli_funcs import *

# Si se le pasa un texto por parámetros, leerlo. Si no, preguntar
data = ' '.join(sys.argv) if len(sys.argv) else input("Fichero o texto a contar:")

if os.path.isfile(data):
    with (open(data, 'r') as fileToRead):
        strToCount = fileToRead.read()
else:
    strToCount = data.lower()   # Rosa y rosa son la misma palabra...

# regex para quitar lo que no sean caracteres alfanuméricos, pero dejando acentos.
words = re.sub("[^a-zA-Z0-9ÁÄÃÂÀÉËÊÈÍÏÎÓÖÕÔÒÚÜÛÙÑáäãâàéëêèíïîóöõôòúüûùñ @-]", '', strToCount).split()
distinctWords = set(words)

skipOneCount = has_cli_param('-s', args) \
            or has_cli_param('--skip-once-word', args) \
            or has_cli_param('--skip-word-once', args)
template = "La palabra {} aparece {} {}"

for w in distinctWords:
    wc = words.count(w)

    if wc == 1 and skipOneCount:
        continue
    print(template.format(w, wc, "vez" if wc == 1 else "veces"))
