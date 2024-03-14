-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name
FROM cities AS c
LEFT JOIN states
ON c.state_id = states.id
ORDER BY c.id ASC;
