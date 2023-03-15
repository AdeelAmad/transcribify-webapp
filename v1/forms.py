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
                error_message = "File size must be less than 5MB" if self.instance.user_id else "File size must be less than 2.5MB"
                raise forms.ValidationError(error_message)
        return file