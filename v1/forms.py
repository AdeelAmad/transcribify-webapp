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
            if self.instance.user:
                if self.instance.user.groups.filter(name='premium').exists():
                    max_file_size = settings.MAX_FILE_SIZE_PREMIUM
                    error_message = "File size must be less than 50MB"
                else:
                    max_file_size = settings.MAX_FILE_SIZE_BASIC
                    error_message = "File size must be less than 5MB"
            else:
                max_file_size = settings.MAX_FILE_SIZE_FREE
                error_message = "File size must be less than 2.5MB"

            if file_size > max_file_size:
                raise forms.ValidationError(error_message)
        return file