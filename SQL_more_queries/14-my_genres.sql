-- random comments to be made so far

SELECT name FROM tv_genres
WHERE tv_genres.id in (
  SELECT genre_id FROM tv_show_genres
  WHERE show_id = (
    SELECT id FROM tv_shows
    WHERE tv_shows.title = 'Dexter')
);
