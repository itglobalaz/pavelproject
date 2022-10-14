from django.db import models


class ProjectStatus(models.TextChoices):
    OPEN = 'Open'
    IN_PROGRESS = 'In progress'
    CHECKING = 'Checking'
    CLOSED = 'Closed'
