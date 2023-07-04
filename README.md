# Neuro Blastoma

This repository investigates whether it is possible to count neuroblastoma cell lines (known as Kelly) in a microscope image. The image is a two-dimensional representation of a cell culture, stained with a fluorescent dye and captured using a widefield fluorescent microscope.

There is a small data set of example cell culture images inside the [`images`](./images/) directory. Inside of the same directory, there is also a folder with test images that can be used to test the algorithms.

## Pre-requisites

- [Poetry](https://python-poetry.org/docs/#installation) >= 1.3.2
- [Pyenv](https://github.com/pyenv/pyenv#installation) >= 2.3.12

## Quick Start

- Be sure to have the specified version of Python installed: `pyenv install 3.11.1`
- Install the dependencies: `poetry install` inside the project folder
- If you want to use the virtual environment inside the terminal: `poetry shell`

## Functionalities

- Open the Jupyter notebooks in e.g. VS Code and run the cells to see the results. VS Code will automatically detect the virtual environment and use it, if not, it will ask for it. Always select the virtual environment created by Poetry in the project folder.
- Create PDFs from the notebooks using the `nbconvert` command, e.g.: `jupyter nbconvert --to webpdf --allow-chromium-download notebooks/01_exploration.ipynb`. This will create a PDF file in the same folder as the notebook.
