-- Selecting title and genre_id from tv_shows and tv_show_genres tables
-- Filtering records where genre_id is NULL (show without a genre linked)
-- Ordering results by tv_shows.title in ascending order and tv_show_genres.genre_id in ascending order

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
