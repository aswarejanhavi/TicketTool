
# TicketApp/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.ticket_list, name='ticket_list'),  # Direct access to ticket_list from the root URL
#     path('create/', views.create_ticket, name='create_ticket'),
#     path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
#     path('ticket/<int:ticket_id>/update_status/', views.update_ticket_status, name='update_ticket_status'),
#     path('ticket/<int:ticket_id>/add_comment/', views.add_comment, name='add_comment'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),  # Your main view
    path('create/', views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('ticket/<int:ticket_id>/update_status/', views.update_status, name='update_ticket_status'),
    path('ticket/<int:ticket_id>/add_comment/', views.add_comment, name='add_comment'),
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Login URL
]
