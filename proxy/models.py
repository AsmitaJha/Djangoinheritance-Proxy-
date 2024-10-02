from django.db import models

'''
Creating 3 models:
a. Cafe as the parent model with 2 fields: name and orders(number of orders)
b. Cake as the first child model with no field as it is a **proxy** model since it has 'proxy=True' in class 'Meta' along with ordering based on 'orders'.
c. ColdDrink as the second child model with no field being **proxy** mode as seen in 'Meta' class with no ordering'''
class Cafe(models.Model):
    name=models.CharField(max_length=50)
    orders=models.IntegerField()
    
class Cake(Cafe):
    class Meta:
        proxy=True
        ordering=["orders"]
        
class ColdDrink(Cafe):
    class Meta:
        proxy=True
        
#Differences from Abstract Base Classes and Multitable inheritance: Both the other models can have extra fields in their child class unlike proxy. other differences are:
'''
a. Abstract Base Classes: It has 'abstract=True' in parent class. The parent model is not created whereas in proxy model, parent model is also created similar to multitable inheritance, and the 'proxy=True' is in the 'meta' class of child model
b. Multitable inheritance: It doesn't need any meta class showing 'something=True' but proxy model has 'proxy=True' in the 'meta' class of its child models. 

'''