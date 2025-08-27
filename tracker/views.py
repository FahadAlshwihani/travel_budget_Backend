from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Trip, Expense  # Ensure your Trip model is imported
from .serializers import TripSerializer, ExpenseSerializer  # Ensure your serializers are imported
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes([AllowAny])
def create_trip(request):
    serializer = TripSerializer(data=request.data)
    if serializer.is_valid():
        trip = serializer.save()
        return Response({'code': trip.code, 'trip': serializer.data},
                        status=status.HTTP_201_CREATED)
    print("Validation Errors:", serializer.errors)  # 👈 ADD THIS LINE
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])  # Allow unauthenticated access
def get_trip_by_code(request, code):
    """Get trip details by its code without authentication"""
    try:
        trip = Trip.objects.get(code=code)
        serializer = TripSerializer(trip)
        return Response(serializer.data)
    except Trip.DoesNotExist:
        return Response({'error': 'Trip not found'},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def expenses_by_trip_id(request, trip_id):
    if request.method == 'GET':
        expenses = Expense.objects.filter(trip__id=trip_id)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            trip = Trip.objects.get(id=trip_id)
        except Trip.DoesNotExist:
            return Response({'error': 'Trip not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(trip=trip)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Add this print to see validation errors
        print("Expense validation errors:", serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_expense(request, trip_id, expense_id):
    try:
        expense = Expense.objects.get(id=expense_id, trip__id=trip_id)
        expense.delete()
        return Response({'message': 'Expense deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Expense.DoesNotExist:
        return Response({'error': 'Expense not found'}, status=status.HTTP_404_NOT_FOUND)
