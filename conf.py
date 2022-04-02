# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Sciences-Physiques.NET'
author = 'Rémi MEVAERE'
copyright = ''

# The full version, including alpha/beta/rc tags
release = '0.0.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # "myst_parser",
    "sphinx_copybutton",
    "myst_nb"
]

myst_enable_extensions = ["dollarmath", "amsmath"]
myst_dmath_double_inline = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

language = 'fr'
exclude_patterns = ['README.md', 'spnetblogvenv', 'venv', '_build', 'Thumbs.db', '.DS_Store']

html_theme_options = {
    "extra_navbar": "",
    "show_toc_level": 2,
    "home_page_in_toc": True,
    "repository_url": "https://github.com/mevaere/spnet",
    "use_repository_button": True,
    "logo_only": True,
    "show_navbar_depth": 1,
    "use_issues_button": True,
}

html_last_updated_fmt = "%d %b %Y à %H:%M"
html_show_copyright = False
html_favicon = '_medias/favicon.png'
html_theme = 'sphinx_book_theme'
html_title = 'Sciences-Physiques.NET'
html_logo = "_medias/logo.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
