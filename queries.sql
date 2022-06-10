SELECT count(Seat_ID) as total_seats FROM seats;

SELECT Customer_name as customers FROM customers;

SELECT empl.Employee_name as employee, super.Employee_name as supervisor FROM employees as empl, employees as super
WHERE empl.Supervisor_ID = super.Employee_ID OR empl.Supervisor_ID IS NULL AND empl.Employee_ID = super.Employee_ID;

SELECT ROUND(SUM(Movie_price), 2) as gross_profit FROM movies, bookings, showings
WHERE bookings.Showing_ID = showings.Showing_ID AND showings.Movie_ID = movies.Movie_ID;

SELECT Movie_name as movie, Theater_ID as theater, DATE_FORMAT(Showing_time, '%m/%d') as date, DATE_FORMAT(Showing_time, '%h:%i %p') as time FROM showings, movies
WHERE DATE_FORMAT(Showing_time, '%m/%d') = '05/09' AND showings.Movie_ID = movies.Movie_ID AND Theater_ID = 2
ORDER BY Showing_time;