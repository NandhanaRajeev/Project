from django.db import models

# Create your models here.
class contactus(models.Model):
    name = models.CharField(blank=False,max_length=50)
    email = models.EmailField(blank=False,max_length=200)
    phone = models.IntegerField(blank=False)
    message = models.TextField(blank=False,max_length=250)

    def _str_(self):
        return str(self.name._str_())
