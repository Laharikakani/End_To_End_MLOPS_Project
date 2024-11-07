import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End_To_End_MLOPS_Project"
AUTHOR_USER_NAME = "Lahari"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "laharikakani7@gmail.com"


setuptools.setup(
    name="End_To_End_MLOPS_Project",
    version=__version__,
    author="LahariKakani",
    author_email="laharikakani7@gmail.com",
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/LahariKakani/End_To_End_MLOPS_Project",
    project_urls={
        "Bug Tracker": f"https://github.com/LahariKakani/End_To_End_MLOPS_Project/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)