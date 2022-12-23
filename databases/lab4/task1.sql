use `db-labs`;

SELECT COUNT(*)
FROM patients
WHERE gender = 'чоловік';

SELECT SUM(sum_to_pay)
FROM conclusions;

SELECT UPPER(last_name)
FROM patients;

SELECT LOWER(first_name)
FROM admins;

SELECT CONCAT(first_name, ' ', last_name)                          AS full_name,
       DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), birthday)), '%Y') + 0 AS age
FROM patients
ORDER BY age;

SELECT *
FROM admins
GROUP BY admin_id
HAVING regular_patients > 7;

SELECT *
FROM cards
HAVING 170 < height;


