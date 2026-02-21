from django.db import models

class Mentor(models.Model):
    mentor_id = models.AutoField(primary_key=True)
    mentor_name = models.CharField(max_length=100)
    mentor_email = models.EmailField(unique=True)
    
    
    def __str__(self):
        return self.mentor_name
