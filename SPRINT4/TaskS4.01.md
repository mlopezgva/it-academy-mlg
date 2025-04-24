# SPRINT 4 - Task S4.01

## Nivell 1
Crear la base de dades.

### Exercici 0
Dissenyar l'esquema en estrella.

```sql
CREATE SCHEMA `mlg_sprint4`
      DEFAULT CHARACTER SET utf8
      COLLATE utf8_unicode_ci ;
```

He creat un nou esquema per separar-ho tot de l'anterior, encara que s'assembli.

#### Taules
Agafarem primer les taules "informatives" (dimensionals) i en llistem les columnes:

products:

    id,product_name,price,colour,weight,warehouse_id

users (uk,ca,usa...):

    id,name,surname,phone,email,birth_date,country,city,postal_code,address

companies:

    company_id,company_name,phone,email,country,website

Ara, la taula que té una relació amb les anteriors, que és la de CC:

credit_cards:

    id,user_id,iban,pan,pin,cvv,track1,track2,expiring_date

Com es pot veure, té una FK amb `users`.  
I, finalment, la taula "facts" que seria `transactions`:

transactions:

    id;card_id;business_id;timestamp;amount;declined;product_ids;user_id;lat;longitude

Com que sóc jo qui crea la DB i les taules, i m'agrada que la PK sigui `<taula>_id` i no només "`id`", els objectes estaran definits així:

<details>
  <summary><i>Codi PlantUML del diagrama ERD</i></summary>

```plantuml
hide methods
skinparam linetype ortho

entity "Product" as P {
    * product_id : numeric <<PK>>
    --
    + product_name : text
    price : money
    colour : text
    weight : decimal
    warehouse_id : text
}

entity "User" as U {
    * user_id : numeric <<PK>>
    --
    name : text
    surname : text
    phone : text
    email : text
    birth_date : date
    country : text
    city : text
    postal_code : text
    address : text
}

entity "Company" as C {
    * company_id : TEXT <<PK>>
    --
    company_name : TEXT  <<INDEX>>
    phone : text
    email : text
    country : text
    website : text
}

entity "Credit Card" as CC {
    * cc_id : numeric <<PK>> <<SERIAL>>
    * credit_card_id : text <<UNIQUE>>
    --
    + user_id : numeric <<FK>>
    iban : text
    pan : text(18)
    pin : text(4)
    cvv : text(3)
    track1 : text
    track2 : text
    expiring_date : date
}

entity "Transaction" as T {
    * transaction_id : text <<PK>>
    --
    * company_id : text <<FK>>
    * //user_id : numeric <<FK>>//
    * credit_card_id : 
    * product_ids : array
    ..
    * transction_time : timestamp
    * amount : money
    latitude : signed float
    longitude : signed float
    * declined : boolean
}

T ||-up-|| C
T ||--|| CC
T ||-le-{ P
T ||-ri-|| U : user_id

note top of U
    As an star schema, only
    one level must be used.
    So, user is linked to
    ""Transaction"" to avoid a
    second level with Credit Card.
end note

U --|{ CC : User may have\n one or more CCs  \n
```
</details>

![ER Sprint4](https://ptuml.hackmd.io/svg/XLHHJzim47xFhpZrQMEKYcqF4q98gEiaj0brev5uGAgkzj5O97PaEsKLtN_VsGuXAKNanSddB-VllhjpeIH1HRumqcNkGUaQBLPGAar-MnCOorjPHjehluNHt1hP23y2T327fmpuEO8weKibuGnqKv5L0ixFvpylBY9ZF8xBfuweiIAcUlhhuqxDFmIWCfgs4H6cD8tjSnv9hGlFY2IXAYmJY9OAqpXAPqVolnUvkICRjUQTLkRQzuJkotEDVQMuOAbzW2fKPHzOARPkAT47MbZQl1hjxRPF545gFxHn7ikbC79m04ffoRa3MKvDLQFUnaIdNQ8YeIdNnUnsSI3HPqwRNMGnxUhw--osPRwVw86K7cdbbAT3MYr9vM6ALYQzFS7YK5rukPdzkRhyrUfXNWon51pYfUfCow-lVkUp_POxLEyVppQe5Ug1zTtdXzDl7nEaEkXhGiHcyunyIOYtA1vE-u4YydbWszzQMQNNWuxe6REmg1qAhuoEnYmwN_pBpY3V_MBkbRnbTRaUmMJobXcJoLlUlfhmq81eBQOnFJdfYqmQlKgZmWitSbMt3An2dmo6l4JElObjxjHQauJxqc3ogpHw_URcKRW4mXqL9AwCAGbrC7C1kzsugSUx7KpJHtnjtqiQFy4ylLiLTdB-lVKaoxJXmdXJWxc7F1vpwO0RWfEmu4J1ZNyCHfT9UvYAaZPKGjKu3oiAWMIouyOSnx2WNBX97rYcDt5dDAZpY670ZM6dCLqq98oMRTn7vGlepSi9zug4e3BBSYxwxYbCpnc4Imugt4A16xhJKPbXn5XYWWEuqzb_)

Creem les taules:

```sql
CREATE TABLE IF NOT EXISTS product (
    product_id    INT           AUTO_INCREMENT PRIMARY KEY,
    product_name  TEXT          NOT NULL,
    price         DECIMAL(10,2) NOT NULL DEFAULT 0.0,
    colour        VARCHAR(10), -- 9 if alpha info comes up...
    weight        FLOAT         NOT NULL,
    warehouse_id  VARCHAR(8)    NOT NULL  -- 8 just in case
);

-- Prices have the money symbol ('`$`') in the CSV, so we have to edit
-- and remove it first from the file before importing

CREATE TABLE IF NOT EXISTS company (
    company_id    VARCHAR(12)   PRIMARY KEY,
    company_name  VARCHAR(150)  NOT NULL,
    phone         VARCHAR(24)   DEFAULT '',
    email         VARCHAR(100)  NOT NULL UNIQUE,
    country       VARCHAR(80)   NOT NULL COMMENT 'Max. official name length',
    website       VARCHAR(1024) DEFAULT ''
);

CREATE TABLE IF NOT EXISTS user (
    user_id     INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(50)  NOT NULL,
    surname     VARCHAR(50)  NOT NULL,
    phone       VARCHAR(24)  DEFAULT '',
    email       VARCHAR(100) NOT NULL UNIQUE,
    birthdate   DATE,
    country     VARCHAR(80)  NOT NULL,
    city        VARCHAR(80)  NOT NULL,
    postal_code VARCHAR(20)  NOT NULL,
    address     VARCHAR(200) DEFAULT ''
);

CREATE TABLE IF NOT EXISTS credit_card (
    cc_id           INT UNSIGNED AUTO_INCREMENT UNIQUE KEY,
    credit_card_id  VARCHAR(10)  PRIMARY KEY,
    user_id         INT UNSIGNED REFERENCES user(user_id),
    iban            CHAR(32)     NOT NULL,
    pan             VARCHAR(20)  NOT NULL UNIQUE KEY,
    pin             CHAR(4)      NOT NULL,
    cvv             CHAR(3)      NOT NULL,
    track1			VARCHAR(46)  NOT NULL,
    track2			VARCHAR(32)  NOT NULL,
    expiring_date   DATE         NOT NULL,
    INDEX cc_iban_idx (iban)
);

CREATE TABLE IF NOT EXISTS transaction (
    transaction_id  CHAR(36)      PRIMARY KEY,
    company_id      VARCHAR(12)   REFERENCES company(company_id),
    user_id         INT UNSIGNED  REFERENCES user(user_id),
    credit_card_id  VARCHAR(10)   REFERENCES credit_card(credit_card_id),
    product_ids     JSON          COMMENT 'With JSON should be easier to work with',
    transaction_ts  TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    amount          DECIMAL(10,2) NOT NULL DEFAULT 0.0,
    latitude        FLOAT SIGNED,
    longitude       FLOAT SIGNED,
    declined        BOOLEAN       NOT NULL DEFAULT TRUE
);
```

I amb això tindriem les taules llestes. Ara, hem d'introduïr les dades.

```sql
LOAD DATA
    LOCAL INFILE 'companies.csv'
     INTO TABLE company
         FIELDS TERMINATED BY ','
                OPTIONALLY ENCLOSED BY '"'
         IGNORE 1 LINES;

LOAD DATA
    LOCAL INFILE 'products.csv'
     INTO TABLE product
          FIELDS TERMINATED BY ','
                 OPTIONALLY ENCLOSED BY '"'
          IGNORE 1 LINES
          (product_id,product_name,@value,colour,weight,warehouse_id)
      SET price = REPLACE(@value, '$', '')
;

-- repeat it for each user_xxx.csv file changind the filename...
LOAD DATA LOCAL INFILE 'users_ca.csv'
     INTO TABLE `user`
          FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\r\n'
          IGNORE 1 LINES
          (user_id,name,surname,phone,email,@bdate,country,city,postal_code,address)
      SET birthdate = STR_TO_DATE(@bdate, '%b %d, %Y')
;

LOAD DATA LOCAL INFILE 'credit_cards.csv'
     INTO TABLE credit_card
          FIELDS TERMINATED BY ','
                 OPTIONALLY ENCLOSED BY '"'
          IGNORE 1 LINES
          (cc_id,credit_card_id,user_id,iban,pan,pin,cvv,track1,track2,@expire_date)
      SET expiring_date = CASE
            WHEN STR_TO_DATE(@expire_date, '%m/%d/%Y') IS NULL
            THEN '0000-00-00'  -- Or a default date, e.g., '1900-01-01'
            ELSE STR_TO_DATE(@expire_date, '%m/%d/%Y')
        END
;

LOAD DATA LOCAL INFILE 'transactions.csv'
     INTO TABLE transcation
          FIELDS TERMINATED BY ';'
                 OPTIONALLY ENCLOSED BY '"'
          IGNORE 1 LINES
          (transaction_id,credit_card_id,company_id,transaction_ts,amount,declined,@prods,user_id,latitude,longitude)
      SET product_ids = CONCAT('[', @prods, ']')
;

```

> [!CAUTION]
> Hi ha un problema: quan utilitzo el comandament `LOAD DATA INFILE '' INTO TABLE`...
> El client em retorna un error:
> 
> 'The MySQL server is running with the --secure-file-priv option so it cannot execute this statement'
> 
> 'Loading local data is disabled; this must be enabled on both the client and server sides'
> 
> No tinc permís per modificar la configuració del servidor... Per tant, hauré de fer, mentre es soluciona (o no) el problema, una transformació dels CSV a comandaments SQL.
> 
> ```sql
> INSERT INTO companies
>      VALUES
>       ('b-2222', 'Ac Fermentum Incorporated', '06 85 56 52 33', 'donec.porttitor.tellus@yahoo.net', 'Germany', 'https://instagram.com/site'
> ),
>     , ('b-2226', 'Magna A Neque Industries', '04 14 44 64 62', 'risus.donec.nibh@icloud.org', 'Australia', 'https://whatsapp.com/group/9')
>     ...
>     ;
> ```
> 
> Seria complicat de fer amb un editor normal, per això ho he fet amb vim. He creat els corresponents fitxers .sql (companies.sql, products.sql, etc.) per poder executar-los al client CLI utilitzant `source <fitxer.sql>`.
> 
> ```
> MySQL root@localhost:mlg_sprint4> source ./companies_mlg_s4.sql
> Query OK, 100 rows affected
> Time: 0.126s
> 
> MySQL root@localhost:mlg_sprint4> source ./products_mlg_s4.sql
> Query OK, 100 rows affected
> Time: 0.163s
> 
> etc.
> ```
> 
> Un cop editats els CSV i convertits en DML, executem tot i ja tenim les dades.

### Exercici 1
> Realitza una subconsulta que mostri tots els usuaris amb més de 30 transaccions utilitzant almenys 2 taules.

```sql
SELECT user_id
     , CONCAT(name, ' ', surname) AS `user`
     , COUNT(transaction_id) AS transaction_count
  FROM transaction AS t
  JOIN user        AS u USING(user_id)
 WHERE NOT declined
 GROUP BY user_id
HAVING COUNT(transaction_id) > 30
```

Sempre imaginant que qui reb l'informe no té interès pels IDs, mostrem el nom del client complet, a més del seu ID.

Resultat:

| user_id | user           | transaction_count |
|--------:|----------------|------------------:|
| 92      | Lynn Riddle    | 39                |
| 267     | Ocean Nelson   | 39                |
| 272     | Hedwig Gilbert | 38                |

També podem veure el total de transaccions *i* el total de transaccions amb èxit (que és el que mostra la taula anterior). Com que a MySQL els camps `BOOLEAN` són INT(1) i el valor `TRUE` és `1`, podem comptar les transaccions amb èxit sumant els valors de la columna `declined`... però és clar, si és `declined = TRUE` serien les fallides. Asixí que ho inverteixo amb `NOT declined` i hi faig el sumatori.

```sql
SELECT user_id
     , CONCAT(name, ' ', surname) AS `user`
     , COUNT(transaction_id) AS transaction_count
     , SUM(NOT declined)     AS successful
  FROM transaction AS t
  JOIN user        AS u USING(user_id)
 GROUP BY user_id
HAVING COUNT(transaction_id) > 30
```

| user_id | user           | transaction_count | successful |
|--------:|----------------|------------------:|-----------:|
| 92      | Lynn Riddle    | 39                | 39         |
| 275     | Kenyon Hartman | 48                | 24         |
| 272     | Hedwig Gilbert | 76                | 38         |
| 267     | Ocean Nelson   | 52                | 39         |

Podem veure que hi ha un més, però que té 24 transaccions amb èxit i per això no sortia a la taula anterior.

### Exercici 2

> Mostra la mitjana d'amount per IBAN de les targetes de crèdit a la companyia Donec Ltd, utilitza almenys 2 taules.

Si mirem la taula credit_card, no té una columna 'company_id' i, per tant, hem d'utilitzar la relació entre transaction + company + credit_card per determinar quines targetes són de la companyia esmentada.

```sql
SELECT iban
     , AVG(amount) AS spend_avg
  FROM transaction AS t
  JOIN credit_card AS cc USING(credit_card_id)
  JOIN company     AS c  USING(company_id)
 WHERE company_name = 'Donec Ltd'
   AND NOT declined   
```

| iban                      | spend_avg |
| ------------------------- | --------- |
| PT87806228135092429456346 | 42.820000 |

## Nivell 2
### Exercici 0
> Crea una nova taula que reflecteixi l'estat de les targetes de crèdit basat en si les últimes tres transaccions van ser declinades i genera la següent consulta:

Més que taula, una VIEW... Seria més pràctic, per què estaria sempre actualitzada.

```sql
CREATE OR REPLACE VIEW active_cc AS
-- O, si ha d'ésser una taula:
-- CREATE OR REPLACE TABLE active_cc AS
SELECT credit_card_id
     , iban, pan
     , (SELECT COUNT(declined)
          FROM `transaction` AS subt
         WHERE t.credit_card_id = subt.credit_card_id
         ORDER BY transaction_ts DESC
         LIMIT 3
         ) > 2 AS last_three_declined
  FROM transaction AS t
  JOIN credit_card AS cc USING(credit_card_id);
```

### Exercici 1

> Quantes targetes estan actives?

Si la TAULA / VIEW és correcta, serien 349 targetes actives:

```sql
SELECT CASE last_three_declined
            WHEN 1 THEN 'Yes'
            WHEN 0 THEN 'No'
       END AS Inactive_CC
     , COUNT(*)
  FROM active_cc
 GROUP BY last_three_declined;
```

| Inactive_CC | count |
| ----------- | -----:|
| Yes         |   238 |
| No          |   349 |

Però per respondre **exactament** l'enunciat:

```sql
SELECT COUNT(last_three_declined = 0) AS Active_CC
  FROM active_cc
 GROUP BY last_three_declined
 HAVING last_three_declined = 0;
```

Resultat:

| Active_CC |
|----------:|
| 349       |

## Nivell 3
### Exercici 0
> Crea una taula amb la qual puguem unir les dades del nou arxiu products.csv amb la base de dades creada, tenint en compte que des de transaction tens product_ids.

Els productes de cada transacció estan "desnormalitzats" en un _array_ a la columna `product_ids`. Per tant, aquesta nova taula hauria de ser una taula que tingués, com a mínim, dues columnes: `transaction_id` i `product_id`, per referenciar el producte amb la compra. Es podria afegir la columna `declined` per si volem fer una consulta de productes comprats, sense haver de fer `JOIN` amb `transaction` per esbrinar-ho.

:::warning
Com dèiem abans, amb dades en constant actualització com aquestes, el "correcte" seria utilitzar _VIEWs_, i no taules. de moment, però, utilitzarem una taule, que és el que demana l'exercici.
:::

Per tant, hem d'extreure aquestes dues (o tres) columnes de la taula `transaction`.

```sql
CREATE TABLE product_transaction AS
      SELECT transaction_id
           , product_id
        -- , declined   -- interessant per estalviar-se un JOIN més endavant
        FROM `transaction` AS t
        JOIN JSON_TABLE(
                t.product_ids,
                '$[*]'
                COLUMNS(product_id INT PATH '$')
             ) AS products;
```

### Exercici 1

> Necessitem conèixer el nombre de vegades que s'ha venut cada producte.

Per respondre a la pregunta d'aquest exercici, i gràcies a haver creat la columna `product_ids` com a JSON, podem simplement fer un COUNT() per `product_id` després d'extreure'n el `product_id` individual de la columna `product_ids`, i com és dinàmic, només necessitarem la taula product per saber el nom de cadascun.
Fent un `JOIN` amb la JSON_TABLE es generen fileres per cada product_id, que només haurem de comptar.

```sql
SELECT product_name, product_id
     , COUNT(product_id) AS compres
  FROM `transaction` AS t
  JOIN JSON_TABLE(
           t.product_ids,
           '$[*]'
           COLUMNS(product_id INT PATH '$')
       ) AS products
  JOIN product USING(product_id)
 GROUP BY product_name, product_id
```

Resultat:

| product_name                  | product_id | compres |
|-------------------------------|-----------:|--------:|
| Tully Dorne                   | 71         | 54      |
| Direwolf Stannis              | 1          | 61      |
| dooku solo                    | 19         | 49      |
| Tully                         | 47         | 62      |
| jinn Winterfell               | 97         | 61      |
| duel                          | 43         | 65      |
| Winterfell                    | 67         | 68      |
| Lannister                     | 31         | 47      |
| skywalker ewok                | 5          | 49      |
| skywalker ewok                | 89         | 51      |
| duel tourney                  | 83         | 57      |
| Direwolf riverlands the       | 79         | 66      |
| riverlands north              | 23         | 68      |
| north of Casterly             | 7          | 54      |
| Tully maester Tarly           | 29         | 49      |
| Lannister Barratheon Direwolf | 41         | 53      |
| Karstark Dorne                | 11         | 48      |
| duel tourney Lannister        | 3          | 51      |
| Dorne bastard                 | 73         | 47      |
| Winterfell Lannister          | 61         | 57      |
| skywalker ewok sith           | 17         | 61      |
| Direwolf Littlefinger         | 37         | 51      |
| palpatine chewbacca           | 13         | 60      |
| Direwolf Stannis              | 59         | 45      |
| Tarly Stark                   | 2          | 65      |
| kingsblood Littlefinger the   | 53         | 58      |

Havia oblidat afegir el filtre `NOT declined`:

```sql
SELECT product_name, product_id
     , COUNT(product_id) AS compres
  FROM `transaction` AS t
  JOIN JSON_TABLE(
           t.product_ids,
           '$[*]'
           COLUMNS(product_id INT PATH '$')
       ) AS products
  JOIN product USING(product_id)
 WHERE NOT declined
 GROUP BY product_name, product_id
```

| product_name                  | product_id | compres |
|-------------------------------|-----------:|--------:|
| Tully Dorne                   | 71         | 44      |
| Direwolf Stannis              | 1          | 51      |
| dooku solo                    | 19         | 44      |
| Tully                         | 47         | 50      |
| jinn Winterfell               | 97         | 53      |
| duel                          | 43         | 54      |
| Winterfell                    | 67         | 59      |
| Lannister                     | 31         | 40      |
| skywalker ewok                | 5          | 42      |
| skywalker ewok                | 89         | 46      |
| duel tourney                  | 83         | 46      |
| Direwolf riverlands the       | 79         | 52      |
| Tully maester Tarly           | 29         | 43      |
| Lannister Barratheon Direwolf | 41         | 48      |
| Karstark Dorne                | 11         | 40      |
| Direwolf Littlefinger         | 37         | 45      |
| palpatine chewbacca           | 13         | 51      |
| Direwolf Stannis              | 59         | 35      |
| Tarly Stark                   | 2          | 56      |
| kingsblood Littlefinger the   | 53         | 47      |
| riverlands north              | 23         | 60      |
| Winterfell Lannister          | 61         | 50      |
| north of Casterly             | 7          | 44      |
| skywalker ewok sith           | 17         | 54      |
| duel tourney Lannister        | 3          | 43      |
| Dorne bastard                 | 73         | 39      |

S'observen noms de productes repetits, però és per què són diferents (diferent color,  o diferent `warehouse_id`) i tenen diferent `product_id`, com es pot veure a les taules.
