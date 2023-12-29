-- Script that uses the hbtn_0d_tvshows database to lists all 
-- Genres of the show Dexter.
-- Record display:tv_genres.name sorted in ascending order by the genre name
SELECT tv_genres.name FROM tv_genres JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id JOIN tv_shows
ON tv_shows.id = tv_shows.show_id
WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name ASC;
