-- this script lists all the cities
SELECT id, name FROM cities
WHERE (SELECT id FROM states WHERE name = "California") = state_id;
