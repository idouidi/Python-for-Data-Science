from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    packages=find_packages(),
    description="A sample test package",
    long_description="A sample test package",
    long_description_content_type="text/plain",
    url="https://github.com/idouidi/ft_package",
    author="idouidi",
    author_email="idouidi@student.42.fr",
    license="MIT",
    install_requires=[],
    python_requires=">=3.10",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
)