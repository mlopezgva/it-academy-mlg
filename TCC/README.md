---
tags:tcc,DataAnalytics
---
[CLueArticle]: https://helloclue.com/es/articulos/ciclo-a-z/el-mito-de-las-fases-lunares-y-la-menstruacion
[ClueHistogram]: https://images.ctfassets.net/juauvlea4rbf/2jqTWw7u5gqLrzHTSKHJ1X/b7bcb49aa9c033ff91950d3d0328fee0/inside_graph_ES_2x.png?w=2400&h=1200&q=50&fm=webp
[SleepStudy]: https://www.cell.com/current-biology/fulltext/S0960-9822(13)00754-9
[HRLC]: https://www.cell.com/action/showPdf?pii=S0960-9822%2808%2900865-8
[LunarCycleHomFinland]: https://bmjopen.bmj.com/content/9/1/e022759
[monnHomicideRateFinland]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6340448/
[IDESCAT]: https://www.idescat.cat
[INE]: https://ine.es/dyngs/INEbase/listaoperaciones.htm
[Flourish]: https://app.flourish.studio
[Canva]: https://www.canva.com
[circadiano]: Del latín "circa" (cerca de) y "día", es decir, ciclos diarios.
[circadianos]: Del latín "circa" (cerca de) y "día", es decir, ciclos diarios.
*[SAD]: Seasonal Affective Disorder

# Correlaciones lunáticas
Breve estudio estadístico sobre la correlación entre la Luna y algunos eventos humanos.

[TOC]

## Abstract | Resumen
Este conciso análisis sobre una serie de series de datos de actividades humanas busca determinar si hay alguna correlación que pudiese hacer pensar en una causalidad entre los ciclos lunares y diversas actividades o eventos.

## Introducción
Aunque parezca algo trivial, el estudio de la influencia de la Luna, único cuerpo celeste aparte del Sol, con la cercanía y tamaño para influenciar de alguna forma a humanos y otros seres vivos ha sido un tema recurrente desde tiempos prehistóricos, antes de las Matemáticas.

Hay tres grandes campos de interés humano sobre la Luna:

- los marineros: tanto por las mareas como por la navegación nocturna.
- las mujeres: menstruación y parto.
- la agricultura: períodos de siembra y de cosecha.

Luego, de forma más reciente, la posible relación entre ciclos lunares y la violencia (accidentes, homicidios, violencia doméstica...) y, más recientemente, sobre los ciclos _circadianos_.

Los experimentos controlados y el uso de mediciones empíricas ha demostrado, por ejemplo, la influencia del ciclo lunar en los tiempos de sueño medio en humanos. Dormimos de media unos cuantos minutos menos en la Luna Llena que en la Luna Nueva, por ejemplo.

Luego tenemos las "leyendas urbanas" sobre la influencia lunar en la menstruación (hay tantas historias sobre lo que influencia la menstruación que casi resulta cómico). Un estudio finlandés sobre en suicidio en una región septentrional del país muestra, sin embargo, una interesante correlación entre una desviación de la incidencia de suicidios, el ciclo lunar, la estación invernal y las mujeres que están cerca de entrar en la menopausia. Otro nos muestra la posible correlación entre las variaciones en el tiempo de sueño y la calidad del sueño en relación a las fases lunares.

Mención aparte para los estudios sobre la influencia de la Luna en la agricultura. En el crecimiento de las plantas, como muchos jardineros y horticultores aficionados saben, influyen muchísimas variables.

Y una de ellas es la luz. Más allá de la mitología y las tradiciones, no debemos olvidar algunos detalles importantes sobre la Luna:

1. la influencia gravitacional depende de su proximidad a la Tierra, no a la fase lunar (la Luna es la misma y pesa igual, solo está iluminada desde diferentes ángulos) y,

2. la luz que recibimos de la Luna, como se intuye del punto anterior, es luz solar; mucho menor por ser un objeto pequeño en términos astronómicos.

¿Por qué es importante? Bueno, primero, porque la influencia gravitacional es discutible como poco; y segundo, porque las plantas se crecen con la luz, gracias a la fotosíntesis, yb puesto que la luz de la Luna es luz solar, cuanta más (Luna Llena) luz, mayor es la acción clorofílica y fotosintética. Es "normal", pues, que durante la Luna Llena crezcan más las cosechas. Y el momento de la siembra debe hacer coresponder el brote de dichas semillas fuera de la tierra con el Cuarto Creciente, para que ese pequeño brote reciba la mayor cantidad de luz en esa primera fase. Como decía antes, por supuesto, **no** es el único factor relevante para la salud de la planta, pero sí lo es para el crecimiento: la humedad es vital, pues el agua es necesaria para la fotosíntesis, especialmente para regadío.

Y como no podía ser menos, se han hecho algunos estudios sobre el tema.

### El gran mito: la menstruación
Otros estudios muestran que más allá del hecho de que los ciclos menstruales son "individuales", un segmento de la población femenina presenta una frecuencia de _sincronía_ superior a la media y que se desvía de la coincidencia temporal; es decir, del hecho de que eventos con ciclos diferentes converjan periódicamente. Antes de la era digital era más difícil realizar estudios con gran cantidad de sujetos. Con la llegada de los _smartphones_ y las aplicaciones de seguimiento del ciclo menstrual, sin embargo, los investigadores tienen acceso a los datos empíricos de millones de mujeres, y estos datos demuestran que no existe una relación directa entre las fases lunares (sinódica o sideral) y la frecuencia de la regla. Como curiosidad y para impedir el cierre de este tipo de estudios, algunos de ellos resaltan lo que se ha dado en llamar "resincronización anual" coincidiendo, curiosamente, con la Luna Llena posterior al Solsticio de Invierno. Aun así, una ligera correlación no implica para nada una causalidad...

Los estudios anteriores a 2015 se basaban en datos de decenas, unos cientos o algunos más ambiciosos hasta algo más de mil participantes; pero como decíamos, tras la aparición de diversas aplicaciones donde mujeres del mundo entero, prácticamente, informan de sus ciclos, los datos disponibles han aumentado en varios órdenes de magnitud, como veremos más adelante.

### Estudios anteriores
Durante la minería de datos, es decir, la búsqueda de conjuntos de datos (_datasets_) para este estudio ligero, he visto otros estudios, mucho más serios y rigurosos, sobre la influencia de la luna en algunos biorritmos y en la psique humana. Quiero destacar algunos de esos estudios.

Pese a que concluyen que no hay una relación estadística entre la Luna y las acciones o eventos humanos, sí deteca estos en algunas especies animales. Ciclos de reproducción de animales marinos, como los corales, se explican, sin embargo, por las mareas más que por las fases de la Luna: las mareas tienen como origen la proximidad de la Luna, no sus fases.

#### _Synodic lunar phases and suicide: based on 2605 suicides over 23 years, a full moon peak is apparent in premenopausal women from northern Finland_
Este estudio lanza un par de detalles que parecen alentar esas "leyendas" o "saber popular" sobre la relación entre mujeres y la Luna: el estudio sobre 2600+ suicidios a lo largo de 23 años en esa región no encuentra correlación alguna entre los ciclos lunares y los suicidios en _hombres_: en las cuatro estaciones y en las "4 fases" lunares, se obseva una distribución cercana al 25% en todos. En las mujeres, en cambio, hay desviaciones evidentes en Luna Llena o Nueva (especialmente en invierno; esto viene causado, en parte, por el SAD, un transtorno clínicamente reconocido que altera significativamente ciclos de sueño, aumento de pesadillas y otros síntomas) que afectan especialmente a mujeres pre-menopáusicas. Esto añade un nuevo dato que aumenta la dificultad en comprender cuál es el mecanismo de esa correlación.

#### _Evidence that the Lunar Cycle Influences Human Sleep_
Este estudio, que se puede encontrar en la web ([_Evidence that the Lunar Cycle Influences Human Sleep_][SleepStudy]), es un estudio empírico que me parece bastante completo (a pesar de contar con 33 participantes), en el que se analizan parámetros tan diversos como la concentración de melatonina en la saliva en la media hora previa al sueño, diferencias entre si hacían siestas o no durante el día, etc. Se tomadron muestras de saliva, sangre, se hicieron EEGs y otras prueba durante un período intermitente entre junio de 2000 y diciembre de 2003. Los sujetos eran básicamente sanos, no tomaban drogas, algunas de las mujeres tomaban anticonceptivos orales (dato a tener en cuenta, dado que se trata de hormonas que, también, podrían influir en la calidad del sueño).

Un punto interesante que cita el mismo estudio es que originalmente se trataba de un anñalisis de los ritmos circadianos así como los cambios homeostáticos que se producen en el cuerpo cuando comienzan las fases de sueño y de vigilia (al despertar), y fue solamente después de una converesación en un bar (lugar habitual de grandes ideas) cuando pensaron en añadir esta información a sus análisis estadísticos. Implica que los sujetos no eran conscientes de la posible correlación, evitando así algún efecto placebo, o psicosomático, en relación a la Luna y su sueño.

El resultado de este estudio no es concuyente según sus autores, pero muestran un patrón ligado a la Luna Llena y Nueva de difícil explicación física, ya que el efecto de la gravedad lunar en masas de agua menores que el mar Caspio, por ejemplo, no es mesurable, citando un estudio recopilatorio ([_Human Responses to the Geophysical Daily, Annual and Lunar Cycles_][HRLC]) sobre la influencia de la Luna sobre la vida humana. Este último expone toda una serie de eventos humanos que se cree pueden estar influenciados por los ciclos lunares (tanto revolución como proximidad) que, en realidad, no se ha podido demostrar que lo estén:

- Psicosis, depresión, ansiedad
- *Comportamiento violento/agresión*
- Convulsiones
- Suicidio
- Tasas de ausentismo
- Insuficiencia coronaria
- Concepción (fertilización in vitro)
- *Nacimiento*
- Menstruación
- Cirugía y supervivencia del cáncer de mama
- Resultado postoperatorio (general)
- Cólico renal
- Admisiones ambulatorias (generales)
- *Accidentes automovilísticos*

En este estudio revisaremos nuevamente algunos de estos puntos. Concretamnete: violencia con armas, nacimientos, defunciones y accidentes.

#### _Lunar cycle in homicides: a population-based time series study in Finland_
<small>Author: Simo Näyhä</small>
En este artículo ([Lunar cycle in homicides: a population-based time series study in Finland][monnHomicideRateFinland]) se estudian los homicidios, también en Finlandia, durante un período extenso: 6808 homicidios cometidos entre 1961 y 2014, desglosando el ciclo sideral, sinódico, perigeo y apogeo... Con un curioso resultado: es uno de los pocos que presenta una correlación entre la Luna Llena y, y aquí está la sorpresa, una disminución de los homicidios. Lo que es totalmente contrario a la creencia popular, instigada en parte por los medios, de que durante la Luna Llena aumentan los actos violentos. Según este estudio, si ello existe, es al contrario (también hay que decir que se trata de Finalndia... O:)).

#### CLUE App: _El mito de las fases lunares y la menstruación_
Hablando de regla, aplicaciones y estudios, está claro que en cuanto hubo datos suficientes, científicos y curiosos con acceso a CLUE y su estudio con 1,5 millones de mujeresos datos de millones de mujeres se lanzaron a la búsqueda de la confirmación o refutación del gran mito. De entre las empresas más conocidas de hace unos años está _Clue_. Y en el blog de la empresa publicarion, en 2017, a tres años de su lanzamiento en **Android** y cuatro en iOS, un artículo para dar respuesta a las muchas peticiones sobre el tema, más específicamente, añadir un Calendario Lunar a la aplicación.

El artículo se titula [_El mito de las fases lunares y la menstruación_][CLueArticle]. En él, básicamente, se desmiente definitivamente (?) cualquier relación causal o siquiera correlación entre nuestro satélite y la regla. Hicieron esto con los datos de 1.5 millones de mujeres. El resumen es este sencillo gráfico:

![ClueHistogram]
<small>Fuente: [_HelloClue_](https://helloclue.com/articles/</small>

Quizá el hecho de que _Clue_ incluya en este artículo la coincidencia del ciclo sinódico lunar (es decir, de las fases lunares) que es de 29,5 días con la media mundial, según sus datos, de la duración del ciclo en 29 días nos dé una idea de que hay más correlación que causalidad.

### _Influencia lunar en cultivos, animales y ser humano - Dialnet_
En el agregador de publicaciones científicas [Dialnet] encontramos un interesante estudio comparativo y experimental sobre la Luna y los cultivos, realizado en Centroamérica, concretamente en Nicaragua (sic), utilizando el maíz (de variedad NB6) como objeto del experimento, consultando a agricultores de varias etnias (indígenas misquitos, criollos y mestizos) para determinar las diferentes creencias sobre el tema.

Resumiendo el artículo, nadie siembra en Luna Nueva y la gran mayoría (91%) lo hace en Luna Llena o en Cuarto Creciente. Sin embargo, el experimento _in situ_ muestra datos diametralmente opuestos:

La germinación fue significativamente alta en las semillas plantadas en Luna Nueva y Cuarto Creciente, y extremadamente bajas las plantadas en Luna Llena. Lo mismo para la altura de las plantas y el diámetro de los tallos. Según el estudio, el análisis de separación de medias Tukey arroja un valor de p=0.011, lo que indica una alta relevancia entre las fases lunares y el crecimiento del maíz... contrario a la creencia popular. Datos similares se dieron en un estiudio sobre la papaya en 2001, según apuntan los investigadores.

Curiosamente (en realidad no), el crecimiento de las hojas no se vio afectado por la fase de la siembra.

Otro punto quizá más importante, es la afectación de enfermedades, plagas e insectos a las plantas. Pese a que la Luna Llena presenta la menor germinación y crecimiento, tanto la siembra durante el Cuarto Creciente como la Luna Llena presentan una mayor resistencia a enfermedades y ataques de insectos, siendo en cambio el grupo de Luna Nueva el único afectado por la "mancha de café", y el Cuarto Menguante el único afectado a los 60 días de la plantación en el segundo grupo.
Resumiendo el resto del estudio, el único otro dato significativo se dio en el peso de las mazorcas, pero el análisis estadístico dio un valor de p=0.19 y por tanto no resulta significativo.

La conclusión del estudio (y de otros que cita este mismo) es que sí hay relación entre las fases lunares y el crecimiento del maíz, pero que este es justamente contrario a la creencia popular. Pero advierte que son muchos los factores que influyen en el crecimiento y salud de las plantas, como el sol, lluvias, abono y otros cuidados.

### En resumen...
Sin embargo, como decía, sigue siendo un campo de estudio: hemos oído en series y películas la influencia de la luna Llena en el aumento de la violencia, sea doméstica, callejera, aumento de la criminalidad, etc. Y aunque parezca _obvio_ que la Luna no puede tener una influencia real, en realidad se estudian estas correlaciones en busca de información que confirme o refute estas hipótesis. A veces por diversión, curiosodad o por la búsqueda de un elemento externo que explique el comportamiento.

## Metodología
Análisis gráfico en busca de correlaciones que puedan hacer pensar en una relación de causa y efecto, con base al número de ocurrencias de diversos incidentes: nacimientos, muertes, accidentes y violencia.Aun así, el uso de Pandas para la creación de las tablas necesarias para la visualización con **[Flourish]** se hizo conveniente una vez los CSV estaban listos. Así pues:

- navegador web: Descarga de los ficheros CSV / XLSx
- Vim, ModernCSV y VSCodium para la "limpieza" de los CSV: verificar que estén los datos, normalizar algunos valores, eliminar columnas irrelevantes.
- MariaDB para la tabulación de los CSV, así com para incluir en los mismos las fases lunares correspondientes a las fechas de los eventos.
- Python + Pandas + VSCodium (iPyNoteBook) para la preparación de las tablas (en CSV) a utilizar para la visualización.
- VSCode, HackMD y Vim para la realización de la presente documentación y parte de la presentación
- [Canva] y [Flourish] para la presentación

## Los datos
Resulta un poco complicado obtener fuentes de datos con frecuencia diaria o, como mucho, semanal. Esto es necesario porque las fases de la Luna suelen ser 4 u 8 y duran entre 3 y 4 días, por lo que los datos deben poder dividirse en esos rangos de tiempo.

### Calendario de fases lunares
Para la relación entre las fechas y las fases lunares, he creado una tabla (primero un CSV con Python) con la fecha (entre 2000 y 2014), el _emoji_ de la fase lunar correspondiente, un índice numérico para la fase lunar (0 para la 🌑 Luna Nueva, 4 para la 🌕 Luna Llena hasta el 7 para la 🌘 Luna Menguante) y el nombre de dicha fase.

```SQL
INSERT INTO moon_phase
     VALUES
    (0, '🌑', 'Luna Nueva',       'New Moon'),
    (1, '🌒', 'Luna Creciente',   'Waxing Crescent Moon'),
    (2, '🌓', 'Cuarto Creciente', 'First Quarter Moon'),
    (3, '🌔', 'Gibosa Creciente', 'Waxing Gibbous Moon'),
    (4, '🌕', 'Luna Llena',       'Full Moon'),
    (5, '🌖', 'Gibosa Menguante', 'Waning Gibbous Moon'),
    (6, '🌗', 'Cuarto Menguante', 'Last Quarter Moon'),
    (7, '🌘', 'Luna Menguante',   'Waning Crescent Moon');
```

De esta forma se puede relacionar la fecha de la tabla de hechos con la fase lunar de dicha fecha. También es posible calcular la iluminación de la Luna (la intensidad de la luz reflejada, por superficie, fase y distancia), pero supondría un trabajo excesivo para una fase preliminar: si se encontrase alguna relación causal, un estudio en mayor profundidad sí tendría en cuenta este dato, así como la distancia Tierra-Luna.

### Datos recopilados y fuentes
Quizá podríamos disponer de más fuentes con más tiempo de búsqueda.

Intenté localizar información sobre divorcios con base diaria o semanal, pero lo más que se encuentra son mensuales y normalmente trimestrales, por lo que no resultan útiles para este estudio.

Por ahora se queda en los siguientes:

#### Institut D'EStadística de CATalunya (IDESCAT)
He encontrado algunos datos de eventos humanos en el [IDESCAT], enconcreto:

- Defunciones diarias
- Nacimientos diarios

He bajado los datos de 2015 a 2023 (2024 no está disponible), aunque seguramente la serie la haré desde 2018 o 2019, más que nada por la interrupción del COVID-19.

#### Instituto Nacional de Estadñistica (INE)
Desde la página eBase encontré datos de muertes semanales en el estado español en el [INE].
Está por AÑO|SEMANADELAÑO, no por día de la semana del año.

- Muertes semanales

#### OpenData BCN y Madrid
De las webs institucionales de ambas ciudades, he podido acceder al portal de datos abiertos y bajra los registros diarioes de:

- Accidentes viarios de Barcelona (2018-24)
- Accidentalidad de Madrid (2018-2024)
- Multas de tráfico en Barcelona (2018-2024)

Que son también eventos humanos y en cierta forma posibles candidatos a esa "influencia lunática".

#### Data.World
Una web con muchos datasets interesantes. De ella hemos extraído los datos relevantes de los _"mass shootings"_ en los EUA desde 2006. A esta tabla le hemos añadido la fase lunar para analizar la correlación:

```python
import pandas as pd
import ephem
from datetime import datetime

# Load the dataset
df = pd.read_csv('data/DATA.WORLD-mass_killing_incidents_public.csv')

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Function to calculate moon phase
def calculate_moon_phase(row):
    observer = ephem.Observer()
    observer.lat = str(row['latitude'])
    observer.lon = str(row['longitude'])
    observer.date = row['date']
    moon = ephem.Moon()
    moon.compute(observer)
    return moon.phase

# Apply the function to each row
df['moon_phase'] = df.apply(calculate_moon_phase, axis=1)

# Save the updated dataframe
df.to_csv('data/mass_killing_incidents_with_moon_phase.csv', index=False)

```

## Presentación

[Presentación con Canva + Flourich](https://www.canva.com/design/DAG2IWPMA0E/Y0F-nu_COAoCRuk3WsUoJQ/edit?utm_content=DAG2IWPMA0E&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)