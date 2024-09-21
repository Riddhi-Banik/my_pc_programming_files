from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    section = models.CharField(max_length=2)
    gpa = models.FloatField()
    photo = models.ImageField(upload_to='img/%y')

    def __str__(self) -> str:
        return self.name


