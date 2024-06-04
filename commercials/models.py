from django.db import models


class Brand(models.Model):
    brand = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.brand}'


class Unit(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.abbreviation}'
    

class Nutrient(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
class Content(models.Model):
    content = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.content}"



class Food(models.Model):
    CATEGORIES = (
        ('TINNED FOODS', 'TINNED FOODS'), 
        ('INSTANT STAPLES', 'INSTANT STAPLES'), 
        ('DAIRY & CREAMERS', 'DAIRY & CREAMERS'),
        ('OILS', 'OILS'),
        ('BISCUITS', 'BISCUITS'),
        ('BEVERAGES', 'BEVERAGES'),
        ('SPREADS, DRESSINGS & SAUCES', ' SPREADS, DRESSINGS & SAUCES'),
        ('GRAINS & CEREALS', 'GRAINS & CEREALS'),
        ('PASTA', 'PASTA'),
        ('INFANT FORMULAE', 'INFANT FORMULAE'),
        ('NUTRITION SUPPLEMENTS', 'NUTRITION SUPPLEMENTS'),
        ('SPICES', 'SPICES'),
    )
    categories = models.CharField(max_length=100, choices=CATEGORIES, blank=True)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    nutrients = models.ManyToManyField(Nutrient, through='FoodNutrient')
    content = models.ManyToManyField(Content, through='NutrientContent')
    
    
    def __str__(self):
        return f'{self.categories} - {self.name} - {self.brand}'



class FoodNutrient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('food', 'nutrient')

    def __str__(self):
        return f"{self.food.name} - {self.nutrient.name}: {self.amount} {self.unit}"
    
    

class NutrientContent(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('food', 'content')

    def __str__(self):
        return f"{self.food.name} - {self.content.content} - {self.amount} {self.unit}"