from django import forms
from django.forms import fields, widgets
from core.models import Event

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'date', 'time', 'location', 'image')
        widgets = {
            'event_name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Event Name'
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Date'
            }),
            'time': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Time'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Location'
            }),
            
        }