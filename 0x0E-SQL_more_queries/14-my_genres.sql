-- Script that lists genres of Dexter show.
-- Query to join tables.
SELECT g.name
       FROM tv_show_genres AS tvg
       INNER JOIN tv_shows AS tv
       ON tvg.show_id = tv.id
       INNER JOIN tv_genres AS g
       ON g.id = tvg.genre_id
       WHERE tv.title = "Dexter"
       ORDER BY g.name ASC;
