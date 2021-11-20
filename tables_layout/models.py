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
                             default="BUSY")

    def __str__(self):
        return f"{self.pk} - {self.state}"
