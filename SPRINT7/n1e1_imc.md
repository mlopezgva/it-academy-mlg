Nivell 1
===
Exercici 1
---

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
El script detecta si se han pasado opciones posibles:

### Ayuda con `-h`o `--help`
Muestra un texto con los detales de uso del script.

### Detalles con `-v` o `-verbose`
Además del resultado, muestra la operación realizada.
