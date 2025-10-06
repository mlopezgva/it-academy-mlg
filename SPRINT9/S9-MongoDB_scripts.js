// Create DB
use Entertainment

// Create and populate "tables" (Collections):
var myCollections = ['theaters', 'comments', 'users', 'movies', 'sessions']

myCollections.forEach(csv => {
    let flines = fs.readFileSync(csv+".json", 'utf-8').split("\n")
    flines.forEach(line => {
        if (line.trim() != '')
            db[csv].insertOne(EJSON.parse(line))
    })
})

// N1E1:

 //A. Muestra los dos primeros comentarios
// Estos son los dos primeros de la base de datos.
db.comments.find().limit(2)

// Y estos, los primeros, por fecha de creación:
db.comments.find().sort(date: 1).limit(2)

// B. Usuarios registrados?
db.users.countDocuments()

// C. Cines en California?
db.theaters.countDocuments({"location.address.state":"CA"})

// D. Primer usuario registrado
db.users.find().limit(1)

// E. Cuántas películas de comedia hay?
db.movies.countDocuments({genres: "comedy"})

// N1E2: Películas de 1932, solo dramas O en francés
db.movies.find(
    {
        year: 1932,
        $or: [
            {languages: /french/i},
            {genres: /drama/i}
        ]
    },
    { // "columnas" a mostrar (o no: `0`)
        title: 1,
        year: 1,
        genres: 1,
        languages: 1,
        _id: 0
    }
)

// Otra opción:
mov1932DramaOrFrench = db.movies
                     .find({
                         year: 1932,
                         $or: [{languages: /french/i},
                               {genres: /drama/i}]
                       },
                       {title: 1, year: 1, genres: 1, languages: 1, _id: 0}
                     )
                     .toArray()
console.table(mov1932DramaOrFrench)
/*
┌─────────┬─────────────────────────────────────┬───────────────────────────────────────────────────────┬──────┬─────────────────────────────────────┐
│ (index) │ title                               │ languages                                             │ year │ genres                              │
├─────────┼─────────────────────────────────────┼───────────────────────────────────────────────────────┼──────┼─────────────────────────────────────┤
│ 0       │ 'The Blood of a Poet'               │ [ 'French' ]                                          │ 1932 │                                     │
│ 1       │ 'The Blue Light'                    │ [ 'German', 'Italian' ]                               │ 1932 │ [ 'Drama', 'Fantasy', 'Mystery' ]   │
│ 2       │ 'Broken Lullaby'                    │ [ 'English' ]                                         │ 1932 │ [ 'Drama' ]                         │
│ 3       │ 'The Crowd Roars'                   │ [ 'English' ]                                         │ 1932 │ [ 'Drama', 'Action' ]               │
│ 4       │ 'A Farewell to Arms'                │ [ 'English' ]                                         │ 1932 │ [ 'Drama', 'Romance', 'War' ]       │
│ 5       │ 'Forbidden'                         │ [ 'English', 'French' ]                               │ 1932 │ [ 'Drama', 'Romance' ]              │
│ 6       │ 'Freaks'                            │ [ 'English', 'German', 'French' ]                     │ 1932 │ [ 'Drama', 'Horror' ]               │
│ 7       │ 'Grand Hotel'                       │ [ 'English', 'Russian' ]                              │ 1932 │ [ 'Drama', 'Romance' ]              │
│ 8       │ 'I Am a Fugitive from a Chain Gang' │ [ 'English' ]                                         │ 1932 │ [ 'Crime', 'Drama', 'Film-Noir' ]   │
│ 9       │ 'The Mummy'                         │ [ 'English', 'Arabic', 'French' ]                     │ 1932 │ [ 'Horror' ]                        │
│ 10      │ 'Payment Deferred'                  │ [ 'English' ]                                         │ 1932 │ [ 'Crime', 'Drama' ]                │
│ 11      │ 'The Red Head'                      │ [ 'French' ]                                          │ 1932 │ [ 'Drama' ]                         │
│ 12      │ 'Red Dust'                          │ [ 'English' ]                                         │ 1932 │ [ 'Drama', 'Romance' ]              │
│ 13      │ 'Scarface'                          │ [ 'English' ]                                         │ 1932 │ [ 'Action', 'Crime', 'Drama' ]      │
│ 14      │ 'Shanghai Express'                  │ [ 'English', 'French', 'Cantonese', ... 1 more item ] │ 1932 │ [ 'Adventure', 'Drama', 'Romance' ] │
│ 15      │ "Smilin' Through"                   │ [ 'English' ]                                         │ 1932 │ [ 'Drama', 'Romance' ]              │
│ 16      │ 'Two Seconds'                       │ [ 'English' ]                                         │ 1932 │ [ 'Drama', 'Thriller' ]             │
│ 17      │ 'I Was Born, But...'                │                                                       │ 1932 │ [ 'Comedy', 'Drama' ]               │
└─────────┴─────────────────────────────────────┴───────────────────────────────────────────────────────┴──────┴─────────────────────────────────────┘
*/


// N1E3: Películas USA entre 2012 y 2014 con entre 5 y 9 premios

// Hay 422 registros:
db.movies.countDocuments({
    year:{$gte:2012, $lt:2015},
    "awards.wins":{$gte:5, $lte:9}
})

// Mostremos solo los 20 primeros resultados...
console.table(
    db.movies
      .find(
        {  year:{$gte:2012, $lt:2015},
           "awards.wins":{$gte:5, $lte:9}},
        {title: 1, "awards.wins":1, year:1, _id: 0})
      .limit(20)
      .toArray()
    )
/*
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
└─────────┴──────┴────────────────────────────────────┴─────────────┘
*/

// N2E1: comentarios de usuarios con dominio `@gameofthron.es`
db.comments.countDocuments({email:/gameofthron.es/i})

// N2E2: cantidad de cines en cada C.P. de Washington, D.C.
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

// Como extra, lista de los usuarios con el domino `gameofthron.es` y cantidad de comentarios:
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

/*
┌─────────┬───────────────────────────────────────────────────────────────────────────┬───────┐
│ (index) │ _id                                                                       │ count │
├─────────┼───────────────────────────────────────────────────────────────────────────┼───────┤
│ 0       │ { name: 'Mace Tyrell', email: 'roger_ashton-griffiths@gameofthron.es' }   │ 331   │
│ 1       │ { name: 'Missandei', email: 'nathalie_emmanuel@gameofthron.es' }          │ 327   │
│ 2       │ { name: 'The High Sparrow', email: 'jonathan_pryce@gameofthron.es' }      │ 315   │
│ 3       │ { name: 'Sansa Stark', email: 'sophie_turner@gameofthron.es' }            │ 308   │
│ 4       │ { name: 'Rodrik Cassel', email: 'ron_donachie@gameofthron.es' }           │ 305   │
│ 5       │ { name: 'Thoros of Myr', email: 'paul_kaye@gameofthron.es' }              │ 304   │
│ 6       │ { name: 'Brienne of Tarth', email: 'gwendoline_christie@gameofthron.es' } │ 302   │
│ 7       │ { name: 'Qyburn', email: 'anton_lesser@gameofthron.es' }                  │ 295   │
│ 8       │ { name: 'Arya Stark', email: 'maisie_williams@gameofthron.es' }           │ 295   │
│ 9       │ { name: 'Beric Dondarrion', email: 'richard_dormer@gameofthron.es' }      │ 293   │
└─────────┴───────────────────────────────────────────────────────────────────────────┴───────┘
*/

// N3E1: Películas de John Landis con puntuación entre 7.5 y 8
landisMovies = db.movies.find({
        directors: /john landis/i,
        "imdb.rating": {$gte: 7.5, $lte: 8}
    },
    {title:1, directors: 1, "imdb.rating": 1, _id: 0}
).toArray()

console.table(landisMovies)
/*
┌─────────┬─────────────────┬──────────────────────────────────┬───────────────────┐
│ (index) │ imdb            │ title                            │ directors         │
├─────────┼─────────────────┼──────────────────────────────────┼───────────────────┤
│ 0       │ { rating: 7.6 } │ 'Animal House'                   │ [ 'John Landis' ] │
│ 1       │ { rating: 7.9 } │ 'The Blues Brothers'             │ [ 'John Landis' ] │
│ 2       │ { rating: 7.6 } │ 'An American Werewolf in London' │ [ 'John Landis' ] │
│ 3       │ { rating: 7.5 } │ 'Trading Places'                 │ [ 'John Landis' ] │
└─────────┴─────────────────┴──────────────────────────────────┴───────────────────┘
*/

// N3E2: Preparar los datos para crear la visualización geográfica de los cines
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
