use `db-labs`;

alter table conclusions
add constraint fk_conclusions_application_id
foreign key (application_id)
references applications(application_id)
on delete cascade;

alter table cards
add constraint fk_cards_patient_id
foreign key (patient_id)
references patients(patient_id)
on delete cascade;

alter table discounts
add constraint fk_discounts_patient_id
foreign key (patient_id)
references patients(patient_id)
on delete cascade;


alter table applications
add constraint fk_applications_patient_id
foreign key (patient_id)
references patients(patient_id)
on delete cascade;

alter table applications
add constraint fk_applications_doctor_id
foreign key (doctor_id)
references doctors(doctor_id)
on delete cascade;

alter table applications
add constraint fk_applications_admin_id
foreign key (admin_id)
references admins(admin_id)
on delete cascade;