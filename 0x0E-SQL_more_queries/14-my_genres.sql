-- Script that uses the hbtn_0d_tvshows database to lists all 
-- Genres of the show Dexter.
-- Record display:tv_genres.name sorted in ascending order by the genre name
SELECT tv_genres.name FROM tv_shows JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.tv_show_id JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name ASC;
