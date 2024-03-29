# Documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join("..")))


# -- Project information -----------------------------------------------------

project = "Plot Serializer"
copyright = "2023, Michaela Lestakova, Kevin Logan"
author = "Michaela Lestakova, Kevin Logan"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",  # Generate documentation from docstrings
    "sphinx.ext.autosummary",  # Generate an automatic summary of the packages
    "sphinx.ext.viewcode",  # Embed links to view the source code
    "sphinx.ext.napoleon",  # Plugin to handle different docstring styles
    "sphinxcontrib.autodoc_pydantic",  # Handle pydantic classes
    "sphinx_rtd_theme",  # Apply readthedocs documentation theme
]

# Generate package summary automatically
autosummary_generate = True

# Applpy google docstring style
napoleon_google_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["static"]

# Show the json schema when displaying pydantic models
autodoc_pydantic_model_show_json = True
