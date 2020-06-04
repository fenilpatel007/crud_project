from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullName = models.CharField(max_length=255)
    empCode = models.CharField(max_length=3)
    mobileNo = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
