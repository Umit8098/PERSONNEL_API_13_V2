from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=32)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Personnel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    GENDER = (
        ("F", "Female",),
        ("M", "Male"),
        ("O", "Other"),
        ("N", "Prefer Not Say"),
    )
    gender = models.CharField(max_length=19, choices=GENDER)
        
    TITLE = (
        ("S", "Senior"),
        ("M", "Mid Senior"),
        ("J", "Junior"),
    )
    title = models.CharField(max_length=15, choices=TITLE)
    salary = models.IntegerField(default=1250)
    started = models.DateTimeField()
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="personnel")
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="personnels")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
