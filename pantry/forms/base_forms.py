# Taken from stackoverflow user scrollout
# https://stackoverflow.com/questions/73354015/multicheckbox-field-validation-with-flask-wtforms

from wtforms.fields import SelectMultipleField
from wtforms.validators import StopValidation
from wtforms import widgets


class MultiCheckBoxField(SelectMultipleField):
    widget = widgets.ListWidget
    option_widget = widgets.CheckboxInput()


class MultiCheckboxAtLeastOne():
    def __init__(self, message=None):
        if not message:
            message = "At Least One Option Must Be Selected."
        self.message = message

        def __call__(self, form, field):
            if len(field.data) == 0:
                raise StopValidation(self.message)