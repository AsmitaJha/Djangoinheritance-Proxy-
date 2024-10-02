from django.contrib import admin
from .models import Cafe, Cake, ColdDrink

# Register your models here.
admin.site.register(Cafe)
admin.site.register(Cake)
admin.site.register(ColdDrink)


#Both the child and parent models can be registered like multitable inheritance and unlike abstract base classes in which only child models can be registered.