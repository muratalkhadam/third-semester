drop database if exists `db-labs`;
create database `db-labs`;

use `db-labs`;

drop table if exists conclusions;
drop table if exists admins;
drop table if exists cards;
drop table if exists patients;
drop table if exists discounts;
drop table if exists applications;
drop table if exists doctors;

create table discounts
(
    discount_id int auto_increment,
    percentage  float,
    reason      varchar(20),
    primary key (discount_id)
);

create table cards
(
    card_id       int auto_increment,
    height        int,
    weight        float,
    medical_group varchar(20),
    primary key (card_id)
);

create table conclusions
(
    conclusion_id         int auto_increment,
    established_diagnosis varchar(40),
    treatment_method      varchar(20),
    sum_to_pay            double,
    primary key (conclusion_id)
);

create table patients
(
    patient_id     int auto_increment,
    first_name     varchar(20),
    last_name      varchar(20),
    birthday       date,
    gender         varchar(20),
    is_beneficiary boolean,
    primary key (patient_id)
);

create table admins
(
    admin_id         int auto_increment,
    first_name       varchar(20),
    last_name        varchar(20),
    regular_patients int,
    shift_number     int,
    primary key (admin_id)
);

create table applications
(
    application_id     int auto_increment,
    possible_diagnosis varchar(40),
    service_type       varchar(20),
    primary key (application_id)
);

create table doctors
(
    doctor_id          int auto_increment,
    first_name         varchar(20),
    last_name          varchar(20),
    working_start_date date,
    qualification      varchar(40),
    specialization     varchar(40),
    primary key (doctor_id)
);
