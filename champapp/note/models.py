from django.db import models





class NoteModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    Done = models.BooleanField(default=False)