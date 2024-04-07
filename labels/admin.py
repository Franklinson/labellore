from django.contrib import admin

# Register your models here.
from labels.models import Label, Unit, Category, Brand

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ( "name", "brand", "energy")
    # list_filter = ("categories",)
    search_fields = ("brand", "name")
# admin.site.register(models.Label)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation")
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("categories", )
    

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("brand", )