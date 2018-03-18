from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()

class Action(models.Model):
    user = models.ForeignKey(User, related_name='actions', db_index=True, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    target_content_type = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name='target_object',
        on_delete=models.CASCADE
    )
    target_id = models.PositiveIntegerField(
        blank=True,
        null=True,
        db_index=True
    )
    target = GenericForeignKey('target_content_type', 'target_id')

    class Meta:
        ordering = ('-created_at',)
