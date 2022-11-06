import os
import secrets
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path


current_directory = Path.cwd()
app = Flask('pantry', instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db.db'  # whatever we name our database
app.config['SQLALCHEMY_BINDS'] = {
    'database_name', 'sqlite:///test_db.db'
}

# In case we want to use JSON for passing data, this makes sure the format is correct
app.config['JSON_SCHEMA'] = os.path.join(
    current_directory, 'pantry', 'static', 'json.schema'
)

# if we want to upload files containing ingredients for parsing into database
app.config['UPLOAD_FOLDER'] = os.path.join(
    current_directory, 'pantry', 'uploads'
)

app.config['ALLOWED_EXTENSIONS'] = {'txt', 'json', 'csv', 'xml'}  # allowed file types
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000  # change first number to increase maximum megabytes
app.config['OUTPUT_FOLDER'] = os.path.join(current_directory, 'pantry',
                                           'outputs')  # this is where the list will be downloadable from
app.config[
    'SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # not exactly sure what this does sqlalchemy needs it for something
app.config['TESTING'] = True  # We're still testing so give us debuggery
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)  # secret stuff

# imported after loading app because of a circular import issue.  views dependent on app, but pages won't load unless
# imported into init
from pantry.views import index, ingredient_form
# db = SQLAlchemy(app)

# table setup can go here and anything that needs to be loaded on a first run

