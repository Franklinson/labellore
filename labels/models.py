from django.db import models

# Create your models here.

class Unit(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.abbreviation}'


class Category(models.Model):
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
    categories = models.CharField(max_length=100, choices=CATEGORIES)
    
    def __str__(self):
        return f'{self.categories}'
    
    class Meta:
        verbose_name_plural = "Category"



class Brand(models.Model):
    brand = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f'{self.brand}'
    

class Label(models.Model):
    Category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL, blank=True)
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
    sugar = models.FloatField(max_length=50, null=True, blank=True)
    sugar_unit = models.ForeignKey(Unit, related_name='sugar_unit', on_delete=models.SET_NULL, null=True, blank=True)
    added_sugar = models.FloatField(max_length=50, null=True, blank=True)
    added_sugar_unit = models.ForeignKey(Unit, related_name='added_sugar_unit', on_delete=models.SET_NULL, null=True, blank=True)
    fat = models.FloatField(max_length=50, null=True, blank=True)
    fat_unit = models.ForeignKey(Unit, related_name='fat_unit', on_delete=models.SET_NULL, null=True, blank=True)
    PUFA = models.FloatField(max_length=50, null=True, blank=True)
    PUFA_unit = models.ForeignKey(Unit, related_name='PUFA_unit', on_delete=models.SET_NULL, null=True, blank=True)
    MUFA = models.FloatField(max_length=50, null=True, blank=True)
    MUFA_unit = models.ForeignKey(Unit, related_name='MUFA_unit', on_delete=models.SET_NULL, null=True, blank=True)
    omega_3 = models.FloatField(max_length=50, null=True, blank=True)
    omega_3_unit = models.ForeignKey(Unit, related_name='omega_3_unit', on_delete=models.SET_NULL, null=True, blank=True)
    omega_6 = models.FloatField(max_length=50, null=True, blank=True)
    omega_6_unit = models.ForeignKey(Unit, related_name='omega_6_unit', on_delete=models.SET_NULL, null=True, blank=True)
    omega_9 = models.FloatField(max_length=50, null=True, blank=True)
    omega_9_unit = models.ForeignKey(Unit, related_name='omega_9_unit', on_delete=models.SET_NULL, null=True, blank=True)
    saturated_fat = models.FloatField(max_length=50, null=True, blank=True)
    saturated_fat_unit = models.ForeignKey(Unit, related_name='saturated_fat_unit', on_delete=models.SET_NULL, null=True, blank=True)
    unsaturated_fat = models.FloatField(max_length=50, null=True, blank=True)
    unsaturated_fat_unit = models.ForeignKey(Unit, related_name='unsaturated_fat_unit', on_delete=models.SET_NULL, null=True, blank=True)
    trans_fat = models.FloatField(max_length=50, null=True, blank=True)
    trans_fat_unit = models.ForeignKey(Unit, related_name='trans_fat_unit', on_delete=models.SET_NULL, null=True, blank=True)
    dietary_fiber = models.FloatField(max_length=50, null=True, blank=True)
    dietary_fiber_unit = models.ForeignKey(Unit, related_name='dietary_fiber_unit', on_delete=models.SET_NULL, null=True, blank=True)
    sodium = models.FloatField(max_length=50, null=True, blank=True)
    sodium_unit = models.ForeignKey(Unit, related_name='sodium_unit', on_delete=models.SET_NULL, null=True, blank=True)
    salt = models.FloatField(max_length=50, null=True, blank=True)
    salt_unit = models.ForeignKey(Unit, related_name='salt_unit', on_delete=models.SET_NULL, null=True, blank=True)
    potassium = models.FloatField(max_length=50, null=True, blank=True)
    potassium_unit = models.ForeignKey(Unit, related_name='potassium_unit', on_delete=models.SET_NULL, null=True, blank=True)
    iron = models.FloatField(max_length=50, null=True, blank=True)
    iron_unit = models.ForeignKey(Unit, related_name='iron_unit', on_delete=models.SET_NULL, null=True, blank=True)
    cholesterol = models.FloatField(max_length=50, null=True, blank=True)
    cholesterol_unit = models.ForeignKey(Unit, related_name='cholesterol_unit', on_delete=models.SET_NULL, null=True, blank=True)
    calcium = models.FloatField(max_length=50, null=True, blank=True)
    calcium_unit = models.ForeignKey(Unit, related_name='calcium_unit', on_delete=models.SET_NULL, null=True, blank=True)
    maxagnesium = models.FloatField(max_length=50, null=True, blank=True)
    maxagnesium_unit = models.ForeignKey(Unit, related_name='maxagnesium_unit', on_delete=models.SET_NULL, null=True, blank=True)
    phosphorus = models.FloatField(max_length=50, null=True, blank=True)
    phosphorus_unit = models.ForeignKey(Unit, related_name='phosphorus_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_A = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_A_unit = models.ForeignKey(Unit, related_name='vitamin_A_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_B1 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B1_unit = models.ForeignKey(Unit, related_name='vitamin_B1_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_B2 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B2_unit = models.ForeignKey(Unit, related_name='vitamin_B2_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_B3 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B3_unit = models.ForeignKey(Unit, related_name='vitamin_B3_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_B5 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B5_unit = models.ForeignKey(Unit, related_name='vitamin_B5_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_B6 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B6_unit = models.ForeignKey(Unit, related_name='vitamin_B6_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_B7 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B7_unit = models.ForeignKey(Unit, related_name='vitamin_B7_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_B9 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B9_unit = models.ForeignKey(Unit, related_name='vitamin_B9_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_B12 = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_B12_unit = models.ForeignKey(Unit, related_name='vitamin_B12_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_C = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_C_unit = models.ForeignKey(Unit, related_name='vitamin_C_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_D = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_D_unit = models.ForeignKey(Unit, related_name='vitamin_D_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_E = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_E_unit = models.ForeignKey(Unit, related_name='vitamin_E_unit', on_delete=models.SET_NULL, null=True, blank=True)
    vitamin_K = models.FloatField(max_length=50, null=True, blank=True)
    vitamin_K_unit = models.ForeignKey(Unit, related_name='vitamin_K_unit', on_delete=models.SET_NULL, null=True, blank=True)
    iodine = models.FloatField(max_length=50, null=True, blank=True)
    iodine_unit = models.ForeignKey(Unit, related_name='iodine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    zinc = models.FloatField(max_length=50, null=True, blank=True)
    zinc_unit = models.ForeignKey(Unit, related_name='zinc_unit', on_delete=models.SET_NULL, null=True, blank=True)
    chloride = models.FloatField(max_length=50, null=True, blank=True)
    chloride_unit = models.ForeignKey(Unit, related_name='chloride_unit', on_delete=models.SET_NULL, null=True, blank=True)
    manganese = models.FloatField(max_length=50, null=True, blank=True)
    manganese_unit = models.ForeignKey(Unit, related_name='manganese_unit', on_delete=models.SET_NULL, null=True, blank=True)
    selenium = models.FloatField(max_length=50, null=True, blank=True)
    selenium_unit = models.ForeignKey(Unit, related_name='selenium_unit', on_delete=models.SET_NULL, null=True, blank=True)
    molybdenum = models.FloatField(max_length=50, null=True, blank=True)
    molybdenum_unit = models.ForeignKey(Unit, related_name='molybdenum_unit', on_delete=models.SET_NULL, null=True, blank=True)
    flouride = models.FloatField(max_length=50, null=True, blank=True)
    flouride_unit = models.ForeignKey(Unit, related_name='flouride_unit', on_delete=models.SET_NULL, null=True, blank=True)
    chromium = models.FloatField(max_length=50, null=True, blank=True)
    chromium_unit = models.ForeignKey(Unit, related_name='chromium_unit', on_delete=models.SET_NULL, null=True, blank=True)
    copper = models.FloatField(max_length=50, null=True, blank=True)
    copper_unit = models.ForeignKey(Unit, related_name='copper_unit', on_delete=models.SET_NULL, null=True, blank=True)
    casein = models.FloatField(max_length=50, null=True, blank=True)
    casein_unit = models.ForeignKey(Unit, related_name='casein_unit', on_delete=models.SET_NULL, null=True, blank=True)
    ash = models.FloatField(max_length=50, null=True, blank=True)
    ash_unit = models.ForeignKey(Unit, related_name='ash_unit', on_delete=models.SET_NULL, null=True, blank=True)
    linolenic = models.FloatField(max_length=50, null=True, blank=True)
    linolenic_unit = models.ForeignKey(Unit, related_name='linolenic_unit', on_delete=models.SET_NULL, null=True, blank=True)
    apha_linolenic = models.FloatField(max_length=50, null=True, blank=True)
    apha_linolenic_unit = models.ForeignKey(Unit, related_name='apha_linolenic_unit', on_delete=models.SET_NULL, null=True, blank=True)
    moisture = models.FloatField(max_length=50, null=True, blank=True)
    moisture_unit = models.ForeignKey(Unit, related_name='moisture_unit', on_delete=models.SET_NULL, null=True, blank=True)
    cholin = models.FloatField(max_length=50, null=True, blank=True)
    cholin_unit = models.ForeignKey(Unit, related_name='cholin_unit', on_delete=models.SET_NULL, null=True, blank=True)
    inositol = models.FloatField(max_length=50, null=True, blank=True)
    inositol_unit = models.ForeignKey(Unit, related_name='inositol_unit', on_delete=models.SET_NULL, null=True, blank=True)
    taurine = models.FloatField(max_length=50, null=True, blank=True)
    taurine_unit = models.ForeignKey(Unit, related_name='taurine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    L_carnitine = models.FloatField(max_length=50, null=True, blank=True)
    L_carnitine_unit = models.ForeignKey(Unit, related_name='L_carnitine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    nucleotides = models.FloatField(max_length=50, null=True, blank=True)
    nucleotides_unit = models.ForeignKey(Unit, related_name='nucleotides_unit', on_delete=models.SET_NULL, null=True, blank=True)
    sphingomyelin = models.FloatField(max_length=50, null=True, blank=True)
    sphingomyelin_unit = models.ForeignKey(Unit, related_name='sphingomyelin_unit', on_delete=models.SET_NULL, null=True, blank=True)
    lutein = models.FloatField(max_length=50, null=True, blank=True)
    lutein_unit = models.ForeignKey(Unit, related_name='lutein_unit', on_delete=models.SET_NULL, null=True, blank=True)
    carotenes = models.FloatField(max_length=50, null=True, blank=True)
    carotenes_unit = models.ForeignKey(Unit, related_name='carotenes_unit', on_delete=models.SET_NULL, null=True, blank=True)
    whey = models.FloatField(max_length=50, null=True, blank=True)
    whey_unit = models.ForeignKey(Unit, related_name='whey_unit', on_delete=models.SET_NULL, null=True, blank=True)
    tryptophan = models.FloatField(max_length=50, null=True, blank=True)
    tryptophan_unit = models.ForeignKey(Unit, related_name='tryptophan_unit', on_delete=models.SET_NULL, null=True, blank=True)
    threonine = models.FloatField(max_length=50, null=True, blank=True)
    threonine_unit = models.ForeignKey(Unit, related_name='threonine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    isoleucine = models.FloatField(max_length=50, null=True, blank=True)
    isoleucine_unit = models.ForeignKey(Unit, related_name='isoleucine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    leucine = models.FloatField(max_length=50, null=True, blank=True)
    leucine_unit = models.ForeignKey(Unit, related_name='leucine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    methionine = models.FloatField(max_length=50, null=True, blank=True)
    methionine_unit = models.ForeignKey(Unit, related_name='methionine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    cystine = models.FloatField(max_length=50, null=True, blank=True)
    cystine_unit = models.ForeignKey(Unit, related_name='cystine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    phenylalanine = models.FloatField(max_length=50, null=True, blank=True)
    phenylalanine_unit = models.ForeignKey(Unit, related_name='phenylalanine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    tyrosine = models.FloatField(max_length=50, null=True, blank=True)
    tyrosine_unit = models.ForeignKey(Unit, related_name='tyrosine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    valine = models.FloatField(max_length=50, null=True, blank=True)
    valine_unit = models.ForeignKey(Unit, related_name='valine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    arginine = models.FloatField(max_length=50, null=True, blank=True)
    arginine_unit = models.ForeignKey(Unit, related_name='arginine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    histidine = models.FloatField(max_length=50, null=True, blank=True)
    histidine_unit = models.ForeignKey(Unit, related_name='histidine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    alanine = models.FloatField(max_length=50, null=True, blank=True)
    alanine_unit = models.ForeignKey(Unit, related_name='alanine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    aspartic = models.FloatField(max_length=50, null=True, blank=True)
    aspartic_unit = models.ForeignKey(Unit, related_name='aspartic_unit', on_delete=models.SET_NULL, null=True, blank=True)
    glutamic = models.FloatField(max_length=50, null=True, blank=True)
    glutamic_unit = models.ForeignKey(Unit, related_name='glutamic_unit', on_delete=models.SET_NULL, null=True, blank=True)
    glycine = models.FloatField(max_length=50, null=True, blank=True)
    glycine_unit = models.ForeignKey(Unit, related_name='glycine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    proline = models.FloatField(max_length=50, null=True, blank=True)
    proline_unit = models.ForeignKey(Unit, related_name='proline_unit', on_delete=models.SET_NULL, null=True, blank=True)
    serine = models.FloatField(max_length=50, null=True, blank=True)
    serine_unit = models.ForeignKey(Unit, related_name='serine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    alcohol = models.FloatField(max_length=50, null=True, blank=True)
    alcohol_unit = models.ForeignKey(Unit, related_name='alcohol_unit', on_delete=models.SET_NULL, null=True, blank=True)
    caffeine = models.FloatField(max_length=50, null=True, blank=True)
    caffeine_unit = models.ForeignKey(Unit, related_name='caffeine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    theobromine = models.FloatField(max_length=50, null=True, blank=True)
    theobromine_unit = models.ForeignKey(Unit, related_name='theobromine_unit', on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.name} - {self.brand} - {self.energy}'