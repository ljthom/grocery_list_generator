from pantry import app
from flask import redirect, render_template, request, url_for, flash

@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    form = AddData();
    if form.validate_on_submit():
        name = request.form['name']
        quantity = request.form['quantity']
        unit = request.form['units']
        record = Database(name, quantity, unit) ## Need database class name
        db.session.add(record)
        db.session.commit();
        return render_template('ingredient_form.html')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form, field).label.text, error),
                      'error')
        return render_template('ingredient_form.html', form=form)