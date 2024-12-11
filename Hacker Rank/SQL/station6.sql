-- weather observation station 6

select city from station where regexp_like(city, '^[aeiou]');
