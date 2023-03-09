from django.db.models.signals import post_save
from django.dispatch import receiver
from v1.models import transcript
from v1.tasks import transcribe_audio

@receiver(post_save, sender=transcript)
def transcript_save(sender, instance, created, **kwargs):
    if created:
        transcribe_audio.apply_async(args=[instance.file.name, instance.id])