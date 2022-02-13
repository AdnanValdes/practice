select avg(rating) from ratings join movies on ratings.movie_id = movies.id where movies.year = 2012;
