import setuptools

with open('requirements.txt', encoding='utf-8') as reqs:
    required = reqs.read().splitlines()

setuptools.setup(
    name='pantry',
    packages=['pantry'],
    include_package_data=True,
    install_requires=required
)
