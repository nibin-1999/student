from django.db import models

class Day(models.Model):
    name=models.CharField(max_length=255)
    food = models.ManyToManyField("food.Food")

    def _str_(self):
        return self.name


class Food(models.Model):
    days=models.CharField(max_length=255,default="day1")
    breakfast=models.CharField(max_length=255)
    lunch=models.CharField(max_length=255)
    tea=models.CharField(max_length=255)
    dinner=models.CharField(max_length=255)

    def _str_(self):
        return self.days