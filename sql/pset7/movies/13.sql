-- Select name from people table where the person_id matches conditions
select distinct name from people
join stars on stars.person_id = people.id
where stars.person_id in (
	-- Get person_id of everyone who stars in a movie with Kevin Bacon
	select person_id from stars 
	where movie_id in (
		-- Get movie_id from movies where Kevin Bacon stars
		select movie_id from stars 
		join people on stars.person_id = people.id
		where name = "Kevin Bacon" and birth = 1958
		)
	)
		-- Remove Kevin Bacon born in 1958 from result
		and people.id != (
			select id from people
			where name = "Kevin Bacon" and birth = 1958);

