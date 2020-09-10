import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='classification_algorithm',
    version='0.1',
    author="Manikant Kumar",
    packages=['classification_algorithm'],
    install_requires=['certifi', 'joblib', 'numpy', 'pandas', 'python-dateutil', 'pytz', 'scikit-learn', 'scipy', 'six',
                      'sklearn', 'threadpoolctl', 'wincertstore', 'xgboost'],
    author_email="mani2474695@gmail.com",
    description="All classifier algorithm at one place",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devil-cyber/Classifier_Algorithm",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
