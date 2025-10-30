/* 2025-10-14 12:53:34 [14 ms] */
CREATE DATABASE IF NOT EXISTS tcc
    DEFAULT CHARACTER SET = 'utf8mb4';

USE tcc;

CREATE TABLE moon_calendar (
    cal_date     DATE    PRIMARY KEY,
    visible_area FLOAT   NOT NULL,
    num_phase    TINYINT NOT NULL,
    phase_char   CHAR(1) NOT NULL
);

-- TRUNCATE moon_calendar;

LOAD DATA LOCAL INFILE 'TCC/data/moon_phases_2000-2024_UTC_no_lib.csv'
     INTO TABLE moon_calendar
        FIELDS TERMINATED BY ','
        IGNORE 1 ROWS
        (cal_date, visible_area, num_phase, phase_char);

CREATE OR REPLACE TABLE moon_phase (
    num_phase   TINYINT     PRIMARY KEY,
    phase_emoji VARCHAR(2)  NOT NULL,
    phase_name  VARCHAR(20) NOT NULL,
    phase_eng   VARCHAR(20) NOT NULL
);

TRUNCATE moon_phase;

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


DROP TABLE IF EXISTS eur_mass_shootings;

CREATE TABLE eur_mass_shootings (
    incident_id     INT         PRIMARY KEY AUTO_INCREMENT,
    date            DATE        NOT NULL,
    city            VARCHAR(49) NOT NULL,
    country         VARCHAR(49) NOT NULL,
    victims_killed  SMALLINT    NOT NULL,
    victims_injured SMALLINT    NOT NULL,
    victims_total   SMALLINT    NOT NULL
) COMMENT 'In all Europe since 1999 to 2025';

TRUNCATE eur_mass_shootings;

LOAD DATA
     LOCAL INFILE 'TCC/data/European_mass_shootings.csv'
     INTO TABLE eur_mass_shootings
        FIELDS TERMINATED BY ';'
        OPTIONALLY ENCLOSED BY '"'
        IGNORE 1 ROWS (
            @Date
          , City
          , Country
          , @Deaths
          , @Injuries
          , @Total
        )
        SET date = STR_TO_DATE(@Date, '%d %M %Y')
          , victims_killed  = @Deaths
          , victims_injured = @Injuries
          , victims_total   = @Total
        ;

SELECT 1 AS incident_count
     , ems.*
     , mc.num_phase
     , mc.phase_char AS lunar_phase_icon
  FROM eur_mass_shootings AS ems
  JOIN moon_calendar           AS mc
    ON mc.cal_date = ems.date;


SELECT country
     , COUNT(incident_id) AS incident_count
     , victims_killed
     , victims_injured
     , victims_total
     , mc.num_phase
     , mc.phase_char AS lunar_phase_icon
  FROM eur_mass_shootings AS ems
  JOIN moon_calendar      AS mc
    ON mc.cal_date = ems.date
 GROUP BY country;

-- MAss shootings en USA, nuevo conjunto de datos de GVA
DROP TABLE IF EXISTS usa_mass_shootings;

CREATE TABLE IF NOT EXISTS usa_mass_shootings (
    incident_id     INT         PRIMARY KEY,
    incident_count  TINYINT     NOT NULL DEFAULT 1,
    date            DATE        NOT NULL,
    state           CHAR(40)    NOT NULL,
    victims_killed  SMALLINT    NOT NULL,
    victims_injured SMALLINT    NOT NULL,
    lng             FLOAT COMMENT 'Longitude',
    lat             FLOAT COMMENT 'Latitude'
);

TRUNCATE usa_mass_shootings;

LOAD DATA
     LOCAL INFILE 'TCC/data/gva_mass_shootings-2025-10-16.csv'
     INTO TABLE usa_mass_shootings
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        IGNORE 1 ROWS (
            incident_id
          , state
          , @longitude
          , @latitude
          , victims_killed
          , victims_injured
          , @killed
          , @injured
          , @date_fixed
          , @incident_count
        )
        SET date = @date_fixed
          , incident_count = 1
          , lng  = @longitude
          , lat  = @latitude
    ;

UPDATE usa_mass_shootings SET state = 'AL' WHERE state = 'Alabama';
UPDATE usa_mass_shootings SET state = 'AK' WHERE state = 'Alaska';
UPDATE usa_mass_shootings SET state = 'AZ' WHERE state = 'Arizona';
UPDATE usa_mass_shootings SET state = 'AR' WHERE state = 'Arkansas';
UPDATE usa_mass_shootings SET state = 'CA' WHERE state = 'California';
UPDATE usa_mass_shootings SET state = 'CO' WHERE state = 'Colorado';
UPDATE usa_mass_shootings SET state = 'CT' WHERE state = 'Connecticut';
UPDATE usa_mass_shootings SET state = 'DE' WHERE state = 'Delaware';
UPDATE usa_mass_shootings SET state = 'DC' WHERE state = 'District of Columbia';
UPDATE usa_mass_shootings SET state = 'FL' WHERE state = 'Florida';
UPDATE usa_mass_shootings SET state = 'GA' WHERE state = 'Georgia';
UPDATE usa_mass_shootings SET state = 'HI' WHERE state = 'Hawaii';
UPDATE usa_mass_shootings SET state = 'ID' WHERE state = 'Idaho';
UPDATE usa_mass_shootings SET state = 'IL' WHERE state = 'Illinois';
UPDATE usa_mass_shootings SET state = 'IN' WHERE state = 'Indiana';
UPDATE usa_mass_shootings SET state = 'IA' WHERE state = 'Iowa';
UPDATE usa_mass_shootings SET state = 'KS' WHERE state = 'Kansas';
UPDATE usa_mass_shootings SET state = 'KY' WHERE state = 'Kentucky';
UPDATE usa_mass_shootings SET state = 'LA' WHERE state = 'Louisiana';
UPDATE usa_mass_shootings SET state = 'ME' WHERE state = 'Maine';
UPDATE usa_mass_shootings SET state = 'MD' WHERE state = 'Maryland';
UPDATE usa_mass_shootings SET state = 'MA' WHERE state = 'Massachusetts';
UPDATE usa_mass_shootings SET state = 'MI' WHERE state = 'Michigan';
UPDATE usa_mass_shootings SET state = 'MN' WHERE state = 'Minnesota';
UPDATE usa_mass_shootings SET state = 'MS' WHERE state = 'Mississippi';
UPDATE usa_mass_shootings SET state = 'MO' WHERE state = 'Missouri';
UPDATE usa_mass_shootings SET state = 'MT' WHERE state = 'Montana';
UPDATE usa_mass_shootings SET state = 'NE' WHERE state = 'Nebraska';
UPDATE usa_mass_shootings SET state = 'NV' WHERE state = 'Nevada';
UPDATE usa_mass_shootings SET state = 'NH' WHERE state = 'New Hampshire';
UPDATE usa_mass_shootings SET state = 'NJ' WHERE state = 'New Jersey';
UPDATE usa_mass_shootings SET state = 'NM' WHERE state = 'New Mexico';
UPDATE usa_mass_shootings SET state = 'NY' WHERE state = 'New York';
UPDATE usa_mass_shootings SET state = 'NC' WHERE state = 'North Carolina';
UPDATE usa_mass_shootings SET state = 'ND' WHERE state = 'North Dakota';
UPDATE usa_mass_shootings SET state = 'OH' WHERE state = 'Ohio';
UPDATE usa_mass_shootings SET state = 'OK' WHERE state = 'Oklahoma';
UPDATE usa_mass_shootings SET state = 'OR' WHERE state = 'Oregon';
UPDATE usa_mass_shootings SET state = 'PA' WHERE state = 'Pennsylvania';
UPDATE usa_mass_shootings SET state = 'RI' WHERE state = 'Rhode Island';
UPDATE usa_mass_shootings SET state = 'SC' WHERE state = 'South Carolina';
UPDATE usa_mass_shootings SET state = 'SD' WHERE state = 'South Dakota';
UPDATE usa_mass_shootings SET state = 'TN' WHERE state = 'Tennessee';
UPDATE usa_mass_shootings SET state = 'TX' WHERE state = 'Texas';
UPDATE usa_mass_shootings SET state = 'UT' WHERE state = 'Utah';
UPDATE usa_mass_shootings SET state = 'VT' WHERE state = 'Vermont';
UPDATE usa_mass_shootings SET state = 'VA' WHERE state = 'Virginia';
UPDATE usa_mass_shootings SET state = 'WA' WHERE state = 'Washington';
UPDATE usa_mass_shootings SET state = 'WV' WHERE state = 'West Virginia';
UPDATE usa_mass_shootings SET state = 'WI' WHERE state = 'Wisconsin';
UPDATE usa_mass_shootings SET state = 'WY' WHERE state = 'Wyoming';

ALTER TABLE usa_mass_shootings
     MODIFY COLUMN `state` CHAR(2);

CREATE OR REPLACE VIEW vw_usa_shootings AS
       SELECT ms.*
            , lp.text_phase AS phase
            , mc.num_phase
            , mc.phase_char AS lunar_phase_icon
         FROM usa_mass_shootings AS ms
         JOIN moon_calendar      AS mc ON mc.cal_date = ms.date
         JOIN lunar_phases       AS lp USING(num_phase);

SELECT * FROM vw_usa_shootings;

-- Accidentes en Madrid 2018-2024
CREATE TABLE accidentes_madrid (
    fecha            DATE        NOT NULL,
    tipo_accidente   VARCHAR(50) NOT NULL,
    meteorologia     VARCHAR(50) NOT NULL,
    genero           TEXT        NOT NULL,
    positivo_alcohol CHAR(1)     NOT NULL DEFAULT 'D' COMMENT 'N No (0), S Sí (1), D, se desconoce (NULL)'
);

-- El fichero mad_accidentes.csv es un volcado de todos ellos en un solo fichero
-- de 14MiB, para no tener que estar repitiendo el LOAD DATA una y otra vez.
LOAD DATA
     LOCAL INFILE 'mad_accidentes.csv'
     INTO TABLE accidentes_madrid
        FIELDS TERMINATED BY ';'
        OPTIONALLY ENCLOSED BY '"'
        IGNORE 1 ROWS (
            fecha
          , tipo_accidente
          , meteorologia
          , genero
          , positivo_alcohol
        );

SELECT COUNT(*) AS accidentes
     , genero
     , meteorologia
  FROM accidentes_madrid
 GROUP BY genero, meteorologia;

SELECT mc.phase_char
     , COUNT(*) AS accidentes
     , genero
     , meteorologia
  FROM accidentes_madrid
  JOIN moon_calendar     AS mc ON cal_date = fecha
 GROUP BY genero, YEAR(fecha)
 ORDER BY 1, 3;

-- Barcelona
CREATE TABLE accidentes_bcn (
    fecha        DATE       NOT NULL,
    turno        VARCHAR(5) NOT NULL,
    num_victimas TINYINT    NOT NULL,
    lng          FLOAT,
    lat          FLOAT
);

CREATE TABLE naixements LIKE defuncions;

LOAD DATA
     LOCAL INFILE 'bcn_accidentes.csv'
     INTO TABLE accidentes_bcn
        FIELDS TERMINATED BY ';'
        OPTIONALLY ENCLOSED BY '"'
        IGNORE 1 ROWS (
            fecha
          , turno
          , num_victimas
          , lng
          , lat
        );

-- Los datos están por accidentes, NO por díà/turno, así que haremos un
-- agregado por fecha/turno del número de accidentes (`COUNT(*)`) y del total
-- de víctimas.
SELECT COUNT(*) AS incidentes
     , date
     , turno
     , SUM(num_victimas) AS num_victimas
FROM accidentes_bcn_tmp
INTO TABLE accidentes_bcn_diarios;

SELECT meteorologia
     , genero
     , COUNT(*)      AS accidentes
     , mp.phase_name AS fase
     , mc.phase_char AS lunar_phase_icon
  FROM accidentes_madrid AS am
  JOIN moon_calendar     AS mc ON cal_date = fecha
  JOIN moon_phase        AS mp USING(num_phase)
 GROUP BY meteorologia
     , genero;

-- Nacimientos y defunciones en Catalunya entre 2018 y 2023
CREATE TABLE defuncions (
  date    DATE      NOT NULL,
  homes   SMALLINT  NOT NULL,
  dones   SMALLINT  NOT NULL,
  total   SMALLINT  AS (homes+dones)
);

LOAD DATA``
     LOCAL INFILE 'TCC/data/IDESCAT/idescat-def-_2019-23.csv'
     INTO TABLE defuncions
         FIELDS TERMINATED BY ';'
       OPTIONALLY ENCLOSED BY '"'
          IGNORE 1 ROWS (
             date,
             homes,
             dones
          );

LOAD DATA
     LOCAL INFILE 'TCC/data/IDESCAT/idescat-naix-_2019-24.csv'
     INTO TABLE defuncions
         FIELDS TERMINATED BY ';'
       OPTIONALLY ENCLOSED BY '"'
          IGNORE 1 ROWS (
             date,
             homes,
             dones
          );

SELECT def.*
     , num_phase
     , phase_emoji AS fase
     , phase_name  AS fase_lunar
  FROM defuncions    AS def
  JOIN moon_calendar AS mc ON cal_date = date
  JOIN moon_phase    AS mp USING(num_phase);

SELECT naix.*
     , num_phase
     , phase_emoji AS fase
     , phase_name  AS fase_lunar
  FROM naixements    AS naix
  JOIN moon_calendar AS mc ON cal_date = date
  JOIN moon_phase    AS mp USING(num_phase);
