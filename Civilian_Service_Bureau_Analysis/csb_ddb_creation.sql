.mode csv
.import "C:\\Users\\windows_user_name\\Downloads\\csb\\2022.csv" csb_2022
.import "C:\\Users\\windows_user_name\\Downloads\\csb\\2021.csv" csb_2021
.import "C:\\Users\\windows_user_name\\Downloads\\csb\\2020.csv" csb_2020
.import "C:\\Users\\windows_user_name\\Downloads\\csb\\2019.csv" csb_2019
.import "C:\\Users\\windows_user_name\\Downloads\\csb\\2018.csv" csb_2018
.import "C:\\Users\\windows_user_name\\Downloads\\csb\\2017.csv" csb_2017
.import "C:\\Users\\windows_user_name\\Downloads\\csb\\2016.csv" csb_2016
.import "C:\\Users\\windows_user_name\\Downloads\\csb\\2015.csv" csb_2015
.import "C:\\Users\\windows_user_name\\Downloads\\csb\\2014.csv" csb_2014
.import "C:\\Users\\windows_user_name\\Downloads\\csb\\2013.csv" csb_2013
.import "C:\\Users\\windows_user_name\\Downloads\\csb\\2012.csv" csb_2012

create table csb_all as 
select * from csb_2022 union all
select * from csb_2021 union all
select * from csb_2020 union all
select * from csb_2019 union all
select * from csb_2018 union all
select * from csb_2017 union all
select * from csb_2016 union all
select * from csb_2015 union all
select * from csb_2014 union all
select * from csb_2013 union all
select * from csb_2012;

drop table csb_2022;
drop table csb_2021;
drop table csb_2020;
drop table csb_2019;
drop table csb_2018;
drop table csb_2017;
drop table csb_2016;
drop table csb_2015;
drop table csb_2014;
drop table csb_2013;
drop table csb_2012;

update csb_all set DATETIMEINIT = null where DATETIMECLOSED = '';
update csb_all set DATETIMECLOSED = null where DATETIMECLOSED = '';
alter table csb_all alter column DATETIMECLOSED set data type datetime;
alter table csb_all alter column DATETIMEINIT set data type datetime;
alter table csb_all add column time_to_complete DOUBLE;
alter table csb_all add column datecreated date;
alter table csb_all add column dateclosed date;
update csb_all set time_to_complete = round(CAST(DATE_SUB('SECOND',DATETIMEINIT,DATETIMECLOSED) AS DOUBLE)/60/60/24,2) where not DATETIMECLOSED is null;
update csb_all set datecreated = CAST(DATETIMEINIT AS DATE) where not DATETIMEINIT is null;
update csb_all set dateclosed = CAST(DATETIMECLOSED AS DATE) where not DATETIMECLOSED is null;
