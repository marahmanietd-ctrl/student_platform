from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(validators=[MinValueValidator(16), MaxValueValidator(100)])
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    master_average = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(20)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
