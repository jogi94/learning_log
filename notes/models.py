from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


# Create your models here.


class Topic(TimeStampedModel):
    """ A Topic the user is learning about"""
    name = models.CharField(max_length=200, help_text="Enter Topic Name?")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    def get_create_url(self):
        return reverse("notes:topic_create")

    def get_absolute_url(self):
        return reverse("notes:topic_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("notes:topic_update", args=(self.id,))

    def get_delete_url(self):
        return reverse("notes:topic_delete", args=(self.id,))


class Entry(models.Model):
    """Something Specific learned about topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        return f'{self.text[:50]}...'

    @staticmethod
    def get_create_url(self):
        return reverse("notes:entry_create")

    def get_update_url(self):
        return reverse("notes:entry_update", args=(self.id,))

    def get_absolute_url(self):
        return reverse("notes:entry_detail", args=(self.id,))

    def get_delete_url(self):
        return reverse("notes:entry_delete", args=(self.id,))