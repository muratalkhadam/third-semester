use `db-labs`;

# patients
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Марк', 'Дудник', '2004-07-13', 'чоловік', true);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Анастасія', 'Гопак', '1968-07-24', 'жінка', false);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Арсен', 'Дурік', '1990-07-05', 'чоловік', false);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Лілія', 'Левицька', '1966-10-25', 'жінка', false);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Роксолана', 'Млинець', '2004-07-01', 'жінка', true);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Софія', 'Бударь', '1963-02-04', 'жінка', false);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Лідія', 'Таран', '1998-04-28', 'жінка', false);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Валерій', 'Геращенко', '1992-10-06', 'чоловік', false);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Григорій', 'Дударь', '1981-01-11', 'чоловік', false);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Андрій', 'Мельник', '1991-11-20', 'чоловік', false);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Мілена', 'Шевченко', '1986-03-28', 'жінка', false);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Марта', 'Коваленко', '2001-01-05', 'жінка', false);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Белла', 'Бондаренко', '1994-06-24', 'жінка', true);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Андрій', 'Коваль', '1989-05-19', 'чоловік', true);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Аврора', 'Шевчук', '1990-08-12', 'жінка', false);
insert into patients (first_name, last_name, birthday, gender, is_beneficiary) values ('Мурат', 'Ал Хадам', '2004-06-10', 'чоловік', true);

# doctors
insert into doctors (first_name, last_name, working_start_date, qualification, specialization) values ('Аліса', 'Гончарук', '2014-01-19', 'друга', 'кардіоревматолог');
insert into doctors (first_name, last_name, working_start_date, qualification, specialization) values ('Богдан', 'Бондарь', '2009-06-01', 'вища', 'гастроентеролог');
insert into doctors (first_name, last_name, working_start_date, qualification, specialization) values ('Василь', 'Зазібілі', '2018-01-19', 'друга', 'вірусолог');
insert into doctors (first_name, last_name, working_start_date, qualification, specialization) values ('Ізабелла', 'Гонта', '2009-07-11', 'вища', 'нарколог');
insert into doctors (first_name, last_name, working_start_date, qualification, specialization) values ('Клара', 'Мурленко', '2020-01-17', 'перша', 'онколог');
insert into doctors (first_name, last_name, working_start_date, qualification, specialization) values ('Веніамін', 'Довпак', '2014-09-04', 'друга', 'нейрохірург');
insert into doctors (first_name, last_name, working_start_date, qualification, specialization) values ('Борис', 'Юрковський', '2021-03-14', 'перша', 'травматолог');

# admins
insert into admins (first_name, last_name, regular_patients, shift_number) values ('Марія', 'Гуцул', 10, 101);
insert into admins (first_name, last_name, regular_patients, shift_number) values ('Арнольд', 'Шевченко', 6, 101);
insert into admins (first_name, last_name, regular_patients, shift_number) values ('Марія', 'Шпак', 7, 202);
insert into admins (first_name, last_name, regular_patients, shift_number) values ('Алла', 'Коваленко', 9, 202);

# discounts
insert into discounts (percentage, reason, patient_id) values (10, 'дитина війни', 1);
insert into discounts (percentage, reason, patient_id) values (5, 'інвалід', 5);
insert into discounts (percentage, reason, patient_id) values (13, 'сирота', 13);
insert into discounts (percentage, reason, patient_id) values (25, 'батько-одинак', 14);
insert into discounts (percentage, reason, patient_id) values (7, 'учасник бойових дій', 16);

# cards
insert into cards (height, weight, medical_group, patient_id) values (175, 66.6, 'підготовча', 1);
insert into cards (height, weight, medical_group, patient_id) values (191, 90, 'спеціальна', 2);
insert into cards (height, weight, medical_group, patient_id) values (187, 91, 'підготовча', 3);
insert into cards (height, weight, medical_group, patient_id) values (165, 51.6, 'підготовча', 4);
insert into cards (height, weight, medical_group, patient_id) values (169, 56, 'підготовча', 5);
insert into cards (height, weight, medical_group, patient_id) values (151, 44, 'спеціальна', 6);
insert into cards (height, weight, medical_group, patient_id) values (188, 67, 'спеціальна', 7);
insert into cards (height, weight, medical_group, patient_id) values (179, 63.6, 'підготовча', 8);
insert into cards (height, weight, medical_group, patient_id) values (175, 66.6, 'підготовча', 9);
insert into cards (height, weight, medical_group, patient_id) values (185, 75.6, 'основна', 10);
insert into cards (height, weight, medical_group, patient_id) values (164, 49.6, 'основна', 11);
insert into cards (height, weight, medical_group, patient_id) values (165, 56.6, 'підготовча', 12);
insert into cards (height, weight, medical_group, patient_id) values (166, 49.2, 'основна', 13);
insert into cards (height, weight, medical_group, patient_id) values (188, 84.4, 'підготовча', 14);
insert into cards (height, weight, medical_group, patient_id) values (162, 52, 'підготовча', 15);
insert into cards (height, weight, medical_group, patient_id) values (176, 70, 'основна', 16);

# applications
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values ('виразка', 'стац-лікування', 2, 1, 3);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values ('вивих ліктя', 'консультація', 7, 2, 1);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values (null, 'консультація', 1, 3, 2);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values (null, 'дом-лікування', 2, 4, 4);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values (null, 'консультація', 2, 5, 3);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values (null, 'стац-лікування', 2, 6, 3);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values (null, 'консультація', 7, 7, 4);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values ('кір', 'консультація', 3, 8, 4);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values (null, 'дом-лікування', 7, 9, 1);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values (null, 'консультація', 2, 10, 1);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values ('передозування метамфітаміном', 'стац-лікування', 4, 11, 2);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values (null, 'стац-лікування', 6, 12, 2);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values (null, 'консультація', 7, 13, 3);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values ('рак кишківника', 'стац-лікування', 5, 14, 3);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values (null, 'дом-лікування', 7, 15, 1);
insert into applications (possible_diagnosis, service_type, doctor_id, patient_id, admin_id) values (null, 'консультація', 5, 16, 4);

# conclusions
insert into conclusions (established_diagnosis, treatment_method, sum_to_pay, application_id) values ('гастрит', 'таблетки', 1580, 1);
insert into conclusions (established_diagnosis, treatment_method, sum_to_pay, application_id) values ('вітрянка', 'крапельниця', 2860, 8);
insert into conclusions (established_diagnosis, treatment_method, sum_to_pay, application_id) values ('перелом пальця', 'гіпсування', 400, 9);