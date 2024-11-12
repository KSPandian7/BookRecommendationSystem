from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "BookRecommendationSystem"
AUTHOR_USER_NAME = "KULASEKARAPANDIAN K"
SRC_REPO = "BookRecommendationSystem"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="KULASEKARAPANDIAN K",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KSPandian7/BookRecommendationSystem",
    author_email="kspandia007@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)