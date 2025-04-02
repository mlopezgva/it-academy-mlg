/**************************
 * SPRINT 1 - Task S2.01  *
 *========================*
 * Manuel López Grijalva  *
 *------------------------*
 * SQL queries Taks S2.01 *
 *  Nocions bàsiques SQL  *
 **************************/

-- Nivell 1
--   Exercici 1 - Import databases
--   Obert ambdós arxius (`estructura_dades.sql` i `dades_introduir.sql`) al MySQL Workbench i executats.
-- 
-- Modificats els `CREATE TABLE` per igualar el tipus de dada de la PK amb la FK de company(id).
-- Canviats alguns `VARCHAR()` a `TEXT` per evitar errors "futurs".

-- Creamos la base de datos
CREATE DATABASE IF NOT EXISTS mlg_transactions;
USE mlg_transactions;

-- Creamos la tabla company
CREATE TABLE IF NOT EXISTS company (
	id           VARCHAR(20) PRIMARY KEY,  -- FK in transaction has 20 characters, must be the same length
	company_name TEXT,
	phone        VARCHAR(15),
	email        TEXT,
	country      VARCHAR(80), -- max official name is for Hong Kong with 62 characters... in English
	website      TEXT
);


-- Creamos la tabla transaction
CREATE TABLE IF NOT EXISTS transaction (
	id             VARCHAR(64) PRIMARY KEY,
	credit_card_id VARCHAR(15) REFERENCES credit_card(id),
	company_id     VARCHAR(20), 
	user_id        INT         REFERENCES user(id),
	lat            FLOAT,
	longitude      FLOAT,
	timestamp      TIMESTAMP,
	amount         DECIMAL(10, 2),
	declined       BOOLEAN,
	FOREIGN KEY (company_id)
	 REFERENCES company(id) 
);

/* ### Exercici 2 - Consultes amb JOIN */

-- 2.1. Llistat de països que han comprat
SELECT DISTINCT country
  FROM mlg_transactions.`transaction` AS t
  JOIN mlg_transactions.`company`     AS c ON c.id = company_id
 WHERE  NOT declined

-- 2.2. Des de quants països es realitzen les compres
SELECT COUNT(DISTINCT country) AS countries
  FROM mlg_transactions.`transaction` AS t
  JOIN mlg_transactions.`company`     AS c ON c.id = company_id
 WHERE  NOT declined

-- 2.3. Companyia amb la mitjana més gran de vendes
SELECT AVG(amount) AS average
     , company_name
  FROM mlg_transactions.`transaction` AS t
  JOIN mlg_transactions.`company`     AS c ON c.id = company_id
 GROUP BY company_id, company_name
 ORDER BY 1 DESC
 LIMIT 1


-- Exercici 3: Utilitzant només subconsultes (sense utilitzar JOIN):
-- 3.1. Llista tranaccions des d'Alemanya
SELECT t.*
  FROM mlg_transactions.`transaction` AS t
 WHERE company_id IN (
	SELECT id FROM mlg_transactions.company WHERE country = 'Germany'
)
   AND NOT declined

-- 3.2. Empreses que han realitzat transaccions per una quantitat superior a la mitjana de totes les transaccions
SELECT company_name
  FROM mlg_transactions.company
 WHERE id IN(
         SELECT DISTINCT company_id
           FROM mlg_transactions.transaction AS t
          WHERE amount > (
                  SELECT AVG(amount)
                    FROM mlg_transactions.`transaction` AS agvt
                )
            AND NOT declined
       )

-- 3.3. Llistat d'empreses sense cap transacció
SELECT id
     , company_name
  FROM mlg_transactions.company
 WHERE id  NOT IN(
         SELECT DISTINCT company_id
           FROM mlg_transactions.transaction
       )

-- Nivell 2

-- Exercici 1
-- Identifica els cinc dies que es va generar la quantitat més gran d'ingressos a l'empresa per vendes. Mostra la data de cada transacció juntament amb el total de les vendes.

SELECT DATE(`timestamp`) AS 'Date'
     , SUM(amount)       AS Tot_amount
     , COUNT(company_id) AS Tot_transactions
  FROM mlg_transactions.transaction  AS t
  LEFT JOIN mlg_transactions.company AS c ON c.id = company_id
 GROUP BY DATE(`timestamp`)
 ORDER BY Tot_amount DESC
 LIMIT 5

-- Exercici 2
-- Quina és la mitjana de vendes per país? Presenta els resultats ordenats de major a menor mitjà.

SELECT country
     , AVG(amount)       AS Avg_amount
     , COUNT(company_id) AS Tot_transactions
  FROM mlg_transactions.transaction  AS t
  LEFT JOIN mlg_transactions.company AS c ON c.id = company_id
 GROUP BY country
 ORDER BY Avg_amount DESC

-- Exercici 3
-- En la teva empresa, es planteja un nou projecte per a llançar algunes campanyes publicitàries per a fer competència a la companyia "Non Institute". Per a això, et demanen la llista de totes les transaccions realitzades per empreses que estan situades en el mateix país que aquesta companyia.

-- 3.1. Mostra el llistat aplicant JOIN i subconsultes.
SELECT t.*
  FROM `transaction` AS t
  JOIN `company`     AS c ON c.id = company_id
 WHERE country = (
         SELECT country
           FROM company
          WHERE company_name = 'Non Institute'
       )
   AND company_name <>  'Non Institute'

-- 3.2. Mostra el llistat aplicant solament subconsultes.
SELECT t.*
  FROM `transaction` AS t
 WHERE company_id IN(
         SELECT id
           FROM company
          WHERE country = (
                  SELECT country
                    FROM company
                   WHERE company_name = 'Non Institute'
                )
            AND company_name <>  'Non Institute'
       )

-- Nivell 3

-- Exercici 1
-- Presenta el nom, telèfon, país, data i amount, d'aquelles empreses que van realitzar transaccions amb un valor comprès entre 100 i 200 euros i en alguna d'aquestes dates: 29 d'abril del 2021, 20 de juliol del 2021 i 13 de març del 2022. Ordena els resultats de major a menor quantitat.

SELECT company_name      AS nom
     , phone             AS 'telèfon'
     , country           AS 'país'
     , DATE(`timestamp`) AS 'data'
     , amount            AS valor
  FROM mlg_transactions.`transaction` AS t
  JOIN mlg_transactions.company       AS c ON c.id = company_id
 WHERE amount BETWEEN 100.00 AND 200.00
   AND DATE(`timestamp`) IN('2021-04-29', '2021-07-20', '2022-03-13')
 ORDER BY valor DESC

-- Exercici 2
-- Necessitem optimitzar l'assignació dels recursos i dependrà de la capacitat operativa que es requereixi, per la qual cosa et demanen la informació sobre la quantitat de transaccions que realitzen les empreses, però el departament de recursos humans és exigent i vol un llistat de les empreses on especifiquis si tenen més de 4 transaccions o menys.

SELECT company_name
     , COUNT(t.id)     AS tot_transctions
     , COUNT(t.id) > 4 AS more_than_four
  FROM mlg_transactions.transaction AS t
  JOIN mlg_transactions.company     AS c ON c.id = company_id
 GROUP BY t.company_id, c.company_name
 ORDER BY 2 DESC
