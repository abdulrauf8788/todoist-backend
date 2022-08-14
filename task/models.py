from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("L", "Low"),
        ("M", "Medium"),
        ("H", "High"),
        ("C", "Critical")
    ]
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default="M")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_key = models.CharField(max_length=32)


    def __str__(self):
        return self.title[:16]
