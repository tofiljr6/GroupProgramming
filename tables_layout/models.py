from django.db import models


class Table(models.Model):
    States = (
        ("BUSY", "busy"),
        ("FREE", "free"),
        ("RESERVED", "reserved"),
    )
    id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=8,
                             choices=States,
                             default="FREE")
    x = models.IntegerField(default=500)
    y = models.IntegerField(default=500)

    def __str__(self):
        return f"{self.id} - {self.state}"
