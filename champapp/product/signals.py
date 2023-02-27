from django.db.models.signals import pre_save
from product.models import ProductModel
import random   
import string


def generate_random_string(length):
    letters = string.ascii_letters
    Char = ''.join(random.choice(letters) for i in range(length))
    return Char



def product_code_generator(sender, instance, **kwargs):
    Char = generate_random_string(3)
    number = random.randint(100, 999)
    instance.code = Char + str(number) + "-" + str(instance.id )
pre_save.connect(product_code_generator,sender=ProductModel)