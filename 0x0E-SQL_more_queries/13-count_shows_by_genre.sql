-- Selecting genre name and counting the number of shows linked to each genre
-- Joining tv_genres table with tv_show_genres table based on genre_id
-- Grouping the results by genre id to count the number of shows linked to each genre
-- Sorting the results in descending order by the number of shows linked to each genre

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;
