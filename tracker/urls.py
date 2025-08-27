from django.urls import path
from .views import create_trip, get_trip_by_code, expenses_by_trip_id, delete_expense

urlpatterns = [
    path('trips/', create_trip, name='create_trip'),
    path('trips/<str:code>/', get_trip_by_code, name='get_trip_by_code'),
    path('trips/<int:trip_id>/expenses/', expenses_by_trip_id, name='expenses_by_trip_id'),
    path('trips/<int:trip_id>/expenses/<int:expense_id>/', delete_expense, name='delete_expense')

]
