from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Food, Brand, Nutrient, Content

# Define the index name
food_index = Index('foods')

@food_index.doc_type
class FoodDocument(Document):
    brand = fields.ObjectField(properties={
        'brand': fields.TextField(),
    })

    nutrients = fields.ObjectField(properties={
        'name': fields.TextField(),
    })

    content = fields.ObjectField(properties={
        'content': fields.TextField(),
    })

    # Define the name field with a keyword sub-field for sorting and aggregations
    name = fields.TextField(
        fields={
            'keyword': fields.KeywordField(),  # Add a keyword sub-field for sorting
        }
    )

    categories = fields.TextField(
        fields={
            'keyword': fields.KeywordField(),  # Add a keyword sub-field for sorting
        }
    )

    class Django:
        model = Food  # The model associated with this Document
        # Remove 'name' and 'categories' from the fields list because they are already defined above
        fields = []  # List only other fields here

        related_models = [Brand, Nutrient, Content]

    def get_queryset(self):
        """Not mandatory but recommended: this queryset will limit the data to index"""
        return super(FoodDocument, self).get_queryset().select_related(
            'brand'
        ).prefetch_related(
            'nutrients', 'content'
        )
