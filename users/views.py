from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from users.forms import UserRegisterForm
from v1.models import transcript


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    context = {}
    context['transcripts'] = []
    for t in transcript.objects.all().filter(user=request.user):
        id = t.id
        timestamp = t.timestamp
        language = t.language
        transcription_method = t.transcription_method

        context['transcripts'].append({'id': id, 'timestamp': timestamp, 'language': language, 'transcription_method': transcription_method})

    return render(request, 'v1/transcript_list.html', context=context)

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    messages.success(request, f'You have been logged out!')
    return redirect('upload')


class list(LoginRequiredMixin, ListView):
    model = transcript
