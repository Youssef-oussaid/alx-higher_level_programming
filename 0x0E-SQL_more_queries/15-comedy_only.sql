-- lists all Comedy shows in the database
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_ genres.genre_id
JOIN tv_genres ON tv_show_genre.show_id = tv_genres.id
WHERE tv_genres = 'Comedy'
ORDER BY tv_shows.title ASC;
