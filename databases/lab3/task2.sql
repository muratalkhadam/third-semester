use `db-labs`;


SELECT p.first_name,
       (SELECT d.percentage
        FROM discounts d
        WHERE p.patient_id = d.patient_id) AS discount_percentage
FROM patients AS p;

SELECT concat(cc.first_name, ' ', cc.last_name) AS fullname, cc.height
FROM (SELECT p.first_name, p.last_name, c.height
      FROM cards AS c,
           patients AS p
      WHERE p.patient_id = c.patient_id) AS cc
ORDER BY cc.height DESC;

# patients with any beneficiaries
SELECT *
FROM patients AS p
WHERE EXISTS(
              SELECT *
              FROM discounts AS d
              WHERE d.patient_id = p.patient_id
          );

# names with diagnosis
SELECT p.first_name
FROM patients AS p
WHERE p.patient_id IN (SELECT a.patient_id
                       FROM conclusions AS c,
                            applications AS a
                       WHERE a.application_id = c.application_id);

# possible combinations of possible and established diagnosis
SELECT possible_diagnosis, established_diagnosis
FROM applications
         CROSS JOIN conclusions;

SELECT concat(p.first_name, ' ', p.last_name) AS fullname,
       d.reason                               AS preferential_group
FROM patients AS p
         JOIN discounts AS d ON p.patient_id = d.patient_id;

# patients with the not normal Body Mass Index
SELECT *
FROM (SELECT concat(p.first_name, ' ', p.last_name)        AS fullname,
             c.height,
             c.weight,
             ROUND(c.weight / POW((c.height / 100), 2), 2) AS bmi
      FROM patients AS p
               JOIN cards AS c ON p.patient_id = c.patient_id) AS bmi_stats
WHERE NOT bmi_stats.bmi BETWEEN 18.5 AND 24.9;

SELECT concat(a.first_name, ' ', a.last_name) AS admin_fullname,
       COUNT(app.service_type)                AS processed_applications
FROM admins AS a
         JOIN applications AS app ON a.admin_id = app.admin_id
GROUP BY admin_fullname;

SELECT concat(p.first_name, ' ', p.last_name) AS patient_fullname,
       concat(d.first_name, ' ', d.last_name) AS doctor_fullname,
       d.qualification,
       d.specialization,
       a.possible_diagnosis
FROM doctors AS d
         LEFT OUTER JOIN applications AS a
                         ON d.doctor_id = a.doctor_id
         LEFT OUTER JOIN patients AS p
                         ON p.patient_id = a.patient_id;

SELECT concat(p.first_name, ' ', p.last_name) AS patient_fullname,
       c.established_diagnosis,
       c.treatment_method,
       c.sum_to_pay
FROM patients AS p
         RIGHT OUTER JOIN applications AS a
                          ON p.patient_id = a.patient_id
         RIGHT OUTER JOIN conclusions AS c
                          ON a.application_id = c.application_id;

SELECT concat(d.first_name, ' ', d.last_name) AS worker_fullname
FROM doctors AS d
UNION
SELECT concat(a.first_name, ' ', a.last_name)
FROM admins AS a

murat сын шлюхи
