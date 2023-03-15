from django import forms

from WhisperApp import settings
from v1.models import transcript


class TranscriptForm(forms.ModelForm):
    class Meta:
        model = transcript
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data['file']
        if file:
            file_size = file.size
            max_file_size = settings.MAX_FILE_SIZE_LOGGED_IN if self.instance.user_id else settings.MAX_FILE_SIZE_NOT_LOGGED_IN
            if file_size > max_file_size:
                raise forms.ValidationError("File size must be less than %s" % max_file_size)
        return file