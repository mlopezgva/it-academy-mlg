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


Acepta los siguientes parámetros:

* **`-h` o `--help`**: Muestra la ayuda del script.
* **`-v` o `--verbose`**: Muestra detalles del cálculo del IMC.
* **`<peso en kg>`**: Peso de la persona en kilogramos (opcional, si no se proporciona, se solicita al usuario).
* **`<altura en m>`**: Altura de la persona en metros (opcional, si no se proporciona, se solicita al usuario).

#### Ayuda

    $ p3 n1e1_imc.py -h

        N1:E1 - Cálculo de IMC
        ----------------------

        Uso:
            n1e1_imc.py
            n1e1_imc.py
            n1e1_imc.py -h           muestra esta ayuda
            n1e1_imc.py --help       muestra esta ayuda
            n1e1_imc.py -v           muestra detalles del cálculo del IMC
            n1e1_imc.py --verbose    muestra detalles del cálculo del IMC
            n1e1_imc.py <peso en kg>
            n1e1_imc.py <peso en kg> <altura en m>

        Ambos parámetros son opcionales. Si solo se informa del primer
        valor este será el peso, y se le preguntará por la altura.  Si no
        se indica ningún valor, se le preguntará por ambos.

        Para mostrar esta ayuda, use -h o --help

#### Diferentes combinaciones de parámetros y _flags_

    $ p3 n1e1_imc.py 60 160

    En base al peso y altura indicados, su IMC es de 23.44.
    Este índice le sitúa en el rango de peso normal

---

    $ p3 n1e1_imc.py 60
    Altura: 160

    En base al peso y altura indicados, su IMC es de 23.44.
    Este índice le sitúa en el rango de peso normal

---

    $ p3 n1e1_imc.py 60
    Altura: 1.6

    En base al peso y altura indicados, su IMC es de 23.44.
    Este índice le sitúa en el rango de peso normal

    Si no se proporcionan argumentos, el script solicita tanto el peso como la altura al usuario. Si solo se proporciona el peso, se solicita la altura.

    $ p3 n1e1_imc.py -v
    Peso: 60
    Altura: 165

    Peso:   60.00 kg
    Altura:   1.65 m

        60.00
    IMC = —————— = 22.04
            1.65²

    En base al peso y altura indicados, su IMC es de 22.04.
    Este índice le sitúa en el rango de peso normal

---

    $ p3 n1e1_imc.py -v 60
    Altura: 1.58

    Peso:   60.00 kg
    Altura:   1.58 m

        60.00
    IMC = —————— = 24.03
            1.58²

    En base al peso y altura indicados, su IMC es de 24.03.
    Este índice le sitúa en el rango de peso normal

### `n1e2_tempConverter.py`
Convierte temperaturas entre diferentes escalas (Celsius, Fahrenheit, Kelvin, Rankine, Réaumur).  Admite la entrada de parámetros por línea de comandos o la solicitud interactiva al usuario.  Muestra información detallada sobre las escalas si se solicita.

Acepta los siguientes parámetros:

* **`-h` o `--help`**: Muestra la ayuda del script.
* **`-s` o `--show-scales`**: Muestra la lista de escalas de temperatura disponibles.
* **`-v` o `--verbose`**: Muestra información detallada de la conversión.
* **`<temperatura>`**: Temperatura a convertir (opcional, si no se proporciona, se solicita al usuario).
* **`<escala de origen>`**: Escala de temperatura de origen (opcional, si no se proporciona, se solicita al usuario).
* **`<escala de destino>`**: Escala de temperatura de destino (opcional, si no se proporciona, se solicita al usuario).

#### Ayuda

Esta es la ayuda que muestra el script usando `--help`

    $ p3 n1e2_tempConverter.py -h

        N1:E2 - Conversor de Temperatura
        --------------------------------
        En este programa se pueden utilizar las siquientes escalas:

      ºC  Celsius   Escala originalmente con el 0 en la ebullición del agua y el 100
                    en la solidificación, que luego se invirtió y quedó como la
                    conocemos hoy en día.
       K  Kelvin    Basada en la Celsius, sitúa sin embargo el punto 0 en el llamado
                    Cero Absoluto, a -273,15ºC. Es la unidad de temperatura del
                    Sistema Internacional de Medidas, con la Celsius como accesoria.
      ºF  Farenheit Utilizada casi que exclusivamente en los EUA, Canadá o UK.
       R  Rankine   Basada en la escala Farenheit, sitúa, como la Kelvin, su punto 0
      Ra            en el 0 absoluto, a -459,67ºF. Aún se emplea para hacer estudios
                    termodinámicos en UK (creada en Escocia) y Estados Unidos.
      ºR  Réaumur   Escala del s. XVII prácticamente en desuso, va de 0ºR a 80ºR
     ºRé            también del punto de fusión del agua al de ebullición.


    Uso:
        n1e2_tempConverter.py               El programa pedirá la información
        n1e2_tempConverter.py -h            Muestra esta ayuda
        n1e2_tempConverter.py --help        Muestra esta ayuda
        n1e2_tempConverter.py -s            Muestra la lista de escalas.
        n1e2_tempConverter.py --show-scales Muestra la lista de escalas.
        n1e2_tempConverter.py <temperatura>
        n1e2_tempConverter.py <temperatura> <escala de origen>
        n1e2_tempConverter.py <temperatura> <escala de origen> <escala destino>

    Los valores son opcionales, pero se leerán siempre en orden.
    Es decir, el primer argumento será la temperatura a convertir.
    Si no se dan más parámetros, se le pedirán las escalas de origen
    y destino; si se da también la escala de origen, se pedirá solo la
    de destino.

    Para referirse a una esca,a se puede utilizar cualqueira de los
    elementos de la lista de escalas (n1e2_tempConverter.py --show-scales).

    Ejemplos:

        n1e2_tempConverter.py               # el programa pedirá los tres valores
        n1e2_tempConverter.py celsius       # error: no es un valor numérico!
        n1e2_tempConverter.py 36.6          # se pedirán origen y destino
        n1e2_tempConverter.py 32 ºC         # se pedirá la escala de destino
        n1e2_tempConverter.py 32 celsius ºF # hará el cálculo

    Para mostrar esta ayuda, use -h o --help

---

    $ p3 n1e2_tempConverter.py -s
        En este programa se pueden utilizar las siquientes escalas:

        ºC  Celsius     Escala originalmente con el 0 en la ebullición del agua y el 100
                        en la solidificación, que luego se invirtió y quedó como la
                        conocemos hoy en día.
        K  Kelvin       Basada en la Celsius, sitúa sin embargo el punto 0 en el llamado
                        Cero Absoluto, a -273,15ºC. Es la unidad de temperatura del
                        Sistema Internacional de Medidas, con la Celsius como accesoria.
        ºF  Farenheit   Utilizada casi que exclusivamente en los EUA, Canadá o UK.
        R  Rankine      Basada en la escala Farenheit, sitúa, como la Kelvin, su punto 0
        Ra              en el 0 absoluto, a -459,67ºF. Aún se emplea para hacer estudios
                        termodinámicos en UK (creada en Escocia) y Estados Unidos.
        ºR  Réaumur     Escala del s. XVII prácticamente en desuso, va de 0ºR a 80ºR
        ºRé             también del punto de fusión del agua al de ebullición.

        Scale      | Symbol  | Alternate
        --------------------------------
        Celsius    |   ºC    | celsius
        Fahrenheit |   ºF    | fahrenheit
        Kelvin     |    K    | kelvin
        Rankine    |    R    | rankine
        Réaumur    |   ºR    | reaumur

Si no se proporcionan argumentos, el script solicita la temperatura, la escala de origen y la escala de destino al usuario. Si solo se proporciona la temperatura, se solicita la escala de origen y la escala de destino. Si se proporcionan la temperatura y la escala de origen, se solicita solo la escala de destino.

#### Ejemplos
Aquí hay una secuencia de conversiones desde los 559.67 Rankines por las otras escalas, y de vuelta a los Rankines. Una forma de comprobar que las conversiones son correctas.

        $ p3 n1e2_tempConverter.py 559.67 "rankine"  "Fahrenheit"
        559.67R = 100.00ºF

        $ p3 n1e2_tempConverter.py 100 "ºF" "Celsius"
        100.0ºF = 37.78ºC

        $ p3 n1e2_tempConverter.py 37.78 ºC reaumur
        37.78ºC = 30.22ºR

        $ p3 n1e2_tempConverter.py 30.22 ºR K
        30.22ºR = 310.92K

        $ p3 n1e2_tempConverter.py 310.92 'K' 'R'
        310.92K = 559.66R

Usndo la opción `--verbose` cambia la salida a una frase, en lugar de una igualdad matemática:

        $ p3 n1e2_tempConverter.py 559.67 "rankine"  "Fahrenheit" -v
        559.67 R (Rankines) son 100.00 ºF (grados Fahrenheit).

        $ p3 n1e2_tempConverter.py 100 "ºF" "Celsius" -v
        100.00 ºF (grados Fahrenheit) son 37.78 ºC (grados Celsius).

        $ p3 n1e2_tempConverter.py 37.78 ºC reaumur -v
        37.78 ºC (grados Celsius) son 30.22 ºR (grados Réaumur).

        $ p3 n1e2_tempConverter.py 30.22 -v ºR K
        30.22 ºR (grados Réaumur) son 310.92 K (Kelvins).

        $ p3 n1e2_tempConverter.py 30.22 -v ºR K
        30.22 ºR (grados Réaumur) son 310.92 K (Kelvins).

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
