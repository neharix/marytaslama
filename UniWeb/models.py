from django.db import models


class Campus(models.Model):
    name = models.CharField(max_length=250)
    capacity = models.IntegerField()

    class Meta:
        verbose_name = "UÝJ"
        verbose_name_plural = "UÝJ-lar"

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=250)
    first_year_students = models.IntegerField()
    second_year_students = models.IntegerField()
    third_year_students = models.IntegerField()
    fourth_year_students = models.IntegerField()
    fifth_year_students = models.IntegerField()

    class Meta:
        verbose_name = "fakultet"
        verbose_name_plural = "fakultetler"

    def __str__(self):
        return self.name
