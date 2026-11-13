import uuid
from django.db import models


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workspace = models.UUIDField(db_index=True)
    restaurant = models.CharField(max_length=20)
    request_key = models.CharField(max_length=80)
    request_hash = models.CharField(max_length=64)
    items = models.JSONField()
    total = models.PositiveIntegerField()
    status = models.CharField(max_length=20, default='placed')
    revision = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['workspace', 'request_key'], name='one_order_per_request')]


class Event(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='events')
    status = models.CharField(max_length=20)
    actor = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
