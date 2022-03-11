-- Script that lists genres of Dexter show.
-- Query that joins tables.
SELECT tv.title
       FROM tv_show_genres AS tvg
       LEFT JOIN tv_shows AS tv
       ON tvg.show_id = tv.id
       LEFT JOIN tv_genres AS g
       ON g.id = tvg.genre_id
       WHERE g.name = "Comedy"
       ORDER BY tv.title ASC;
