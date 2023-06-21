-- this scipt groups by temperature
SELECT city, AVG(avg_temp) FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
