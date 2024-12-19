from django.db import models


class MoodOfTheDay(models.Model):
    person_name = models.CharField(max_length=32)
    date = models.DateField()
    mood = models.IntegerField()

    def __str__(self):
        return f"{self.person_name} set its mood to {self.mood} on {self.date.isoformat()}"
