-- 
-- Dissenyar l'esquema en estrella.
-- 

CREATE SCHEMA `mlg_sprint4`
      DEFAULT CHARACTER SET utf8
      COLLATE utf8_unicode_ci ;

-- 
-- Creem les taules:
-- 

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

-- 
-- Carreguem les dades
-- 

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
LOAD DATA
    LOCAL INFILE 'users_ca.csv'
     INTO TABLE `user`
          FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\r\n'
          IGNORE 1 LINES
          (user_id,name,surname,phone,email,@bdate,country,city,postal_code,address)
      SET birthdate = STR_TO_DATE(@bdate, '%b %d, %Y')
;

LOAD DATA
    LOCAL INFILE 'credit_cards.csv'
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

LOAD DATA
    LOCAL INFILE 'transactions.csv'
     INTO TABLE transcation
          FIELDS TERMINATED BY ';'
                 OPTIONALLY ENCLOSED BY '"'
          IGNORE 1 LINES
          (transaction_id,credit_card_id,company_id,transaction_ts,amount,declined,@prods,user_id,latitude,longitude)
      SET product_ids = CONCAT('[', @prods, ']')
;

-- Exercici 1
-- Realitza una subconsulta que mostri tots els usuaris amb més de 30 transaccions utilitzant almenys 2 taules.

SELECT user_id
     , CONCAT(name, ' ', surname) AS `user`
     , COUNT(transaction_id) AS transaction_count
  FROM transaction AS t
  JOIN user        AS u USING(user_id)
 WHERE NOT declined
 GROUP BY user_id
 HAVING COUNT(transaction_id) > 30

--- També podem veure el total de transaccions i el total de transaccions amb èxit
SELECT user_id
     , CONCAT(name, ' ', surname) AS `user`
     , COUNT(transaction_id) AS transaction_count
     , SUM(NOT declined)     AS successful
  FROM transaction AS t
  JOIN user        AS u USING(user_id)
 GROUP BY user_id
 HAVING COUNT(transaction_id) > 30

-- Exercici 2
-- Mostra la mitjana d'amount per IBAN de les targetes de crèdit a la companyia Donec Ltd, utilitza almenys 2 taules.
SELECT cc.iban
     , AVG(t.amount) AS spend_avg
  FROM transaction AS t
  JOIN credit_card AS cc USING(credit_card_id)
  JOIN company     AS c  USING(company_id)
 WHERE company_name = 'Donec Ltd'
   AND NOT declined
 GROUP BY iban;

-- Nivell 2
-- Exercici 0
-- Crea una nova taula que reflecteixi l'estat de les targetes de crèdit basat en si
-- les últimes tres transaccions van ser declinades
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

-- Exercici 1
SELECT COUNT(last_three_declined = 0) AS Active_CC
  FROM active_cc
 GROUP BY last_three_declined
 HAVING last_three_declined = 0;

-- Nivell 3
-- Exercici 0
-- Crea una taula amb la qual puguem unir les dades del nou arxiu products.csv amb la base de dades creada,
-- tenint en compte que des de transaction tens product_ids.
CREATE TABLE product_transaction AS
      SELECT transaction_id
           , product_id
        FROM `transaction` AS t
        JOIN JSON_TABLE(
                t.product_ids,
                '$[*]'
                COLUMNS(product_id INT PATH '$')
             ) AS products;

-- Exercici 1
-- Necessitem conèixer el nombre de vegades que s'ha venut cada producte.

-- Sense la nova taula:
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

-- Utilitzant la taula creada per a aquest nivell:
SELECT product_name
     , product_id
     , COUNT(NOT declined) AS compres
  FROM product_transaction
  JOIN product     USING(product_id)
  JOIN transaction USING(transaction_id)
 GROUP BY product_name, product_id
