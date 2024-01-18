from setuptools import setup, find_packages

setup(
    name="clean_folder",
    version="0.1",
    packages=["clean_folder"],
    author="Michał",
    license="MIT",
    entry_points={
        "console_scripts": [
            "clean-folder = clean_folder.clean:main",
        ],
    },
)
