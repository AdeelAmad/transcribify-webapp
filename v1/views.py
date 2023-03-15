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
            form.save(commit=False)
            return redirect('transcript', pk=form.pk)
    else:
        form = TranscriptForm()
    file_size = "5MB" if request.user.is_authenticated else "2.5MB"
    plan = "Free Account" if request.user.is_authenticated else "No Account"
    return render(request, 'v1/transcript_form.html', {'form': form, 'file_size': file_size, 'plan': plan})

class transcript(DetailView):
    model = transcript