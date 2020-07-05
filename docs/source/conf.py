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

import glob
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join("..", "..", "source")))


# -- Project information -----------------------------------------------------

project = 'Les Itérables'
copyright = '2020, Sixty North'
author = 'Sixty North'

import les_iterables

# The full version, including alpha/beta/rc tags
release = les_iterables.__version__



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme

    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Intersphinx mapping -----------------------------------------------------

major, minor, *_ = sys.version_info
python_version = f"{major}.{minor}"

# Allow us to link to the Python 3 documentation
intersphinx_mapping = {
    "python": (f"https://docs.python.org/{python_version}", (None, "python-inv.txt"))
}

# -- autodoc configuration --------------------------------------------

autodoc_default_values = {
    "members": None,
    "undoc-members": None,
    "special-members": "__init__",
    "show-inheritance": None,
    "member-order": "bysource",
    "exclude-members": "__dict__,__weakref__,__module__",
}


# -- sphinx-apidocs configuration --------------------------------------------

# Directory into which sphinx-apidocs which place its output
apidocs_build_dirpath = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "api"
)

# Directory to a Python package for which API docs will be generated
apidocs_source_dirpath = os.path.dirname(les_iterables.__file__)


apidocs_template_dirpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "_templates")


def run_better_apidoc(app):
    remove_apidoc()

    import better_apidoc

    better_apidoc.APP = app
    args = [
        "better-apidoc",
        "-t",
        apidocs_template_dirpath,
        "--force",
        "--no-toc",
        "--separate",
        "-o",
        apidocs_build_dirpath,
        apidocs_source_dirpath,
    ]
    better_apidoc.main(args)


def remove_apidoc():
    """Removes all generated files in the apidocs_build_dirpath.
    """
    api_doc_rst_files = glob.glob(os.path.join(apidocs_build_dirpath, "*.rst"))
    for api_doc_rst_file in api_doc_rst_files:
        try:
            os.remove(api_doc_rst_file)
        except OSError:
            pass


# -- Auto section labelling --------------------------------------------------

autosectionlabel_prefix_document = True


# -- Application setup -------------------------------------------------------


def setup(app):
    #app.add_stylesheet("theme_extensions.css")
    app.connect("builder-inited", run_better_apidoc)
    pass
