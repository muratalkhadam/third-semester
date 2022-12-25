use `db-labs`;
# a
SELECT COUNT(*)
FROM patients
WHERE gender = 'чоловік';
# b
SELECT SUM(sum_to_pay)
FROM conclusions;
# c
SELECT UPPER(last_name)
FROM patients;

SELECT LOWER(first_name)
FROM admins;
# d
SELECT CONCAT(first_name, ' ', last_name)                          AS full_name,
       DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), birthday)), '%Y') + 0 AS age
FROM patients
ORDER BY age;
# e
SELECT COUNT(shift_number), shift_number
FROM admins
GROUP BY shift_number;
# f
SELECT COUNT(patient_id)                      AS patient_amount,
       CONCAT(d.first_name, ' ', d.last_name) AS doctor_name
FROM applications
         JOIN doctors d on d.doctor_id = applications.doctor_id
GROUP BY doctor_name
HAVING patient_amount > 1;
# g
SELECT AVG(sum_to_pay)
FROM conclusions
HAVING AVG(sum_to_pay) > 1;
# h
SELECT ROW_NUMBER() OVER (ORDER BY c.height DESC) AS position,
       CONCAT(p.first_name, ' ', p.last_name)     AS full_name,
       c.height
FROM patients p
         JOIN cards c on p.patient_id = c.patient_id;
# i
SELECT CONCAT(p.first_name, ' ', p.last_name) AS full_name,
       c.weight
FROM patients p
         JOIN cards c on p.patient_id = c.patient_id
ORDER BY c.weight DESC;
