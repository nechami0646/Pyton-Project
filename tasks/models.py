
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100) # שם הצוות

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('manager', 'מנהל'),
        ('employee', 'עובד'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"

class Task(models.Model):
    # הגדרת אפשרויות לסטטוס המשימה [cite: 11]
    STATUS_CHOICES = [
        ('new', 'חדש'),
        ('in_progress', 'בתהליך'),
        ('completed', 'הושלם'),
    ]

    title = models.CharField(max_length=200)  # שם המשימה [cite: 8]
    description = models.TextField()  # תיאור המשימה [cite: 9]
    due_date = models.DateField()  # תאריך יעד לסיום [cite: 10]

    # סטטוס עם ערך ברירת מחדל "חדש" [cite: 11]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    # קישור למשתמש שמבצע את המשימה [cite: 12]
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title