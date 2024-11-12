# TicketApp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket,Comment
from .forms import TicketForm, CommentForm

# View for listing all tickets
@login_required
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'TicketApp/templates/tickets_list.html', {'tickets': tickets})


# View for creating a new ticket
@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creator = request.user
            ticket.save()
            return redirect('tickets_list')
    else:
        form = TicketForm()
    return render(request, 'TicketApp/templates/create_ticket.html', {'form': form})

# View for viewing a single ticket's details
@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    comments = ticket.comments.all()
    comment_form = CommentForm()

    return render(request, 'TicketApp/ticket_detail.html', {
        'ticket': ticket,
        'comment': comments,
        'comment_form': comment_form
    })

# View for updating ticket status
@login_required
def update_status(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket.status = request.POST.get('status')
        ticket.save()
        return redirect('ticket_detail', ticket_id=ticket_id)
    return render(request, 'TticketApp/update_status.html', {'ticket': ticket})

# View for adding a comment to a ticket
@login_required
def add_comment(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.user = request.user
            comment.save()
            return redirect('ticket_detail', ticket_id=ticket_id)
    return redirect('ticket_detail', ticket_id=ticket_id)

# TicketApp/views.py

def home(request):
    return render(request, 'home.html')  # Assuming you have a home.html template


from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class CustomLoginView(auth_views.LoginView):
    template_name = 'TicketApp/login.html'
    success_url = reverse_lazy('home')
