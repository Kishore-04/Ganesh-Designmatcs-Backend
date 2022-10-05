from django.db import models
# Create your models here.
class Logo(models.Model):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.company_name