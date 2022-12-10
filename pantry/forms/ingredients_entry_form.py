from pantry.forms.base_forms import ModelForm
from pantry.models.ingredient_entry import IngredientEntry
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length


class IngredientEntryForm(ModelForm):
    ingredient = StringField('IngredientName', validators=[InputRequired(), Length(1, 255)])
    quantity = IntegerField()
    unit = SelectField('Unit', choices=[
        ('oz', 'Ounces'),
        ('tbsp', 'Tablespoons'),
        ('tsp', 'Teaspoons'),
        ('cup', 'Cups'),
        ('pint', 'Pints'),
        ('g', 'Grams'),
        ('mg', 'Milligrams'),
        ('kg', 'Kilograms'),
        ('lbs', 'Pounds'),
        ('gal', 'Gallons')
    ])



