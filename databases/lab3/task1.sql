use `db-labs`;


SELECT *
FROM patients;

SELECT *
FROM discounts
WHERE percentage > 10 ;

SELECT *
FROM patients
WHERE gender = 'чоловік' or is_beneficiary;

SELECT *
FROM patients
WHERE not gender = 'жінка';

SELECT *
FROM patients
WHERE gender = 'чоловік' and is_beneficiary;

SELECT *
FROM patients
WHERE gender = 'чоловік' AND NOT is_beneficiary
   OR
    gender = 'жінка' AND is_beneficiary;

SELECT medical_group
FROM cards
WHERE height > 170;

SELECT *
FROM cards
WHERE weight % 2 = 0;

SELECT height, weight
FROM cards
WHERE medical_group IN ('основна', 'спеціальна');

SELECT *
FROM patients
WHERE birthday BETWEEN DATE('2000-01-01') AND DATE('2009-12-31');

SELECT *
FROM patients
WHERE first_name LIKE 'м%';

SELECT *
FROM applications
WHERE possible_diagnosis IS NOT NULL;