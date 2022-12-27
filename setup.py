import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

__version__ = None
with open("de_GA/version.py") as f:
    exec(f.read())

# Long description
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

tests_requires = [
    "coverage==4.5.1",
    "pytest==3.8.0",
    "pytest-cov==2.6.0",
    "pylint==2.2.2",
    "pylint-plugin-utils==0.4",
    "factory-boy==2.11.1",
    "flake8==3.5.0",
    "isort==4.3.4",
    "requests-mock==1.5.2",
    "safety==1.8.4",
    "autopep8==1.4",
    "ipdb==0.11",
]

install_requires = [
    "requests==2.18.4",
    "mock==3.0.5",
    "packaging==19.0",
    "Twisted==19.2.0",
    "numpy==1.16.2",
    "botocore==1.12.147",
    "setuptools==65.5.1",
    "boto3==1.9.147",
    "pytest==3.8.0",
    "simplejson==3.16.0",
    "Unidecode==1.0.23",
    "httpretty==0.9.6",
    "scikit_learn==0.21.2",
    "typing==3.6.6",
    "klein",
    "responses"
]

extras_requires = {"test": tests_requires}

setup(
    name="de_GA",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        # supported python versions
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
    ],
    packages=find_packages(exclude=["tests", "tools", "docs", "contrib"]),
    version=__version__,
    install_requires=install_requires,
    tests_require=tests_requires,
    extras_require=extras_requires,
    description="Controlador de projetos de machine learning,"
                "exclusivo para projetos Softplan.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Softplan Planejamento e Sistemas",
    author_email="manoel.almeidaj@softplan.com.br",
    maintainer="Manoel Almeida Neto",
    maintainer_email="manoel.almeida@softplan.com.br",
    license="Apache 2.0",
    url="http://www.softplan.com.br",
    download_url="https://gitlab.com/api-projects-boilerplates/"
                 "differential-evolution-ga/{}.tar.gz"
                 "".format(__version__),
    project_urls={
        "Bug Reports": "https://gitlab.com/api-projects-boilerplates/differential-evolution-ga"
                       "/issues",
        "Source": "https://gitlab.com/api-projects-boilerplates/differential-evolution-ga",
    },
)
