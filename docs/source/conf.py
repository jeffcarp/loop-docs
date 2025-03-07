# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'loop'
copyright = '2024, TJLA'
author = 'TJLA'

release = '0.1'
version = '0.1.0'

import sys
from pathlib import Path
sys.path.insert(0, str(Path('..', '..').resolve()))

print('SYS PATH:')
print(sys.path)

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
