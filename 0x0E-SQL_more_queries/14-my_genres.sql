-- Selecting genre names of the show Dexter from the tv_genres table
-- Joining tv_genres table with tv_show_genres table based on genre_id
-- Joining tv_show_genres table with tv_shows table based on show_id to filter the show Dexter
-- Filtering records where show title is Dexter
-- Ordering the results in ascending order by genre name

SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
