from django.contrib import admin

# Register your models here.
from Locals.models import Label, Unit

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("categories", "name", "energy")
    list_filter = ("categories",)
    search_fields = ("name", )
# admin.site.register(models.Label)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation")
    
    
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("categories", )
    