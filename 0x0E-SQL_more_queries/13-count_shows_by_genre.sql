--lists all genres from hbtn_0d_tvshows,displays number of shows linked to each
--First column must be called genre
--Second column must be called number_of_shows
--Don’t display a genre that doesn’t have any shows linked
USE hbtn_0d_tvshows;
SELECT genres.genre as genre, COUNT(tv_show_genres.tv_show_id) as number_of_shows
FROM genres LEFT JOIN tv_show_genres
ON genres.id = tv_show_genres.genre_id
GROUP BY genres.genre HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
