# movie_api/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Showtime
from .serializers import ShowtimeSerializer

class ReserveSeat(APIView):
    def post(self, request, showtime_id):
        showtime = Showtime.objects.get(pk=showtime_id)
        num_seats_to_reserve = request.data.get('num_seats', 1)
        
        if num_seats_to_reserve <= 0:
            return Response({"error": "Invalid number of seats"}, status=status.HTTP_400_BAD_REQUEST)
        
        if showtime.available_seats < num_seats_to_reserve:
            return Response({"error": "Not enough available seats"}, status=status.HTTP_400_BAD_REQUEST)
        
        showtime.available_seats -= num_seats_to_reserve
        showtime.save()
        
        return Response({"success": f"{num_seats_to_reserve} seats reserved successfully"}, status=status.HTTP_200_OK)

class PurchaseTicket(APIView):
    def post(self, request, showtime_id):
        showtime = Showtime.objects.get(pk=showtime_id)
        num_tickets_to_purchase = request.data.get('num_tickets', 1)
        
        if num_tickets_to_purchase <= 0:
            return Response({"error": "Invalid number of tickets"}, status=status.HTTP_400_BAD_REQUEST)
        
        if showtime.available_seats < num_tickets_to_purchase:
            return Response({"error": "Not enough available seats"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Here you can implement ticket purchase logic, like storing ticket information in database, sending confirmation email, etc.
        # For simplicity, we'll just return a success message
        return Response({"success": f"{num_tickets_to_purchase} tickets purchased successfully"}, status=status.HTTP_200_OK)
