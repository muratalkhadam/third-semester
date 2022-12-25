USE `db-labs`;

# a
CREATE OR REPLACE VIEW patient_info AS
SELECT p.patient_id,
       CONCAT(p.first_name, ' ', p.last_name) AS full_name,
       c.height,
       c.weight,
       c.medical_group
FROM patients AS p
         JOIN cards c on p.patient_id = c.patient_id
ORDER BY p.patient_id;

SELECT *
FROM patient_info;
# b
CREATE OR REPLACE VIEW patient_doctor AS
SELECT p.patient_id,
       CONCAT(p.first_name, ' ', p.last_name) AS patient_name,
       pi.medical_group,
       CONCAT(d.first_name, ' ', d.last_name) AS doctor_name,
       possible_diagnosis,
       d.specialization
FROM patients p
         JOIN applications a on p.patient_id = a.patient_id
         JOIN doctors d on d.doctor_id = a.doctor_id
         JOIN patient_info pi on pi.patient_id = a.patient_id
ORDER BY doctor_name;

SELECT *
FROM patient_doctor;
# c
ALTER VIEW patient_info AS
SELECT p.patient_id,
       CONCAT(p.first_name, ' ', p.last_name)        AS full_name,
       c.height,
       c.weight,
       c.medical_group,
       ROUND(c.weight / POW((c.height / 100), 2), 2) AS bmi
FROM patients AS p
         JOIN cards c on p.patient_id = c.patient_id
ORDER BY p.patient_id;

SELECT *
FROM patient_info;
# d
/*
MySQL command to view the definition of a view or table,
similar to sp_helptext in Microsoft SQL Server
*/
SHOW CREATE VIEW patient_info;

SELECT *
FROM information_schema.TABLES
WHERE TABLE_TYPE = 'VIEW'
  AND TABLE_SCHEMA = 'db-labs';
