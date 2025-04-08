-- Ex. 1.1 - Crear la taula credit_card

CREATE TABLE IF NOT EXISTS credit_card (
    credit_card_id SERIAL            PRIMARY KEY AUTO_INCREMENT,
    id             VARCHAR(15)       UNIQUE,
    iban           VARCHAR(80)       NOT NULL COMMENT 'Company should not have this information...',
    pan            VARCHAR(19)       NOT NULL COMMENT 'CC number length 15-19',
    pin            SMALLINT ZEROFILL NOT NULL COMMENT 'should never save this information',
    cvv            SMALLINT UNSIGNED NOT NULL,
    expiring_date  VARCHAR(8)        NOT NULL COMMENT 'Should be just month/year like 04/31 or 04/2031 with length of 5 o 7 characters',
    KEY cc_id (id) COMMENT '_Original_ id'

-- Ex. 1.2
-- Confirma que existeiri el registre a actualitzar...
SELECT * FROM credit_card WHERE id = 'CcU-2938';

-- Actualització
UPDATE credit_card
   SET iban = 'R323456312213576817699999'
 WHERE id   = 'CcU-2938'

-- Ex. 1.3
-- No funciona, per què les FK (company_id, credit_card_id, user_id) ho rebutjaran: no hi ha una companyia amb l'ID que es demana inserir:
INSERT INTO transaction (
    id,
    credit_card_id, company_id, user_id, lat, longitude, amount, declined
) VALUES (
    '108B1D1D-5B23-A76C-55EF-C568E49A99DD',
    'CcU-9999',     'b-9999',    '9999', 829.999,  -117.999, 111.11, 0
);

-- Es podria fer amb dades falses,. així:
INSERT INTO company VALUES (
    'b-9999', '<SENSE NOM>', '<SENSE TELEFON>', '<SENSE EMAIL>', '<PAIS DESCONEGUT>'
);
INSERT INTO credit_card VALUES (
    DEFAULT, 'CcU-9999', '<IBAN DESCONEGUT>', '0000', '000', '0000-00-00', NULL
);
INSERT INTO `user` VALUES (
    '9999', 'NO-NAME', 'NO-SURNAME', '<NO-PHONE>', '<NO-EMAIL>', NULL, NULL, NULL, NULL, NULL
);
--
-- I després, l'INSERT.

-- Ex. 1.4
ALTER TABLE credit_card
       DROP COLUMN pan;

-----

-- Ex. 2.1
DELETE
  FROM transction
 WHERE id = '02C6201E-D90A-1859-B4EE-88D2986D3B02';

-- Ex. 2.2
CREATE OR REPLACE VIEW VistaMarketing AS
       SELECT c.company_name AS 'Nom de la companyia'
            , c.phone        AS 'Telèfon'
            , c.country      AS 'País'
            , (SELECT ROUND(AVG(amount), 2)
                 FROM `transaction` AS sT
                WHERE sT.company_id = c.id) AS 'Mitjana de compres'
         FROM company AS c;

-- Show the view ordered by the average
SELECT * FROM vistamarketing ORDER BY 4 DESC;
SELECT * FROM vistamarketing ORDER BY `Mitjana de compres` DESC; -- alternate order

-- Ex.2.3
SELECT *
  FROM vistamarketing
 WHERE `País` = 'Germany'
  ORDER BY `Mitjana de compres` DESC; -- alternate

-- Ex. 3.1
ALTER TABLE company DROP COLUMN website;
ALTER TABLE credit_card
     MODIFY COLUMN pin CHAR(4),
        ADD COLUMN fecha_actual DATE;

SET foreign_key_checks = 0; -- permetre modificar la columna, encara que sigui una FK
ALTER TABLE `transaction`
  ADD FOREIGN KEY transaction_user_fk (user_id)        REFERENCES user(id),
  ADD FOREIGN KEY transaction_ccid_fk (credit_card_id) REFERENCES credit_card(id),
  MODIFY COLUMN user_id        INT         NOT NULL,
  MODIFY COLUMN credit_card_id VARCHAR(15) NOT NULL,
  MODIFY COLUMN company_id     VARCHAR(20) NOT NULL
  ;
SET foreign_key_checks = 1; -- restablir la verificació

-- Ex. 3.2
-- Crea la vista
CREATE OR REPLACE VIEW InformeTecnico AS
  SELECT t.id           AS 'ID Transacció'
       , u.name         AS 'Nom'
       , u.surname      AS 'Cognom(s)'
       , cc.iban        AS 'IBAN'
       , c.company_name AS 'Empresa'
    FROM transaction AS t
    JOIN credit_card AS cc ON cc.id = t.credit_card_id
    JOIN company     AS c  ON c.id  = company_id
    JOIN user        AS u  ON u.id  = user_id;

-- Consulta la vista
SELECT * FROM InformeTecnico ORDER BY 1;
