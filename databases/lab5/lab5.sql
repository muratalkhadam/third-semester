USE `db-labs`;

# 1 a
DROP PROCEDURE IF EXISTS temp_five_patients;
DELIMITER $$
CREATE PROCEDURE temp_five_patients()
BEGIN
    DROP TABLE IF EXISTS temp;
    CREATE TEMPORARY TABLE temp AS (SELECT *
                                    FROM patient_info
                                    LIMIT 5);
    SELECT *
    FROM temp;
END $$
DELIMITER ;
CALL temp_five_patients();


# 1 b
DROP PROCEDURE IF EXISTS compare_height;
DELIMITER $$
CREATE PROCEDURE compare_height(IN height_to_compare INT)
BEGIN
    SELECT full_name,
           IF(height > height_to_compare,
              CONCAT('ВИЩЕ', ' ', height_to_compare),
              CONCAT('НИЖЧЕ', ' ', height_to_compare)
               ) AS height_comparing
    FROM patient_info;
END $$
DELIMITER ;
CALL compare_height(185);


# 1 c
DROP PROCEDURE IF EXISTS do_while;
DELIMITER $$
CREATE PROCEDURE do_while()
BEGIN
    DECLARE var INT DEFAULT 5;

    WHILE var > 0
        DO
            SET var = var - 1;
        END WHILE;

    SELECT var;
END $$
DELIMITER ;
CALL do_while();


# 1 d
DROP PROCEDURE IF EXISTS get_beneficiaries;
DELIMITER $$
CREATE PROCEDURE get_beneficiaries()
BEGIN
    SELECT *
    FROM patients
    WHERE is_beneficiary;
END $$
DELIMITER ;
CALL get_beneficiaries();

# 1 e
DROP PROCEDURE IF EXISTS get_patient_by_gender;
DELIMITER $$
CREATE PROCEDURE get_patient_by_gender(
    IN gen VARCHAR(20)
)
BEGIN
    SELECT *
    FROM patients
    WHERE gender = gen;
END $$
DELIMITER ;
CALL get_patient_by_gender('чоловік');

# 1 f
DROP PROCEDURE IF EXISTS get_amount_by_bmi_limit;
DELIMITER $$
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
DELIMITER ;
CALL get_amount_by_bmi_limit(20, @amount);

# 1 g
DROP PROCEDURE IF EXISTS update_discount;
DELIMITER $$
CREATE PROCEDURE update_discount()
BEGIN
    UPDATE discounts
    SET percentage = percentage * 1.1
    WHERE percentage < 10;
END $$
DELIMITER ;
CALL update_discount();

# 1 h
DROP PROCEDURE IF EXISTS check_admins;
DELIMITER $$
CREATE PROCEDURE check_admins()
BEGIN
    SELECT *
    FROM admins
    WHERE regular_patients > 7;
END $$
DELIMITER ;
CALL check_admins();

# 2 a
DROP FUNCTION IF EXISTS get_high_qual_doctors;
DELIMITER $$
CREATE FUNCTION get_high_qual_doctors() RETURNS INT
    DETERMINISTIC
BEGIN
    DECLARE amount INT;
    SELECT COUNT(*)
    FROM doctors
    WHERE qualification = 'вища'
    INTO amount;
    RETURN amount;
END $$
DELIMITER ;
SELECT get_high_qual_doctors() AS high_qual;

# 2 b (stored procedure for this task)
DROP PROCEDURE IF EXISTS get_by_spec;
DELIMITER $$
CREATE PROCEDURE get_by_spec(
    IN spec VARCHAR(20)
)
BEGIN
    SELECT *
    FROM doctors
    WHERE specialization = spec;
END $$
DELIMITER ;
CALL get_by_spec('кардіоревматолог');

# 2 c
DELIMITER $$
DROP FUNCTION IF EXISTS get_table;
CREATE FUNCTION get_table(t_name VARCHAR(20)) RETURNS VARCHAR(2048)
    DETERMINISTIC
BEGIN
    DECLARE result VARCHAR(2048);
    DECLARE temp1, temp2 VARCHAR(1024);
    SELECT GROUP_CONCAT(COLUMN_NAME)
    INTO temp1
    FROM information_schema.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE()
      AND TABLE_NAME = t_name;

    SELECT GROUP_CONCAT(PRIVILEGES)
    INTO temp2
    FROM information_schema.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE()
      AND TABLE_NAME = t_name;

    SET result = CONCAT(temp1, temp2);
    RETURN result;
END $$
DELIMITER ;
SELECT get_table('patients');
