from django.contrib import admin


from commercials.models import Label, Unit, Brand, NutrientList, Nutrient


class NutrientInline(admin.StackedInline):
    model = Nutrient
    extra = 3



# @admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("categories", "name", "brand", "energy")
    list_filter = ("categories",)
    search_fields = ("brand__brand", "name")
    fieldsets = [
        (None, {"fields": ["categories", "brand", "name", "net_weight", "net_weight_unit",
                           "serving_size", "serving_size_unit", "serving_quantity", "serving_quantity_unit",
                           "per", "per_unit", "energy", "energy_unit"]}),
        # ("Date information", {"fields": ["brand"], "classes": ["collapse"]}),
    ]
    inlines = [NutrientInline]


admin.site.register(Label,LabelAdmin)
admin.site.register(Nutrient)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "abbreviation")
    search_fields = ("name", )
    
    

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("brand", )
    search_fields = ("brand", )
    

@admin.register(NutrientList)
class NutrientListAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)