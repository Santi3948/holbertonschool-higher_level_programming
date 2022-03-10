-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT name AS genre, COUNT(genre_id) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NOT NULL
GROUP BY genre
ORDER BY number_of_shows DESC
