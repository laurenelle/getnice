from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
  first_name = models.CharField(max_length=120, null=False, blank=False)
  last_name = models.CharField(max_length=120, null=False, blank=False)
  # default is false for email field
  email = models.EmailField()
  timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)

  def __unicode__(self):
    return smart_unicode(self.email)