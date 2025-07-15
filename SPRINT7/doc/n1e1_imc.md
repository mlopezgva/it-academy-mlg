Nivell 1
===
Exercici 1
---

(Viene del [README del Sprint 7](../README.md))

### Calculadora de l'índex de massa corporal

Escriu una funció que calculi l'IMC ingressat per l'usuari/ària, és a dir, qui ho executi haurà d'ingressar aquestes dades.

La funció ha de classificar el resultat en les seves respectives categories

### El cálculo del IMC
Para calcular el IMC es necesario dividir el peso en kg de un paciente entre el cuadrado de su altura en metros. Con esto obtendremos un valor que se situará en uno de los siguientes rangos:

Bajo peso: menos de 18,5.
Peso normal: 18,5-24,9.
Sobrepeso: 25-29,9.
Obesidad: más de 30.

Fórmula:

$$ IMC = \frac{P}{a^2} $$

## El script
El script está diseñado para admitir una serie de parámetros y valores directamente desde la línea de comandos. Puesto que los valores son obligatorios para poder realizar el caĺculo, si no se indican esos valores, o falta alguno de ellos, el script preguntará lo que falte.

### Validación
Se comprueba que ambos valores sean numéricos, y se detiene el script con un mensaje de error si nalguno de ellos no lo es.

Se realiza una validación sencilla de la altura. Si está en el rango de las centenas, se divide entre 100, asumiendo que se ha indicado la altura en cm en lugar de en metros.

si, aun así, la altura supera los 2.5m, se da como erónea, se pmuestra un mensaje de error y se termina el script.

### 'Flags' de líenea de comandos
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
