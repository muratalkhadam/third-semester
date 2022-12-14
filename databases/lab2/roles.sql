use `db-labs`;


create role if not exists doctor, admin;

grant update, select on cards to doctor;
grant insert, select, delete on conclusions to doctor;
grant select on * to doctor;

grant insert, select, delete on applications to admin;
grant insert, select, delete on cards to admin;
grant insert, select, delete on conclusions to admin;
grant update, insert, select on discounts to admin;
grant update, insert, select on doctors to admin;
grant update, insert, select on patients to admin;
grant select on admins to admin;

create user if not exists doctor123 identified by 'test1';
grant doctor to doctor123;

create user if not exists admin123 identified by 'test2';
grant admin to admin123;
