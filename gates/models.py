from django.db import models
from datetime import datetime



type_choices= [
    ('sliding-gates','sliding gates'),
    ('swinging-gates','swinging gates'),
    ('garage-gates','garage gates'),
    ('CCTV','CCTV'),
    ('Flood-Lights','Flood Lights'),
    ]
   
class items(models.Model):
    image =models.ImageField(upload_to='photos',help_text="min:dimension 250px by 250 px")
    title = models.CharField(max_length=200)
    description = models.TextField()
    types= models.CharField(max_length=120, choices= type_choices)
    datepost = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(unique=True,max_length=100)

    def __str__(self):
        return self.types
    


    class Meta:
        ordering = ['-datepost']


