Nivell 1
===
Exercici 2
---

(Viene del [README del Sprint 7](../README.md))

### Conversor de temperaturas

Existeixen diverses unitats de temperatura utilitzades en diferents contextos i regions. Les més comunes són Celsius (°C), Fahrenheit (°F) i Kelvin (K). També existeixen altres unitats com Rankine (°Ra) i Réaumur (°Re). Selecciona almenys 2 conversors, de tal manera que en introduir una temperatura retorni, com a mínim, dues conversions.

### Factores de conversión de temperaturas
Se han seleccionado cinco escalas de temperaturas, desde las históricas **Réaumur** o **Rankine**, a las actualmente utilizadas **Celsius**, **Fahrenheit** y la escala del S.I., el **Kelvin**.

Así pues, en este programa se pueden utilizar las siquientes escalas:

Símbolo | Nombre | Información
:---:|---|---
  ºC |  Celsius | Escala originalmente con el 0 en la ebullición del agua y el 100 en la solidificación, que luego se invirtió y quedó como la conocemos hoy en día.
   K | Kelvin |  Basada en la Celsius, sitúa sin embargo el punto 0 en el llamado Cero Absoluto, a -273,15ºC. Es la unidad de temperatura del Sistema Internacional de Medidas, con la Celsius como accesoria.
  ºF | Farenheit | Utilizada casi que exclusivamente en los EUA, Canadá o UK.
   R<br>Ra | Rankine |  Basada en la escala Farenheit, sitúa, como la Kelvin, su punto 0 en el 0 absoluto, a -459,67ºF. Aún se emplea para hacer estudios termodinámicos en UK (creada en Escocia) y Estados Unidos.
  ºR<br>ºRé | Réaumur |  Escala del s. XVII prácticamente en desuso, va de 0ºR a 80ºR también del punto de fusión del agua al de ebullición.

Conversión | Fórmula
---|---
De Celsius a Fahrenheit | ºF = ºC × 1,8 + 32
De Celsius a Kelvin | K = ºC + 273,15
De Celsius a Rankine | R = (ºC + 273.15) × 9/5
De Celsius a Réaumur | ºR = (4/5) ºC
De Fahrenheit a Celsius | ºC = (ºF – 32) / 1,8
De Fahrenheit a Kelvin | K = (ºF – 32) / 1,8 + 273,15
De Fahrenheit a Rankine | R = ºF + 459,67
De Fahrenheit a Réaumur | ºF = (9/5) ºC + 32
De Kelvin a Celsius | ºC = K – 273,15
De Kelvin a Fahrenheit | ºF = 1,8 × (K – 273,15) + 32
De Kelvin a Rankine | R = K × (9.5) (o: R = K / 1.8)
De Kelvin a Réaumur | ºR = (K - 273,15) / (5/4)
De Rankine a Celsius | ºC = (R – 491,67) × 5/9
De Rankine a Fahrenheit | ºF = R – 459,67
De Rankine a Kelvin | K = R × 5/9
De Rankine a Réaumur | ºR = (R - 491.67) / 2.25000002
De Réaumur a Celsius | ºC = (5/4) × ºR
De Réaumur a Farenheit | ºR = (4/9)(ºF – 32)
De Réaumur a Kelvin | K = (ºR × 1.25) + 273,15
De Réaumur a Rankine | R = (ºR × 2.25) + 491.67

### 'Flags' de líenea de comandos
Acepta los siguientes parámetros:

* **`-h` o `--help`**: Muestra la ayuda del script.
* **`-s` o `--show-scales`**: Muestra la lista de escalas de temperatura disponibles.
* **`-v` o `--verbose`**: Muestra información detallada de la conversión.
* **`<temperatura>`**: Temperatura a convertir (opcional, si no se proporciona, se solicita al usuario).
* **`<escala de origen>`**: Escala de temperatura de origen (opcional, si no se proporciona, se solicita al usuario).
* **`<escala de destino>`**: Escala de temperatura de destino (opcional, si no se proporciona, se solicita al usuario).

Si no se proporcionan argumentos, el script solicita la temperatura, la escala de origen y la escala de destino al usuario. Si solo se proporciona la temperatura, se solicita la escala de origen y la escala de destino. Si se proporcionan la temperatura y la escala de origen, se solicita solo la escala de destino.

### Ejemplos
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

