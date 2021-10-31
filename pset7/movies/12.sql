select title from movies 
join stars on movies.id = stars.movie_id
join people on stars.person_id = people.id
where people.name = "Johnny Depp"

intersect

select title from movies 
join stars on movies.id = stars.movie_id
join people on stars.person_id = people.id
where people.name = "Helena Bonham Carter";
