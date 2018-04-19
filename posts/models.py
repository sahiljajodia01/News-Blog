from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# def upload_location(instance, filename):
#     return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    image = models.FileField(upload_to='images/',
        null=True,
        blank=True,
        # height_field='height_field',
        # width_field='width_field'
        )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='token')
    token = models.CharField(max_length=200, null=True, blank=True)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return self.token
