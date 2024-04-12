# Online-Ticket-Booking-System

Introduction
Welcome to the Movie Ticket Booking System API. This API allows users to browse available movies, view showtimes, reserve seats, and purchase tickets.

Authentication
Authentication is required for certain endpoints. You need to obtain a JSON Web Token (JWT) by logging in as a user. Use the JWT token in the Authorization header for authenticated requests.

Endpoints
Available Movies
URL: /movies/
Method: GET
Description: Get a list of available movies.
Response:
200 OK: Returns a list of movies with details.
401 Unauthorized: Authentication credentials were not provided or invalid.
Movie Details
URL: /movies/<movie_id>/
Method: GET
Description: Get details of a specific movie, including showtimes.
Response:
200 OK: Returns details of the movie with showtimes.
404 Not Found: The specified movie ID does not exist.
Showtime Reservation
URL: /showtimes/<showtime_id>/reserve/
Method: POST
Description: Reserve seats for a specific showtime.
Request Body:
json
Copy code
{
    "num_seats": 2
}
Response:
200 OK: Seats reserved successfully.
400 Bad Request: Invalid request or not enough available seats.
401 Unauthorized: Authentication credentials were not provided or invalid.
Ticket Purchase
URL: /showtimes/<showtime_id>/purchase/
Method: POST
Description: Purchase tickets for a specific showtime.
Request Body:
json
Copy code
{
    "num_tickets": 2
}
Response:
200 OK: Tickets purchased successfully.
400 Bad Request: Invalid request or not enough available seats.
401 Unauthorized: Authentication credentials were not provided or invalid.
