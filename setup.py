import setuptools
import zipfile

with open('requirements.txt', encoding='utf-8') as reqs:
    required = reqs.read().splitlines()

setuptools.setup(
    name='pantry',
    packages=['pantry'],
    include_package_data=True,
    install_requires=required
)

with zipfile.ZipFile("./pantry/models/recipes.db.zip", 'r') as zip_ref:
    zip_ref.extractall("./pantry/models/recipes.db")
