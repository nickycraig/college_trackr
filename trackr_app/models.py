from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class School(models.Model):
    name = models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    size = models.IntegerField(default=0)
    public_private = models.CharField(max_length=100)
    research_class = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    notes =models.CharField(max_length=1500)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="schools")

    def __str__(self):
        return self.name