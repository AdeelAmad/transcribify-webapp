from django.shortcuts import render
from django.views.generic import DetailView, CreateView

from v1.models import transcript


# Create your views here.
class uploadAudio(CreateView):
    model = transcript
    fields = ['file']

    def form_valid(self, form):
        return super().form_valid(form)

class transcript(DetailView):
    model = transcript