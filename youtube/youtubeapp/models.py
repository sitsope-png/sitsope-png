from django.db import models



# Create your models here.

class Language(models.Model):
    title = models.CharField(max_length=156)
    def __str__(self):
        return self.title


class Entry(models.Model):
    #name = models.CharField(max_length=124)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="")
    def __str__(self):
        return self.language




"""class Language(models.Model):
    title=models.CharField(max_length=100)
    class Meta:
        db_table='colors' 
    def __str__(self):
        return self.title"""