
# TicketApp/forms.py
from django import forms
from .models import Ticket, Comment

# Ticket Form
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'assigned_engineer', 'status']

# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
