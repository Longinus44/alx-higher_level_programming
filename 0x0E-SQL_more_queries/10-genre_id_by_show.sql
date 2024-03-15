-- Selecting title and genre_id from tv_shows and tv_show_genres tables
-- Joining tv_shows with tv_show_genres based on their respective ids
-- Ordering results by title and genre_id in ascending order

SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows.tv_shows
INNER JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
