from django.db import models

# Create your models here.
class Text_Crawl_Line(models.Model):
    text=models.TextField()
    def __str__(self) -> str:
        return self.text