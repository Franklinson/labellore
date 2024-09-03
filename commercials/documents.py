from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Food, Brand, Nutrient, Content, Unit

@registry.register_document
class FoodDocument(Document):
    # Related fields for Brand
    brand = fields.ObjectField(properties={
        'brand': fields.TextField(),
    })
    
    # Many-to-many relationship fields for Nutrients with Unit Abbreviations
    nutrients = fields.NestedField(properties={
        'name': fields.TextField(),
        'amount': fields.FloatField(),
        'unit': fields.ObjectField(properties={
            'abbreviation': fields.TextField(),  # Only the abbreviation field
        })
    })
    
    # Many-to-many relationship fields for Content with Unit Abbreviations
    content = fields.NestedField(properties={
        'content': fields.TextField(),
        'amount': fields.FloatField(),
        'unit': fields.ObjectField(properties={
            'abbreviation': fields.TextField(),  # Only the abbreviation field
        })
    })

    class Index:
        name = "foods"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Food
        fields = [
            "categories",
            "name",
        ]
        related_models = [Brand, Nutrient, Content, Unit]

    def get_queryset(self):
        return super().get_queryset().select_related("brand").prefetch_related(
            "nutrients", "content", "nutrients__foodnutrient", "content__nutrientcontent", "nutrients__foodnutrient__unit", "content__nutrientcontent__unit"
        )

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Brand):
            return related_instance.food_set.all()
        elif isinstance(related_instance, Nutrient):
            return related_instance.food_set.all()
        elif isinstance(related_instance, Content):
            return related_instance.food_set.all()
        elif isinstance(related_instance, Unit):
            return related_instance.foodnutrient_set.all().values_list('food', flat=True)
