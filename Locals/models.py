from django.db import models

# Create your models here.
class Unit(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.abbreviation}'


# class Category(models.Model):
#     CATEGORIES = (
#         ('ANIMAL PROTEINS', 'ANIMAL PROTEINS '), 
#         ('SOUP AND STEWS', 'SOUP AND STEWS'), 
#         ('PORRIDGES', 'PORRIDGES'),
#         ('LOCAL STAPLES', 'LOCAL STAPLES'),
#         ('FRUITS AND VEGETABLES', 'FRUITS AND VEGETABLES'),
#         ('NUTS AND LEGUMES', 'NUTS AND LEGUMES'),
#     )
#     categories = models.CharField(max_length=100, choices=CATEGORIES)
    
#     def __str__(self):
#         return f'{self.categories}'
    
#     class Meta:
#         verbose_name_plural = "Category"
        
        
class Label(models.Model):
    CATEGORIES = (
        ('ANIMAL PROTEINS', 'ANIMAL PROTEINS '), 
        ('SOUP AND STEWS', 'SOUP AND STEWS'), 
        ('PORRIDGES', 'PORRIDGES'),
        ('LOCAL STAPLES', 'LOCAL STAPLES'),
        ('FRUITS AND VEGETABLES', 'FRUITS AND VEGETABLES'),
        ('NUTS AND LEGUMES', 'NUTS AND LEGUMES'),
    )
    categories = models.CharField(max_length=100, choices=CATEGORIES, blank=True)
    # Category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    net_weight = models.FloatField(max_length=50, null=True, blank=True)
    net_weight_unit = models.ForeignKey(Unit, related_name='net_weight_unit', on_delete=models.SET_NULL, null=True, blank=True)
    serving_size = models.FloatField(max_length=50, null=True, blank=True)
    serving_size_unit = models.ForeignKey(Unit, related_name='serving_size_unit', on_delete=models.SET_NULL, null=True, blank=True)
    serving_quantity = models.FloatField(max_length=50, null=True, blank=True)
    serving_quantity_unit = models.ForeignKey(Unit, related_name='serving_quantity_unit', on_delete=models.SET_NULL, null=True, blank=True)
    per = models.FloatField(max_length=50, null=True, blank=True)
    per_unit = models.ForeignKey(Unit, related_name='per_unit', on_delete=models.SET_NULL, null=True, blank=True)
    energy = models.FloatField(max_length=50, null=True, blank=True)
    energy_unit = models.ForeignKey(Unit, related_name='energy_unit', on_delete=models.SET_NULL, null=True, blank=True)
    carbohydrate = models.FloatField(max_length=50, null=True, blank=True)
    carbohydrate_unit = models.ForeignKey(Unit, related_name='carbohydrate_unit', on_delete=models.SET_NULL, null=True, blank=True)
    protein = models.FloatField(max_length=50, null=True, blank=True)
    protein_unit = models.ForeignKey(Unit, related_name='protein_unit', on_delete=models.SET_NULL, null=True, blank=True)
    fat = models.FloatField(max_length=50, null=True, blank=True)
    fat_unit = models.ForeignKey(Unit, related_name='fat_unit', on_delete=models.SET_NULL, null=True, blank=True)
