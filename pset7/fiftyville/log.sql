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
select license_plate, minute from courthouse_security_logs
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

/* Check phone call records for calls less than a minute in duration that match a person with the above
license plate */
select distinct c.name as caller from people as c
where c.phone_number in (
	select caller from phone_calls
	where year = 2020
	and month = 7
	and day = 28
	and duration < 60 -- Durations are in seconds
)
and c.license_plate in (
	select license_plate from courthouse_security_logs
	where year = 2020
	and month = 7
	and day = 28
	and hour = 10
	and minute between 15 and 25
);
/* Result:
caller
-------
Roger
Russell
Evelyn
Ernest
*/

-- Check if any of the above was using an atm the morning of the theft
select name, atm_location, transaction_type, amount from atm_transactions
join bank_accounts on atm_transactions.account_number = bank_accounts.account_number
join people on bank_accounts.person_id = people.id
where name in ( 
	select distinct c.name as caller from people as c
	where c.phone_number in (
		select caller from phone_calls
		where year = 2020
		and month = 7
		and day = 28
		and duration < 60 -- Durations are in seconds
	)
	and c.license_plate in (
		select license_plate from courthouse_security_logs
		where year = 2020
		and month = 7
		and day = 28
		and hour = 10
		and minute between 15 and 25
		)
	)
and atm_location = "Fifer Street"
and year = 2020
and month = 7
and day = 28;
/* Result
Ernest - withdraw 50
Russell - withdraw 35
*/

-- Check for passengers on 8:20 flight to Heathrow
select name from people
join passengers on passengers.passport_number = people.passport_number
join flights on flights.id = passengers.flight_id
join airports as o on o.id = flights.origin_airport_id
join airports as d on d.id = flights.destination_airport_id
where name in (
	 
select name from atm_transactions
join bank_accounts on atm_transactions.account_number = bank_accounts.account_number
join people on bank_accounts.person_id = people.id
where name in ( 
	select distinct c.name as caller from people as c
	where c.phone_number in (
		select caller from phone_calls
		where year = 2020
		and month = 7
		and day = 28
		and duration < 60 -- Durations are in seconds
	)
	and c.license_plate in (
		select license_plate from courthouse_security_logs
		where year = 2020
		and month = 7
		and day = 28
		and hour = 10
		and minute between 15 and 25
		)
	)
and atm_location = "Fifer Street"
and year = 2020
and month = 7
and day = 28
)
and flights.origin_airport_id = (
	select id from airports
	where city = "Fiftyville"
)
and  flights.destination_airport_id = (
	select id from airports
	where city = "London"
)
and flights.day = 29
and flights.month = 7
and flights.year = 2020
and flights.hour = 8
and flights.minute = 20;
/* Result
Ernest -- This is the thief
*/

-- Check people who recieved a call from Ernest less than 60 seconds in duration
select name from people
join phone_calls on phone_calls.receiver = people.phone_number
where phone_calls.caller = (
	select caller from phone_calls
	join people on phone_calls.caller = people.phone_number
	where name = "Ernest"
)
and year = 2020
and month = 7
and day = 28
and duration < 60;
/* Result
Berthold -- this is the accomplice
*/
