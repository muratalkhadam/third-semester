use `db-labs`;

alter table conclusions
    add column application_id int;

alter table applications
    add column doctor_id int;

alter table cards
    add column patient_id int;
alter table discounts
    add column patient_id int;
alter table applications
    add column patient_id int;

alter table applications
    add column admin_id int;