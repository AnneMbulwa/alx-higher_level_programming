-- Llists all genres from hbtn_0d_tvshows,displays number of shows linked to each
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
