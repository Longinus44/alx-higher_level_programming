-- Selecting show titles and genre names from the tv_shows and tv_genres tables
-- Performing a LEFT JOIN operation between tv_shows and tv_show_genres tables to ensure all shows are included
-- Joining tv_show_genres with tv_genres to get the genre names
-- Using IFNULL function to display 'NULL' for genre name if a show doesn't have a genre linked
-- Ordering the results in ascending order by the show title and genre name


SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS genre
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, genre ASC;
