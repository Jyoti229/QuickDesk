from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, Comment
from .forms import TicketForm, CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user
    if user.role == 'agent':
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(created_by=user)
    return render(request, 'helpdesk/dashboard.html', {'tickets': tickets})

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            return redirect('dashboard')
    else:
        form = TicketForm()
    return render(request, 'helpdesk/create_ticket.html', {'form': form})

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    comments = ticket.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.author = request.user
            comment.save()
            return redirect('ticket_detail', ticket_id=ticket_id)
    else:
        form = CommentForm()
    return render(request, 'helpdesk/ticket_detail.html', {
        'ticket': ticket,
        'comments': comments,
        'form': form
    })

def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'ticket_list.html', {'tickets': tickets})

def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    return render(request, 'ticket_detail.html', {'ticket': ticket})
from django.shortcuts import render
from .models import Ticket  # make sure Ticket model is imported
from django.contrib.auth.decorators import login_required

@login_required
def view_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user).order_by('-created_at')
    return render(request, 'view_tickets.html', {'tickets': tickets})