-- Cálculo del procentaje total de operaciones declinadas
SELECT SUM(declined) AS declined
     , COUNT(transaction_id)   AS "all"
     , ROUND((SUM(declined)/COUNT(transaction_id))*100, 2) AS "% Declined"
  FROM `transaction`

/*
| declined | all | % Declined |
|----------|-----|------------|
| 87       | 587 | 14.82      |
*/

-- Cálculo del procentaje total de operaciones declinadas por año
SELECT YEAR(transaction_ts) AS YearOfTransaction
     , SUM(declined) AS declined
     , COUNT(transaction_id)   AS "all"
     , ROUND((SUM(declined)/COUNT(transaction_id))*100, 2) AS "% Declined"
  FROM `transaction`
  JOIN company USING(company_id)
 GROUP BY YEAR(transaction_ts)
 ORDER BY 4 DESC

/*
| YearOfTransaction | declined | all | % Declined |
|-------------------|----------|-----|------------|
| 2021              | 74       | 479 | 15.45      |
| 2022              | 13       | 108 | 12.04      |
*/

-- Cálculo del porcentaje de operaciones declinadas por país
SELECT country
     , SUM(declined) AS declined
     , COUNT(transaction_id)   AS "all"
     , ROUND((SUM(declined)/COUNT(transaction_id))*100, 2) AS "% Declined"
  FROM `transaction`
  JOIN company USING(company_id)
 GROUP BY country
 ORDER BY 4 DESC

/*
| country        | declined | all | % Declined |
|----------------|----------|-----|------------|
| Spain          | 1        | 2   | 50.00      |
| France         | 3        | 6   | 50.00      |
| Australia      | 6        | 12  | 50.00      |
| Italy          | 8        | 17  | 47.06      |
| United States  | 8        | 17  | 47.06      |
| New Zealand    | 5        | 11  | 45.45      |
| Netherlands    | 8        | 18  | 44.44      |
| Belgium        | 5        | 13  | 38.46      |
| China          | 1        | 3   | 33.33      |
| Sweden         | 11       | 79  | 13.92      |
| Norway         | 7        | 68  | 10.29      |
| Ireland        | 6        | 62  | 9.68       |
| United Kingdom | 7        | 100 | 7.00       |
| Canada         | 4        | 61  | 6.56       |
| Germany        | 7        | 118 | 5.93       |
*/

-- Para saber el producto más caro comprado por cada usuario
-- 1. Vista con el producto más caro por transacción:
CREATE OR REPLACE
  VIEW most_expensive_by_transaction AS
     SELECT transaction_id, MAX(product_id) AS product_id
          , MAX(price) AS price
       FROM product_transaction
       JOIN product USING(product_id)
   GROUP BY transaction_id
   ORDER BY product_id;

-- 2. Consulta/vista con el producto más caro por usuario
SELECT user_id, CONCAT(u.name, ' ', u.surname) AS uname
     , country
     , MAX(product_name)
     , MAX(mt.price)
  FROM `transaction` AS t
  JOIN most_expensive_by_transaction AS mt USING(transaction_id)
  JOIN `user`        AS u USING(user_id)
  JOIN product       AS p USING(product_id)
 GROUP BY user_id, name, surname, country
 ORDER BY name;

-- Pero se puede haver sin la VIEW extra:
SELECT user_id, CONCAT(u.name, ' ', u.surname) AS uname
     , country
     , MAX(product_name)
     , MAX(p.price)
  FROM `transaction` AS t
  JOIN product_transaction AS pt USING(transaction_id)
  JOIN `user`        AS u USING(user_id)
  JOIN product       AS p USING(product_id)
 GROUP BY user_id, name, surname, country
 ORDER BY name;

-- Ahora solo queda transformar eso a DAX "y ya"...

/*
+---------+--------------------+----------------+-------------------------------+---------------+
| user_id | uname              | country        | MAX(product_name)             | MAX(mt.price) |
+---------+--------------------+----------------+-------------------------------+---------------+
| 81      | Acton Gallegos     | United States  | north of Casterly             | 161.11        |
| 266     | Aiko Chaney        | Canada         | Lannister Barratheon Direwolf | 171.13        |
| 121     | Ainsley Herrera    | United States  | dooku solo                    | 60.33         |
| 243     | Alan Vazquez       | Canada         | duel                          | 114.77        |
| 90      | Alika Kinney       | United States  | Tully Dorne                   | 195.94        |
| 248     | Allen Calhoun      | Canada         | north of Casterly             | 161.11        |
| 174     | Amal Kennedy       | United Kingdom | Lannister Barratheon Direwolf | 141.01        |
| 129     | Amber Blevins      | United States  | skywalker ewok                | 195.94        |
| 180     | Amelia Valenzuela  | United Kingdom | Lannister                     | 85.02         |
| 244     | Andrew Strong      | Canada         | Winterfell                    | 195.94        |
| 111     | Astra Baldwin      | United States  | jinn Winterfell               | 132.86        |
| 209     | Athena Malone      | Canada         | Winterfell                    | 195.94        |
| 217     | Avye Key           | Canada         | Winterfell                    | 195.94        |
| 66      | Bert Juarez        | United States  | duel tourney                  | 167.20        |
| 173     | Bertha Sloan       | United Kingdom | jinn Winterfell               | 169.96        |
| 63      | Beverly Burt       | United States  | duel tourney                  | 26.51         |
| 213     | Blake Strickland   | Canada         | Lannister Barratheon Direwolf | 171.13        |
| 255     | Blaze Daniel       | Canada         | Winterfell Lannister          | 91.89         |
| 196     | Blaze Duke         | United Kingdom | jinn Winterfell               | 114.09        |
| 96      | Brennan Wynn       | United States  | Winterfell Lannister          | 195.94        |
| 175     | Brent Bates        | United Kingdom | Winterfell                    | 195.94        |
| 262     | Brett Kirby        | Canada         | Tully Dorne                   | 161.11        |
| 149     | Brock Doyle        | United States  | Dorne bastard                 | 114.09        |
| 147     | Brody Talley       | United States  | Lannister Barratheon Direwolf | 169.96        |
| 137     | Brody Goodwin      | United States  | Winterfell Lannister          | 171.13        |
| 118     | Brooke Jensen      | United States  | duel tourney                  | 28.01         |
| 208     | Burke Graham       | Canada         | Tully Dorne                   | 167.20        |
| 87      | Camden Carpenter   | United States  | Direwolf Stannis              | 169.96        |
| 234     | Camilla Roach      | Canada         | skywalker ewok                | 172.78        |
| 78      | Camilla Zimmerman  | United States  | Tully                         | 171.22        |
| 197     | Carly Mathews      | United Kingdom | Tully Dorne                   | 169.96        |
| 98      | Cassandra Ferguson | United States  | Winterfell Lannister          | 28.01         |
| 125     | Celeste Ellis      | United States  | dooku solo                    | 161.11        |
| 95      | Chase Ellis        | United States  | Tully                         | 91.89         |
| 238     | Chester Haynes     | Canada         | Winterfell Lannister          | 171.13        |
| 265     | Chloe Keith        | Canada         | Tully                         | 172.78        |
| 268     | Clark Olson        | Canada         | Lannister                     | 161.11        |
| 141     | Clark Hewitt       | United States  | skywalker ewok                | 172.78        |
*/


SELECT `Client Name`
     , FIRST_VALUE(product_name) OVER pr AS most_expensive
     , FIRST_VALUE(price)        OVER pr AS max_price
     , LAST_VALUE(product_name)  OVER pr AS cheapest_product
     , LAST_VALUE(price)         OVER pr AS cheapest_price
     , COUNT(transaction_id)             AS transaction_count
     , (SELECT SUM(declined)
          FROM `transaction` AS st
         WHERE st.user_id = up.user_id
       )                         AS declined_transactions
     , u.country                 AS users_country
  FROM user_products AS up
  JOIN `user`        AS u  USING(user_id)
 GROUP BY user_id, `Client Name`, u.country, product_name, price
  WINDOW pr AS (
         PARTITION BY user_id
             ORDER BY price DESC)
;
