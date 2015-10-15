from django.db.models import Q
from django.views.generic import TemplateView

from events.models import Event

from .models import Instructor, Group


class DanceView(TemplateView):
    template_name = "dance/dance.html"

    def get_context_data(self, **kwargs):
        context = super(DanceView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(type__startswith='dance')
        context['show_events'] = Event.objects.filter(type__exact="dance show")
        context['instructors'] = Instructor.objects.filter(Q(gender__exact='M') | Q(partner__isnull=True)).distinct()
        context['groups'] = Group.objects.all()
        return context
