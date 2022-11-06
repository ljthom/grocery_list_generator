import setuptools

setuptools.setup(
    name='pantry',
    packages=['pantry'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask-wtf',
        'jsonschema'
    ],
)