from wtforms_alchemy import ModelForm
from pantry.models.ingredient_entry import IngredientEntry


class IngredientEntryForm(ModelForm):
    class Meta:
        model = IngredientEntry
