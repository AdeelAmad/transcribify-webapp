from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView

from v1.forms import TranscriptForm
from v1.models import transcript


def upload(request):
    if request.method == 'POST':
        form = TranscriptForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            form.instance.user = request.user
        else:
            form.instance.user = None
        if form.is_valid():
            t = form.save()
            return redirect('transcript', pk=t.pk)
    else:
        form = TranscriptForm()
    if request.user.is_authenticated:
        if request.user.groups.filter(name='premium').exists():
            plan = "Premium"
            file_size = "50MB"
        else:
            plan = "Basic"
            file_size = "5MB"
    else:
        plan = "Free"
        file_size = "2.5MB"

    return render(request, 'v1/transcript_form.html', {'form': form, 'file_size': file_size, 'plan': plan})

class transcript(DetailView):
    model = transcript