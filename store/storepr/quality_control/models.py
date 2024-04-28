from django.db import models
from tasks.models import Project
from tasks.models import Task


class BugReport(models.Model):
    STATUS_CHOICES = [
        ('under consideration', 'В рассмотрении'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
    ]

    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Critical'),
        (5, 'Urgent'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='not selected'
    )

    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=0
    )

    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='bug_reports'
    )

    task = models.ForeignKey(
        to=Task,
        on_delete=models.SET_NULL,
        null=True,
        related_name='bug_reports'
    )


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('under consideration', 'В рассмотрении'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
    ]

    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
        (4, 'Critical'),
        (5, 'Urgent'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='not selected'
    )

    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=0
    )

    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='feature_requests',
    )

    task = models.ForeignKey(
        to=Task,
        on_delete=models.SET_NULL,
        null=True,
        related_name='feature_requests'
    )
