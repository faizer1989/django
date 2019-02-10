from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # models.Model means that the Post is a Django Model, so Django knows that it
    # should be saved in the database.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.ForeignKey - this is a link to another model
    title = models.CharField(max_length=200)
    # models.CharField this is how you define text with limited number of charactersself.

    text = models.TextField()
    # this is for long text without a limit
    created_date = models.DateTimeField(default=timezone.now)
    # models.DateTimeField - this is a date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
