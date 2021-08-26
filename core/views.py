from core.models import Event
from core.forms import EventCreationForm
from django.shortcuts import redirect, render
from django.views.generic.base import View

# Create your views here.
class HomeView(View):
    form_class = EventCreationForm
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        all_events = Event.objects.all()
        context = {'form': form, 'all_events': all_events}
        return render(request, self.template_name, context=context)

class EventCreate(View):
    form_class = EventCreationForm
    template_name = 'core/event_create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home_view')
        else:
            context = {'form': form}
            return render(request, self.template_name, context=context)      

class EventLike(View):
    def post(self, request, *args, **kwargs):
        event_id = kwargs.get('id')
        event = Event.objects.get(id=event_id)
        event.is_liked = True
        event.save()
        return redirect(request.META.get('HTTP_REFERER'))

class EventUnlike(View):
    def post(self, request, *args, **kwargs):
        event_id = kwargs.get('id')
        event = Event.objects.get(id=event_id)
        event.is_liked = False
        event.save()
        return redirect(request.META.get('HTTP_REFERER'))

