from django.core.exceptions import ValidationError

class FileSizeValidator:

    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        if value.size > self.max_size:
            raise ValidationError('File too large. Size should not exceed 2.5 MB.')