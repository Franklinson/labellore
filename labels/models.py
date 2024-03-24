from django.db import models

# Create your models here.
class Label(models.Model):
    CATEGORIES = (
        ('TINNED FOODS', 'TINNED FOODS'), 
        ('INSTANT STAPLES', 'INSTANT STAPLES'), 
        ('DAIRY & CREAMERS', 'DAIRY & CREAMERS'),
        ('OILS', 'OILS'),
        ('BISCUITS', 'BISCUITS'),
        ('BEVEARAGES', 'BEVEARAGES'),
        ('SPREADS, DRESSINGS & SAUCES', ' SPREADS, DRESSINGS & SAUCES'),
        ('GRAINS & CEREALS', 'GRAINS & CEREALS'),
        ('PASTA', 'PASTA'),
        ('INFANT FORMULAE', 'INFANT FORMULAE'),
        ('NUTRITION SUPPLEMENTS', 'NUTRITION SUPPLEMENTS'),
        ('SPICES', 'SPICES'),
)
    categories = models.CharField(max_length=100, choices=CATEGORIES)
    name = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    net_weight = models.FloatField(max_length=50, null=True, blank=True)
    serving_size = models.FloatField(max_length=50, null=True, blank=True)
    serving_quantity = models.FloatField(max_length=50, null=True, blank=True)
    per = models.FloatField(max_length=50, null=True, blank=True)
    energy = models.FloatField(max_length=50, null=True, blank=True)
    carbohydrate = models.FloatField(max_length=50, null=True, blank=True)
    protein = models.FloatField(max_length=50, null=True, blank=True)
    sugar = models.FloatField(max_length=50, null=True, blank=True)
    added_sugar = models.FloatField(max_length=50, null=True, blank=True)
    fat = models.FloatField(max_length=50, null=True, blank=True)
    PUFA = models.FloatField(max_length=50, null=True, blank=True)
    MUFA = models.FloatField(max_length=50, null=True, blank=True)
    omega_3 = models.FloatField(max_length=50, null=True, blank=True)
    omega_6 = models.FloatField(max_length=50, null=True, blank=True)
    omega_9 = models.FloatField(max_length=50, null=True, blank=True)
    saturated_fat = models.FloatField(max_length=50, null=True, blank=True)
    unsaturated_fat = models.FloatField(max_length=50, null=True, blank=True)
    trans_fat = models.FloatField(max_length=50, null=True, blank=True)
    dietary_fiber = models.FloatField(max_length=50, null=True, blank=True)
    sodium = models.FloatField(max_length=50, null=True, blank=True)
    salt = models.FloatField(max_length=50, null=True, blank=True)
    potassium = models.FloatField(max_length=50, null=True, blank=True)
    iron = models.FloatField(max_length=50, null=True, blank=True)
    cholesterol = models.FloatField(max_length=50, null=True, blank=True)
    calcium = models.FloatField(max_length=50, null=True, blank=True)
    maxagnesium = models.FloatField(max_length=50, null=True, blank=True)
    phosphorus = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_A = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B1 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B1 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B2 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B3 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B5 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B6 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B7 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B9 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B12 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_C = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_D = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_E = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_K = models.FloatField(max_length=50, null=True, blank=True)
    iodine = models.FloatField(max_length=50, null=True, blank=True)
    zinc = models.FloatField(max_length=50, null=True, blank=True)
    chloride = models.FloatField(max_length=50, null=True, blank=True)
    manganese = models.FloatField(max_length=50, null=True, blank=True)
    selenium = models.FloatField(max_length=50, null=True, blank=True)
    molybdenum = models.FloatField(max_length=50, null=True, blank=True)
    flouride = models.FloatField(max_length=50, null=True, blank=True)
    chromium = models.FloatField(max_length=50, null=True, blank=True)
    copper = models.FloatField(max_length=50, null=True, blank=True)
    casein = models.FloatField(max_length=50, null=True, blank=True)
    ash = models.FloatField(max_length=50, null=True, blank=True)
    linolenic = models.FloatField(max_length=50, null=True, blank=True)
    apha_linolenic = models.FloatField(max_length=50, null=True, blank=True)
    moisture = models.FloatField(max_length=50, null=True, blank=True)
    cholin = models.FloatField(max_length=50, null=True, blank=True)
    inositol = models.FloatField(max_length=50, null=True, blank=True)
    taurine = models.FloatField(max_length=50, null=True, blank=True)
    L_carnitine = models.FloatField(max_length=50, null=True, blank=True)
    nucleotides = models.FloatField(max_length=50, null=True, blank=True)
    sphingomyelin = models.FloatField(max_length=50, null=True, blank=True)
    lutein = models.FloatField(max_length=50, null=True, blank=True)
    carotenes = models.FloatField(max_length=50, null=True, blank=True)
    whey = models.FloatField(max_length=50, null=True, blank=True)
    tryptophan = models.FloatField(max_length=50, null=True, blank=True)
    threonine = models.FloatField(max_length=50, null=True, blank=True)
    isoleucine = models.FloatField(max_length=50, null=True, blank=True)
    leucine = models.FloatField(max_length=50, null=True, blank=True)
    methionine = models.FloatField(max_length=50, null=True, blank=True)
    cystine = models.FloatField(max_length=50, null=True, blank=True)
    phenylalanine = models.FloatField(max_length=50, null=True, blank=True)
    tyrosine = models.FloatField(max_length=50, null=True, blank=True)
    valine = models.FloatField(max_length=50, null=True, blank=True)
    arginine = models.FloatField(max_length=50, null=True, blank=True)
    histidine = models.FloatField(max_length=50, null=True, blank=True)
    alanine = models.FloatField(max_length=50, null=True, blank=True)
    aspartic = models.FloatField(max_length=50, null=True, blank=True)
    glutamic = models.FloatField(max_length=50, null=True, blank=True)
    glycine = models.FloatField(max_length=50, null=True, blank=True)
    proline = models.FloatField(max_length=50, null=True, blank=True)
    serine = models.FloatField(max_length=50, null=True, blank=True)
    alcoholc = models.FloatField(max_length=50, null=True, blank=True)
    caffeine = models.FloatField(max_length=50, null=True, blank=True)
    theobromine = models.FloatField(max_length=50, null=True, blank=True)
    
    
    # def __str__(self):
    #     return f'{self.categories} - {self.name} - {self.brand} - {self.energy}'