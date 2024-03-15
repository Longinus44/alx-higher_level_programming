-- Selecting city ID, city name, and state name from cities and states tables
-- Filtering records where city's state_id matches state's id
-- Ordering results by city ID in ascending order

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;

