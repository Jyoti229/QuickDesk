from django.urls import path
from .views import (
    dashboard,
    create_ticket,
    ticket_list,
    ticket_detail,
    view_tickets
)

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),  # Admin or user dashboard
    path('create/', create_ticket, name='create_ticket'),  # Create new support ticket
    path('tickets/', ticket_list, name='ticket_list'),  # List all tickets (admin or support agent)
    path('ticket/<int:ticket_id>/', ticket_detail, name='ticket_detail'),  # View single ticket
    path('view-tickets/', view_tickets, name='view_tickets'),  # Logged-in user’s own tickets
]
