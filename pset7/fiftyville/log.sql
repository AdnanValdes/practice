-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Find:
-- 	Thief | City thief escaped to | Accomplice
-- Crime notes: happened on July 28, 2020 on Chamberlin street

-- Start by looking at crime reports on July 28, 2020 on Chamberlin st
select * from crime_scene_reports 
where year = 2020 
and month = 7 
and day = 28 
and street = "Chamberlin Street";
-- Result: Duck was stolen at 10:15am from the Chamberlin St. courthouse. There were three witnesses present, and their interviews mention the courhouse.


-- Check interviews table and parse interview text for witnesses on July 28, 2020 who mention courthouse
select * from interviews
where year = 2020
and month = 7
and day = 28
and transcript like "%courthouse%";
/*Result:
Ruth: within 10 min of theft, thief got into car
Eugene: Saw thief at ATM on fifer street
Raymond: As thief left courhouse, made <1 min call about taking earlest flight on July 29, 2020 out of fiftyville. The other person bought ticket.
*/

-- Check security logs for vehicles that left within 10 min of theft (at hour 10, between minute 15 and 25)
select license_plane, minute from courthouse_security_logs
where year = 2020
and month = 7
and day = 28
and hour = 10
and minute between 15 and 25; -- For BETWEEN, start and end values are included
-- Possible license_plates
/*license_plate  minute*/
/*-------------  ------*/
/*5P2BI95        16*/
/*94KL13X        18*/
/*6P58WS2        18*/
/*4328GD8        19*/
/*G412CB7        20*/
/*L93JTIZ        21*/
/*322W7JE        23*/
/*0NTHK55        23*/

-- Find what is the earliest flight out of Fiftyville on July 29, 2020
select o.full_name as origin, d.full_name as destination, hour || "-" || minute as dep_time from flights
join airports as o on origin_airport_id= o.id
join airports as d on destination_airport_id=d.id
where origin_airport_id = (
	select id from airports
	where city = "Fiftyville"
)
and year = 2020
and month = 7
and day = 29
group by hour, minute
order by hour, minute
limit 1;
-- Result:
/*origin                       destination       dep_time*/
/*---------------------------  ----------------  --------*/
/*Fiftyville Regional Airport  Heathrow Airport  8-20*/




