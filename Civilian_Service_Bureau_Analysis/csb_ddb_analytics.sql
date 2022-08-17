#Ward TTC
.output "C:\\Users\\legis\\OneDrive\\Documents\\CSB Project\\ward_ttc.csv"
select date_trunc('month',dateclosed) as closedmonth,
ward,
avg(time_to_complete) as avg_time_to_complete,
count(REQUESTID) as request_count
from csb_all
where not dateclosed is null
group by closedmonth, ward
order by closedmonth asc;

#Issue TTC
.output "C:\\Users\\legis\\OneDrive\\Documents\\CSB Project\\PROBLEMCODE_TTC.csv"
select date_trunc('month',dateclosed) as closedmonth,
	PROBLEMCODE, 
	avg(time_to_complete) AS avg_time_to_complete,
	count(REQUESTID) as request_count
from csb_all
where not dateclosed is null
group by closedmonth, PROBLEMCODE
order by closedmonth asc;

#Group TTC
.output "C:\\Users\\legis\\OneDrive\\Documents\\CSB Project\\group_TTC.csv"
select date_trunc('month',dateclosed) as closedmonth,
	csb_all.group, 
	avg(time_to_complete) AS avg_time_to_complete,
	count(REQUESTID) as request_count
from csb_all
where not dateclosed is null
group by closedmonth, csb_all.group
order by closedmonth asc;

#submitto TTC
.output "C:\\Users\\legis\\OneDrive\\Documents\\CSB Project\\SUBMITTO_TTC.csv"
select date_trunc('month',dateclosed) as closedmonth,
	csb_all.SUBMITTO, 
	avg(time_to_complete) AS avg_time_to_complete,
	count(REQUESTID) as request_count
from csb_all
where not dateclosed is null
group by closedmonth, csb_all.SUBMITTO
order by closedmonth asc;