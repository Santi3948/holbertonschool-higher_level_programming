-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT title, genre_id FROM tv_shows
RIGHT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY title, genre_id
