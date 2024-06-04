from django.contrib import admin


from commercials.models import Food, Unit, Brand, FoodNutrient, Nutrient


class FoodNutrientInline(admin.TabularInline):
    model = FoodNutrient
    extra = 1


# @admin.register(Label)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("categories", "name", "brand")
    list_filter = ("categories",)
    search_fields = ("brand__brand", "name")
    fieldsets = [
        (None, {"fields": ["categories", "brand", "name"]}),
        # ("Date information", {"fields": ["brand"], "classes": ["collapse"]}),
    ]
    inlines = [FoodNutrientInline]


admin.site.register(Food,FoodAdmin)

@admin.register(Nutrient)
class NutrientAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation")
    search_fields = ("name", )
    
    

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("brand", )
    search_fields = ("brand", )
    

@admin.register(FoodNutrient)
class FoodNutrientAdmin(admin.ModelAdmin):
    list_display = ('food', 'nutrient', 'amount')
    list_filter = ('food', 'nutrient')