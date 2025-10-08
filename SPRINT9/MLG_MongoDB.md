SPRINT 9 - MongoDB
===

> _Treballarem amb una base de dades que conté col·leccions relacionades amb una aplicació d'entreteniment cinematogràfic:_
> 
> - `users`: Emmagatzema informació d'usuaris/es, incloent-hi noms, emails i contrasenyes xifrades.
> - `theatres`: Conté dades de cinemes, com ID, ubicació (direcció i coordenades geogràfiques).
> - `sessions`: Guarda sessions d'usuari, incloent-hi ID d'usuari i tokens JWT per a l'autenticació.
> - `movies`: Inclou detalls de pel·lícules, com a trama, gèneres, durada, elenc, comentaris, any de llançament, directors, classificació i premis.
> - `comments`: Emmagatzema comentaris d'usuaris/es sobre pel·lícules, amb informació de l'autor/a del comentari, ID de la pel·lícula, text del comentari i la data.
> 
> Duràs a terme algunes consultes que et demana el client/a, el qual està mesurant si seràs capaç o no de fer-te càrrec de la part analítica del projecte vinculat amb la seva base de dades.

Nivell 1
---
> _Crea una base de dades amb MongoDB utilitzant com a col·leccions els arxius adjunts._

He creado un servidor MongoDB usando docker, así que lo que he hecho es levantarlo y conectar.

```shell
❯ docker compose up -d

❯ mongosh localhost:27018
Current Mongosh Log ID: 68d93ab0f96e8c102ace5f46
Connecting to:          mongodb://localhost:27018/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.8
Using MongoDB:          8.0.14
Using Mongosh:          2.5.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

test> use Entertainment
switched to db Entertainment
```

Después de esto, he importado cada uno de los ficheros, leyendo el fichero, dividiendo cada línea, pues he visto que cada línea es un objeto JSON, y cada línea la he interpretado (`parse()`) y añadido a la colección. Puesto que la colección ("tabla") se crea si no existe (un peligro si uno se equivoca al teclear, algo que me pasa mucho), solo había que iterar sobre cada línea del fichero:

```jsx
Entertainment> fs.readFileSync('users.json', 'utf-8')
				 .split('\n')
                 .forEach(line => {
                 	if (line.trim()!='')
                    	db.users.insertOne(EJSON.parse(line));
                    })

Entertainment> fs.readFileSync('theaters.json', 'utf-8')
				 .split('\n')
                 .forEach(line => {
                 	if (line.trim()!='')
                    	db.theaters.insertOne(EJSON.parse(line));
                    })

Entertainment> fs.readFileSync('sessions.json', 'utf-8')
				 .split('\n')
                 .forEach(line => {
                 	if (line.trim()!='')
                    	db.sessions.insertOne(EJSON.parse(line));
                    })

Entertainment> fs.readFileSync('movies.json', 'utf-8')
				 .split('\n')
                 .forEach(line => {
                 	if (line.trim()!='')
                    	db.movies.insertOne(EJSON.parse(line));
                    })

Entertainment> fs.readFileSync('comments.json', 'utf-8')
				 .split('\n')
                 .forEach(line => {
                 	if (line.trim()!='')
                    	db.comments.insertOne(EJSON.parse(line));
                    })

Entertainment> db.stats()
{
  db: 'Entertainment',
  collections: Long('5'),
  views: Long('0'),
  objects: Long('151005'),
  avgObjSize: 357.2854607463329,
  dataSize: 53951891,
  storageSize: 35426304,
  indexes: Long('5'),
  indexSize: 2691072,
  totalSize: 38117376,
  scaleFactor: Long('1'),
  fsUsedSize: 300511469568,
  fsTotalSize: 501380800512,
  ok: 1
}

Entertainment> db.getCollectionNames()
                 .forEach(col => console.log(
                     col,
                     "\n\tSize (in KiB):", db[col].dataSize()/1024,
                     "\n\tDocuments (records):", db[col].countDocuments()
                 ))
sessions 
        Size (in KiB): 0.5703125 
        Documents (records): 3
movies 
        Size (in KiB): 37243.203125 
        Documents (records): 47079
comments 
        Size (in KiB): 15039.490234375 
        Documents (records): 100609
theaters 
        Size (in KiB): 375.2548828125 
        Documents (records): 3129
users 
        Size (in KiB): 28.875 
        Documents (records): 185
```

Pensándolo bien, se podría haber utilizado esa idea del último paso para ejecutar los "import" del inicio. Algo así como esto (sin probar):

```jsx
var myCollections = ['theaters', 'comments', 'users', 'movies', 'sessions']

myCollections.forEach(csv => {
    let flines = fs.readFileSync(csv+".json", 'utf-8').split("\n")
    flines.forEach(line => {
        if (line.trim() != '')
            db[csv].insertOne(EJSON.parse(line))
    })
})
```

#### Oh! ¡Pues sí que ha funcionado!

```jsx
Entertainment> use Prueba
switched to db Prueba
Prueba> var myCollections = [
    'theaters', 'comments',
    'users', 'movies', 'sessions'
]

Prueba> myCollections.forEach(csv => {
          let flines = fs.readFileSync(csv+".json", 'utf-8').split("\n")
          flines.forEach(line => {
             if (line.trim() != '')
               db[csv].insertOne(EJSON.parse(line))
          })
      })

Prueba> db.getCollectionNames()
                 .forEach(col => console.log(
                    col,
                    "\n\tSize (in KiB):", db[col].dataSize()/1024,
                    "\n\tDocuments (records):", db[col].countDocuments()
                ))
movies 
        Size (in KiB): 36737.4609375 
        Documents (records): 23539
theaters 
        Size (in KiB): 341.6318359375 
        Documents (records): 1564
sessions 
        Size (in KiB): 0.52734375 
        Documents (records): 1
comments 
        Size (in KiB): 13958.71875 
        Documents (records): 50304
users 
        Size (in KiB): 28.875 
        Documents (records): 185
```

Captura:

![create tables](https://hackmd.io/_uploads/SJSgIfOnxl.png)

### Exercici 1
Consultes bàsiques.

#### S9N1E1`a`: Mostra els 2 primers comentaris que hi ha en la base de dades.

Estos sson los dos primeros de la base de datos.
```javascript
db.comments.find().limit(2)
```

![image](https://hackmd.io/_uploads/rygIIG_2xg.png)

Y estos, los primeros, por fecha de creación:

```javascript
db.comments.find().sort(date: 1).limit(2)
```

![image](https://hackmd.io/_uploads/SkEwUfdhxx.png)

Vale, al final he instalado el MongoDB Compass... Qué complicación para hacer cosas simples. Sobre todo porque es el que hará el N3E2[^note1]. Para todo lo demás, complica más que ayuda.

[^note1]: Y para nada: no he podido usar ***MongoDB Compass*** para crear el mapa que pide. He perdido como una hora, o dos, de tiempo intentando resolverlo.

En fin, captura:

![image](https://hackmd.io/_uploads/SkcuLMdnll.png)

#### S9N1E1`b`: Quants usuaris tenim registrats?

```javascript
db.users.countDocuments()
```

![image](https://hackmd.io/_uploads/HJyqLfdhlx.png)

***Compass***: como no sea esto:

![image](https://hackmd.io/_uploads/HJB9UMOhxg.png)

no se me ocurre qué más pueda ser. :worried: 

#### S9N1E1`c`: Quants cinemes hi ha en l'estat de Califòrnia?

```javascript
db.theaters.countDocuments({"location.address.state":"CA"})
```

![image](https://hackmd.io/_uploads/BySoUfu2lg.png)

Compass:

![image](https://hackmd.io/_uploads/rJ73Ifu2ge.png)

#### S9N1E1`d`: Quin va ser el primer usuari/ària en registrar-se?
No hay un campo / clave para la fecha de alta. Solo podemos asumir que el primer elemento guardado sea el primero en registrarse. En cuyo caso:

```javascript
db.user.find().limit(1)
```

Compass:  
![image](https://hackmd.io/_uploads/rk3TIGdhgx.png)

> Pero eso no significa que ese sea el primer usuario registrado. No existe tal información, que haya visto.

#### S9N1E1`e`: Quantes pel·lícules de comèdia hi ha en la nostra base de dades?

```javascript
db.movies.countDocuments({genres: "comedy"})
7024
```

or

```javascript
db.movies.countDocuments({genres: {$in: ["comedy"]}})
7024
```

o, para buscar sin saber si está en mayúsculas o minúsculas (porque si busco "comedy" con los métdos de arriba, devuelve `0`), se puede usar una regex:

```javascript
db.movies.countDocuments({genres: /comedy/i})
7024
```

![image](https://hackmd.io/_uploads/SJ0CLfdnxg.png)

Compass:

![image](https://hackmd.io/_uploads/Sk3yvfd2xe.png)

### Exercici 2
> Mostra'm tots els documents de les pel·lícules produïdes en 1932, però que el gènere sigui drama o estiguin en francès.

```javascript
db.movies.find(
    {
        year: 1932,
        $or: [
            {languages: /french/i},
            {genres: /drama/i}
        ]
    },
    {
        title: 1,
        year: 1,
        genres: 1,
        languages: 1,
        _id: 0
    }
)
```

Compass:

![image](https://hackmd.io/_uploads/By1MvG_nge.png)

O, más sucinto:

```javascript
mov1932DramaOrFrench = db.movies
                     .find({
                         year: 1932,
                         $or: [{languages: /french/i},
                               {genres: /drama/i}]
                       },
                       {title: 1, year: 1, genres: 1, languages: 1, _id: 0}
                     )
                     .toArray()
```

Y, para ver mejor los resultados, con ese `.toArray()` podemos llamar a un método de `mongosh` que muestra el resultado en una tabla:

![image](https://hackmd.io/_uploads/r1WHPzd2gg.png)

### Exercici 3
Mostra'm tots els documents de pel·lícules estatunidenques que tinguin entre 5 i 9 premis que van ser produïdes entre 2012 i 2014.

Aquí toca, de nuevo, mezclar ANDs y ORs... Producción entre 2012-14, esto es un rango, igual que la cantidad de premios (que veo que está en `awards.wins`). Será más sencillo que el anterior, en realidad:

```javascript
db.movies.find({
    year:{$gte:2012, $lt:2015},
    "awards.wins":{$gte:5, $lte:9}
})
```

Claro que esto muestra una lista enorme de todo, porque

```javascript
Entertainment> db.movies.countDocuments({
    year:{$gte:2012, $lt:2015},
    "awards.wins":{$gte:5, $lte:9}
})

422
```

son muchos registros. Así que filtraré los 5 primeros, que ya es, solo para mostrar el resultado, como pide el enunciado. Pero no creo necesario volvar los datos de los 422 resgistros... ¿no?

```javascript
Entertainment> console.table(
    db.movies
      .find(
        {  year:{$gte:2012, $lt:2015},
           "awards.wins":{$gte:5, $lte:9}},
        {title: 1, "awards.wins":1, year:1, _id: 0})
      .limit(20)
      .toArray())

┌─────────┬──────┬────────────────────────────────────┬─────────────┐
│ (index) │ year │ title                              │ awards      │
├─────────┼──────┼────────────────────────────────────┼─────────────┤
│ 0       │ 2013 │ 'The Secret Life of Walter Mitty'  │ { wins: 6 } │
│ 1       │ 2013 │ 'The Croods'                       │ { wins: 8 } │
│ 2       │ 2013 │ 'The Book Thief'                   │ { wins: 6 } │
│ 3       │ 2013 │ 'World War Z'                      │ { wins: 5 } │
│ 4       │ 2014 │ 'Godzilla'                         │ { wins: 7 } │
│ 5       │ 2013 │ 'Mr Hockey: The Gordie Howe Story' │ { wins: 5 } │
│ 6       │ 2012 │ 'Hitchcock'                        │ { wins: 6 } │
│ 7       │ 2013 │ 'Krrish 3'                         │ { wins: 9 } │
│ 8       │ 2013 │ 'Lone Survivor'                    │ { wins: 7 } │
│ 9       │ 2013 │ 'One Chance'                       │ { wins: 5 } │
│ 10      │ 2013 │ 'The Lone Ranger'                  │ { wins: 6 } │
│ 11      │ 2013 │ "The World's End"                  │ { wins: 7 } │
│ 12      │ 2012 │ "That's My Boy"                    │ { wins: 6 } │
│ 13      │ 2012 │ '21 Jump Street'                   │ { wins: 8 } │
│ 14      │ 2012 │ 'Mariachi Gringo'                  │ { wins: 5 } │
│ 15      │ 2013 │ 'Kill Your Darlings'               │ { wins: 5 } │
│ 16      │ 2012 │ 'The Lucky One'                    │ { wins: 6 } │
│ 17      │ 2013 │ 'Particle Fever'                   │ { wins: 5 } │
│ 18      │ 2012 │ 'Thursday Till Sunday'             │ { wins: 8 } │
│ 19      │ 2013 │ 'Star Trek Into Darkness'          │ { wins: 9 } │
│ ......  │ .... │ .........................          │ ........... │
└─────────┴──────┴────────────────────────────────────┴─────────────┘
```

Aquí está la captura del terminal. Primero los datos en "crudo" (JSON) y luego en forma de tabla, usando, de nuevo, `console.table()`:

![image](https://hackmd.io/_uploads/B1AwDfungg.png)

Compass:

![image](https://hackmd.io/_uploads/rJ6uPGuhgg.png)

Nivell 2
---
### S9N2E1 - Exercici 1
> Compte quants comentaris escriu un usuari/ària que utilitza "GAMEOFTHRON.ES" com a domini de correu electrònic.

Aquí tenemos que usar un filtro regex (supongo que hay un "in_str" o equivalente, pero las regex son "nativas" y válidas) para el dominio. Como guarda el e-mail en la misma colección (posiblemente para permitir mś de un e-mail al mismo usuario, por el motivo que sea), no es necesario hacer ningún "join".

```javascript
db.comments.countDocuments({email:/gameofthron.es/i})
```

Y vemos que no tiene vida, porque ha escrito nada menos que

    Entertainment> db.comments.countDocuments({email:/gameofthron.es/i})
    22841

comentarios. Casi ná :tired_face: 

Compass:

![image](https://hackmd.io/_uploads/HJPsDfuheg.png)

### S9N2E2 - Exercici 2
> Quants cinemes hi ha en cada codi postal situats dins de l'estat Washington D. C. (DC)?

Bueno, más agregación, pero además hay que filtrar antes. Esto se hace con `$match`:

```javascript
db.theaters.aggregate([
    {$match: {"location.address.state": "DC"}},
    {$group: {
        _id: {
            state:   "$location.address.state",
            zipcode: "$location.address.zipcode"
        },
        theaters:{$sum:1}}
    }
])
```

Resultado:

```javascript
[
  { _id: { state: 'DC', zipcode: '20010' }, theaters: 1 },
  { _id: { state: 'DC', zipcode: '20016' }, theaters: 1 },
  { _id: { state: 'DC', zipcode: '20002' }, theaters: 1 }
]
```

Para comprobar el resultado:

```shell
Entertainment> db.theaters.countDocuments({"location.address.zipcode": '20010'})
1
Entertainment> db.theaters.countDocuments({"location.address.zipcode": '20016'})
1
Entertainment> db.theaters.countDocuments({"location.address.zipcode": '20002'})
1
```

![image](https://hackmd.io/_uploads/r16hwz_heg.png)

***Compass***: de nuevo, muy complejo para algo mucho más simple escribiendo en texto...

![image](https://hackmd.io/_uploads/r1l0Dfdngl.png)

Con la configuracíon de los "stages" (en texto, que lo otro ocupa mucho):

![image](https://hackmd.io/_uploads/ByhCvG_3ll.png)

### Bonus: top 10 `@gameofthorn.es` commenters
> Solo en mongosh / CLI

```javascript
console.table(
    db.comments
      .aggregate([
        {$match: {email: /@gameofthron\.es$/i}},     // just the domain
        {$group: {
          _id:   {name: "$name", email: "$email"}, // list name and email
          count: {$sum: 1}}},
        {$sort:  {count: -1}},  // reverse ordered (max first)
        {$limit: 10}            // only the Top 10
      ])
      .toArray()
)
```

Resultado:

![image](https://hackmd.io/_uploads/rksJ_M_ngg.png)

Nivell 3
---
### Exercici 1
> Troba totes les pel·lícules dirigides per John Landis amb una puntuació IMDb (Internet Movie Database) d'entre 7,5 i 8.

```javascript
db.movies.find({
        directors: /john landis/i,
        "imdb.rating": {$gte: 7.5, $lte: 8}
    },
    {title:1, directors: 1, "imdb.rating": 1, _id: 0}
})
```

Captura:

![image](https://hackmd.io/_uploads/SkPL6WW6ge.png)

Para seguir con la tradición, mostramos la más conocida y legible tabla :wink: :

```javascript
landisMovies = db.movies.find({
        directors: /john landis/i,
        "imdb.rating": {$gte: 7.5, $lte: 8}
    },
    {title:1, directors: 1, "imdb.rating": 1, _id: 0}
}).toArray()

console.table(landisMovies)
```

![image](https://hackmd.io/_uploads/S1kZAW-pxx.png)

Y Compass:

![image](https://hackmd.io/_uploads/SkytR-ZTex.png)

Veo que podría haber mostrado en los anteriores resultados, únicamente los títulos, o nombres, etc. En fin, considérense corregidos.

### Exercici 2
> Mostra en un mapa la ubicació de tots els teatres de la base de dades.

No he podido hacerlo con _Compass_ porque no me sale la opción de "Map". He intentado reinstalar, revisar la configuración, etc., nada. Así que me he decidido por otra opción, *on-line*, para mostrar los puntos del mapa: [GeoJSON.io](http://geojson.io).

Para ello, he tenido que exportar los datos utilizando `mongosh` para ejecutrar un script que altere los datos de `location.geo.coordinates` a algo que se espera GeoJSON.

Este fue el código:

```javascript
const raw = db.theaters
              .find({}, {"location.geo": 1, "_id": 0})
              .toArray();
const features = raw.map(doc => ({
                  type: "Feature",
                  geometry: doc.location.geo,
                  properties: {}
                }));
const geojson = {
  type: "FeatureCollection",
  features: features
};

fs.writeFileSync("geodata.json", JSON.stringify(geojson, null, 2));
```

Esto deja los datos en el formato que espera la página web:

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -93.24565,
          44.85466
        ]
      },
      "properties": {}
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -76.512016,
          38.29697
        ]
      },
      "properties": {}
    },
// ... 1561 registros ...
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          -82.536293,
          35.442486
        ]
      },
      "properties": {}
    }
  ]
}
```

Y el resultado es este:

![geojson_S9N3E2](https://hackmd.io/_uploads/r1qEFMd3gg.jpg)
