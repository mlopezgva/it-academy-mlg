# SPRINT 7 - Python I: Tipos y estructuras de datos
> Primer sprint de Python.

## Nivel I
### `n1e1_imc.py`
Calcula el índice de masa corporal (IMC) a partir del peso y la altura. Permite introducir los valores por línea de comandos o solicitarlos al usuario.  Gestiona errores de entrada y proporciona un informe con la clasificación del IMC.

        $ p3 n1e1_imc.py
        Peso: 60
        Altura: 155

        En base al peso y altura indicados, su IMC es de 24.97.
        Este índice le sitúa en el rango de sobrepeso

> Ver la doc de este script en [N1E2-IMC](./doc/n1e1_imc.md)

### `n1e2_tempConverter.py`
Convierte temperaturas entre diferentes escalas (Celsius, Fahrenheit, Kelvin, Rankine, Réaumur).  Admite la entrada de parámetros por línea de comandos o la solicitud interactiva al usuario.  Muestra información detallada sobre las escalas si se solicita.

Si no se proporcionan argumentos, el script solicita la temperatura, la escala de origen y la escala de destino al usuario. Si solo se proporciona la temperatura, se solicita la escala de origen y la escala de destino. Si se proporcionan la temperatura y la escala de origen, se solicita solo la escala de destino.

> Ver la doc de este script en [N1E2-Conversor de temperaturas](./doc/n1e2_tempConverter.md)

### `n1e3_wordCount.py`
Cuenta las palabras en un texto dado. El texto puede ser proporcionado como argumento de línea de comandos o solicitado al usuario. Opcionalmente, puede omitir las palabras que aparecen una sola vez. Utiliza expresiones regulares para preprocesar el texto. Como extra, si el argumento es el nombre de un fichero existente, lee este fichero como entrada de texto.

Por ejemplo, usando `n1e3_wordCount.py -s README.md`, revisaría todas las palabras y las contaría.

### `n1e4_rdict.py`
Invierte claves y valores de un diccionario. Si el diccionario de entrada tiene múltiples claves con el mismo valor, devuelve un mensaje de error. Si el diccionario está vacío, devuelve un mensaje indicando que está vacío.

## Nivel II

> Ambos scripts en este nivel son funciones y llamadas de prueba, no scripts CLI al uso como los anteriores.

### `n2e1_rdict.py`
Invierte claves y valores de un diccionario. Si hay múltiples claves con el mismo valor, el valor en el diccionario invertido será una lista con todas las claves que compartían ese valor.  Gestiona el caso de un diccionario vacío, devolviendo un mensaje en ese caso.

Este script es en realidad una adaptación del n1e4_rdict.py, que tiene el mismo comportamiento, si se le pasa un segundo parámetro (`allow_duplicates`). Pero no pasándolo, agrupa los valores.

### `n2e2_convert_nums.py`
Recibe una lista de valores (números en formato string, números, listas anidadas...).  Separa los valores en dos listas: una con valores numéricos (convertidos a `int` o `float`) y otra con valores no numéricos. Gestiona diferentes formatos numéricos (incluidos números en notación científica) y listas anidadas.

## Nivel III
### `n3e1_word_classify.py`

Clasifica las palabras de un texto dado en función de la letra inicial.

El texto se puede proporcionar como argumento de línea de comandos o solicitarse al usuario.  El script utiliza la función `word_count` (del script `n1e3_wordCount.py`) para contar las palabras y omitir, opcionalmente, las que aparecen una sola vez (mediante el parámetro `-s` o `--skip-words-once`).  El resultado es un diccionario anidado donde la clave es la letra inicial (minúscula) de la palabra, y el valor es otro diccionario que contiene las palabras que empiezan por esa letra y sus recuentos.

Opciones:

* `-s` o `--skip-words-once`: Ignora palabras que solo aparecen una vez en el texto.
* `<text>` o `<filename>`: Texto o nombre de archivo que contiene el texto a procesar (obligatorio, aunque si no se le pasa nada, pide una entrada al usuario, pudiendo aún dar el nombre de un fichero).
