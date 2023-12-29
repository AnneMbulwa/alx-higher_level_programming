-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title
SELECT DISTINCT title
FROM tv_shows JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id

JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title  NOT IN(
	SELECT title
	FROM tv_shows
	JOIN tv_show_genres
	ON tv_show_genres.show_id = tv_shows.id

	JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = "Comedy")
ORDER BY title;
