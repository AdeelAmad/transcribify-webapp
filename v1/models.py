import uuid
from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from v1.validators import FileSizeValidator

def generate_filename(instance, filename):
    """
    Generates a new filename for the uploaded file based on the current date/time.
    """
    extension = filename.split('.')[-1]
    new_filename = f'{instance.id}.{extension}'
    return f'transcripts/{new_filename}'

class transcript(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=2, default='en', blank=True)
    file = models.FileField(upload_to=generate_filename, validators=[FileExtensionValidator(['mp3', 'wav', 'm4a']),
                                                                     FileSizeValidator(2.5*1024*1024)])
    result_raw = models.TextField(blank=True, default='Processing... Check Back Soon\nMost Files Process in 1-2 Minutes')
    result_processed = models.TextField(blank=True, default='Processing... Check Back Soon\nMost Files Process in 1-2 Minutes')

    def get_absolute_url(self):
        return reverse('transcript', kwargs={'pk': self.pk})