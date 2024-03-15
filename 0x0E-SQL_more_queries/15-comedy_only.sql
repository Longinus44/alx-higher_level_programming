-- Selecting show titles of Comedy shows from the tv_shows table
-- Joining tv_shows table with tv_show_genres table based on show_id
-- Joining tv_show_genres table with tv_genres table based on genre_id to filter Comedy genre
-- Filtering records where genre name is Comedy
-- Ordering the results in ascending order by show title

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
