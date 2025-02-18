from setuptools import setup, find_packages

setup(
    name='deprecate_cmsplugin_filer',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    description="A small app with a migration for converting deprecated cmsplugin-filer objects to djangocms plugin objects.",
    long_description=open('README.md', 'r').read(),
    install_requires=[
        'django >= 1.11',
    ],
)
