from django.contrib import admin

from .models import NoteModel

class NoteModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'Done']
    fieldsets = [
        ('Product Data', {'fields':['title' , 'description','Done']}),
    ]
admin.site.register(NoteModel , NoteModelAdmin)