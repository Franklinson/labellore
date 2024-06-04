from django.contrib import admin


from Locals.models import Food, Unit, FoodNutrient, Content, Nutrient, NutrientContent


class FoodNutrientInline(admin.TabularInline):
    model = FoodNutrient
    extra = 1

class NutrientContentInline(admin.TabularInline):
    model = NutrientContent
    extra = 1

class FoodAdmin(admin.ModelAdmin):
    list_display = ("categories", "name")
    list_filter = ("categories",)
    search_fields = ("name", )
    fieldsets = [
        (None, {"fields": ["categories", "name"]}),
    ]
    inlines = [NutrientContentInline, FoodNutrientInline]


admin.site.register(Food,FoodAdmin)

@admin.register(Nutrient)
class NutrientAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation")
    search_fields = ("name", )
    
    
@admin.register(FoodNutrient)
class FoodNutrientAdmin(admin.ModelAdmin):
    list_display = ('food', 'nutrient', 'amount')
    list_filter = ('food', 'nutrient')
    

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("content",)
    search_fields = ("content",)
    
    
@admin.register(NutrientContent)
class NutrientContentAdmin(admin.ModelAdmin):
    list_display = ("food", "content")
    list_filter = ("food", "content")

    