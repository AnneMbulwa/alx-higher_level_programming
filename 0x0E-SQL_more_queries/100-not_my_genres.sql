-- Script that  list all genres not linked to the show Dexter in hbtn_0d_tvshows database
-- Each record should display: tv_genres.name
SELECT DISTINCT name
FROM tv_genres JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.show_id

JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name NOT IN (
	SELECT name
	FROM tv_genres JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id

	JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = "Dexter")
ORDER BY tv_genres.name;
