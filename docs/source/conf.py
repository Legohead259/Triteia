# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Triteia Micro USV'
copyright = '2025, Braidan Duffy, Diego Colon-Serrano'
author = 'Braidan Duffy, Diego Colon-Serrano'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ "breathe" ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Breathe Configuration ---------------------------------------------------
breathe_projects = {"Triteia-CACS-Firmware": "../build/xml/"}
breathe_default_project = "Triteia-CACS-Firmware"
