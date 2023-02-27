from django.db import models



def get_filename_ext(filepath):
    import os
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    import random
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}-{instance.title}{ext}"
    return f"product/{final_name}" 





class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to=upload_image_path)
    code = models.CharField(max_length=12)
    location = models.CharField(max_length=30)
    quantity = models.SmallIntegerField()
    producttype = models.CharField(max_length=30)
    def __str__(self):
        return self.title