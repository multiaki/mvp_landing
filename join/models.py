from django.db import models

# Create your models here.
class Join(models.Model):
    email = models.EmailField(max_length=250)
    fullname = models.CharField(max_length=250, blank=True)
    zip_code = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __unicode__(self):
        return self.email