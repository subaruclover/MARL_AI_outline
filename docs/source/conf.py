# Configuration file for the Sphinx documentation builder.

# -- Project information
import sphinx_rtd_theme

project = 'MARL'
copyright = '2022, Qiong'
author = 'Qiong Huang'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    # 'sphinxcontrib.bibtex',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
source_suffix = ['.rst', '.md']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here
html_static_path = ['_static']

html_logo = 'images/logo.png'
html_theme_options = {
    'logo_only': True
}

def setup(app):
    app.add_js_file(
        "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js")
    app.add_js_file("https://cdn.jsdelivr.net/npm/vega@5.20.2")
    app.add_js_file("https://cdn.jsdelivr.net/npm/vega-lite@5.1.0")
    app.add_js_file("https://cdn.jsdelivr.net/npm/vega-embed@6.17.0")

    app.add_js_file("js/copybutton.js")
    app.add_js_file("js/benchmark.js")
    app.add_css_file("css/style.css")

# -- Options for EPUB output
epub_show_urls = 'footnote'



