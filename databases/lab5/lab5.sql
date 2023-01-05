USE `db-labs`;

# 1 a
DELIMITER $$
DROP PROCEDURE IF EXISTS temp_five_patients;
CREATE PROCEDURE temp_five_patients()
BEGIN
    DROP TABLE IF EXISTS temp;
    CREATE TEMPORARY TABLE temp AS (SELECT *
                                    FROM patient_info
                                    LIMIT 5);
    SELECT *
    FROM temp;
END $$
CALL temp_five_patients();
DELIMITER ;

# 1 b
DELIMITER $$
DROP PROCEDURE IF EXISTS compare_height;
CREATE PROCEDURE compare_height(IN height_to_compare INT)
BEGIN
    SELECT full_name,
           IF(height > height_to_compare,
              CONCAT('ВИЩЕ', ' ', height_to_compare),
              CONCAT('НИЖЧЕ', ' ', height_to_compare)
               ) AS height_comparing
    FROM patient_info;
END $$
CALL compare_height(185);
DELIMITER ;

# 1 c
DELIMITER $$
DROP PROCEDURE IF EXISTS do_while;
CREATE PROCEDURE do_while()
BEGIN
    DECLARE var INT DEFAULT 5;

    WHILE var > 0
        DO
            SET var = var - 1;
        END WHILE;

    SELECT var;
END $$
CALL do_while();
DELIMITER ;

# 1 d
DELIMITER $$
DROP PROCEDURE IF EXISTS get_beneficiaries;
CREATE PROCEDURE get_beneficiaries()
BEGIN
    SELECT *
    FROM patients
    WHERE is_beneficiary;
END $$
CALL get_beneficiaries();
DELIMITER ;

# 1 e
DELIMITER $$
DROP PROCEDURE IF EXISTS get_patient_by_gender;
CREATE PROCEDURE get_patient_by_gender(
    IN gen VARCHAR(20)
)
BEGIN
    SELECT *
    FROM patients
    WHERE gender = gen;
END $$
CALL get_patient_by_gender('чоловік');
DELIMITER ;

# 1 f
DELIMITER $$
DROP PROCEDURE IF EXISTS get_amount_by_bmi_limit;
CREATE PROCEDURE get_amount_by_bmi_limit(
    IN bmi_max INT,
    OUT amount INT
)
BEGIN
    SELECT COUNT(*)
    FROM patient_info
    WHERE bmi < bmi_max
    INTO amount;

    SELECT amount;
END $$
CALL get_amount_by_bmi_limit(20, @amount);
DELIMITER ;

# 1 g
DELIMITER $$
DROP PROCEDURE IF EXISTS update_discount;
CREATE PROCEDURE update_discount()
BEGIN
    UPDATE discounts
    SET percentage = percentage * 1.1
    WHERE percentage < 10;
END $$
CALL update_discount();
DELIMITER ;

# 1 h
DELIMITER $$
DROP PROCEDURE IF EXISTS check_admins;
CREATE PROCEDURE check_admins()
BEGIN
    SELECT *
    FROM admins
    WHERE regular_patients > 7;
END $$
CALL check_admins();
DELIMITER ;

