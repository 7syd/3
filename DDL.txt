create database company;
use company;
create table salesman (
salesman_id int(5) not null, salesman_name varchar(20) not null, salesman_address varchar(30), company_name char(10),date_of_join date not null, product_name char(20), product_id int(5), age int(3) not null, salary int(8) not null);
desc salesman;
insert into salesman values
(120, "Sid", "Der", "Mon", "2022-03-04", "Bb", 957, 24, 17000),
 (125, "Anish", "Con", "Cdl", "2020-04-09", "pp", 999, 22, 17000),
 (130, "Arin", "Del", "Wes", "2020-08-04", "ee", 900, 24, 17000),
  (101, "Yash", "Sw", "Dts", "2021-03-12", "Dd", 940, 25, 17000);

select * from salesman;
start transaction;
delete from salesman where salesman_id = 101;
select * from salesman;
rollback;
alter table salesman add CONSTRAINT uc_salesman_name UNIQUE(salesman_name);
alter table salesman add CONSTRAINT pk_salesman_id PRIMARY KEY(salesman_id);
alter table salesman add (age int(2)), add constraint chk_age check (age>=18);
alter table salesman alter salary set default (17000);
desc salesman;
create view s_view as select salesman_id, salesman_name, salary from salesman;
select * from s_view;
select count(salary) as count_rows from salesman;
select max(salary) as max_salary from salesman;
select min(salary) as min_salary from salesman;
select avg(salary) as avg_salary from salesman;
create table t1 (s_id int, s_name varchar(30), salary int(8));
insert into t1 values(1, "Aryan", 170000),
(2, "Sid", 170000),
(3, "Anish", 150000),
(4, "Arin", 120000);
create table t2 (s_id int, s_name varchar(30), salary int(8));
 insert into t2 values (1, "Aryan", 170000),
(5, "Yash", 120000),
(6, "Raj", 130000);
select * from t2;
select * from t1;
select * from t1 union select * from t2;
select * from t1 union all select * from t2;
create synonym employee as salesman;
truncate salesman;
drop table salesman;
drop database company;
