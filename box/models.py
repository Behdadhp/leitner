from django.db import models


class LeitnerBox(models.Model):
    """ORM representation for the Leitner box"""

    word = models.CharField(max_length=50, blank=False, null=False)
    translate = models.CharField(max_length=50, blank=False, null=False)
    pronounce = models.CharField(max_length=50, blank=True, null=True)
    counter = models.IntegerField( blank=False, null=False)
    example = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.word
