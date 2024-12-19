from django.db import models


class MoodOfTheDay(models.Model):
    person_name = models.CharField(max_length=32)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    mood = models.IntegerField()

    def __str__(self):
        return (
            f"{self.person_name} set its mood to {self.mood} on {self.year}"
        )
