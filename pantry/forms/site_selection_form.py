from flask_wtf import FlaskForm
from wtforms import SubmitField
from pantry.forms.base_forms import MultiCheckBoxField, MultiCheckboxAtLeastOne
from pantry.db_utils import sites


class RecipeSelectionForm(FlaskForm):
    sites = MultiCheckBoxField('Recipe Sites', choices=sites.keys(), validators=[MultiCheckboxAtLeastOne])
    submit = SubmitField()
