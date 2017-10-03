# -*- coding: utf-8 -*-
#
# sphinx-quickstart on Fri Nov 28 22:10:09 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import subprocess
import sphinx

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.append(os.path.abspath('sphinxext'))

import sphinx_gallery

# General configuration
# ---------------------

needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.doctest',
        'only_directives',
        'ipython_console_highlighting',
        #'matplotlib.sphinxext.only_directives',
        ('sphinx.ext.imgmath'  # only available for sphinx >= 1.4
            if sphinx.version_info[:2] >= (1, 4)
            else 'sphinx.ext.pngmath'),
        'sphinx.ext.intersphinx',
        'sphinx.ext.extlinks',
        'sphinx_gallery.gen_gallery',
]

doctest_test_doctest_blocks = 'true'

sphinx_gallery_conf = {
    'examples_dirs': ['intro/summary-exercises/examples',
                      'intro/matplotlib/examples',
                      'intro/numpy/examples',
                      'intro/scipy/examples',
                      # the following entry contains an extra level because
                      # execution of the other python files causes errors
                      'advanced/advanced_numpy/examples/plots',
                      'advanced/image_processing/examples',
                      'advanced/mathematical_optimization/examples',
                      'packages/scikit-image/examples',
                      'packages/scikit-learn/examples',
                      'packages/statistics/examples',
                      'guide/examples',
                     ],
    'gallery_dirs': ['intro/summary-exercises/auto_examples',
                     'intro/matplotlib/auto_examples',
                     'intro/numpy/auto_examples',
                     'intro/scipy/auto_examples',
                     'advanced/advanced_numpy/auto_examples',
                     'advanced/image_processing/auto_examples',
                     'advanced/mathematical_optimization/auto_examples',
                     'packages/scikit-image/auto_examples',
                     'packages/scikit-learn/auto_examples',
                     'packages/statistics/auto_examples',
                     'guide/auto_examples',
                     ],
    'doc_module': 'scipy-lecture-notes',
    'reference_url': {
        'numpy': 'http://docs.scipy.org/doc/numpy',
        'scipy': 'http://docs.scipy.org/doc/scipy/reference',
        'pandas': 'http://pandas.pydata.org/pandas-docs/stable/',
        'seaborn': 'http://seaborn.pydata.org/',
        'matplotlib': 'http://matplotlib.org/',
        'scikit-learn': 'http://scikit-learn.org/stable',
        'scikit-image': 'http://scikit-image.org/docs/stable/',
        'mayavi': 'http://docs.enthought.com/mayavi/mayavi/',
        'statsmodels': 'http://www.statsmodels.org/stable/',
        },
    'backreferences_dir': False,
    }

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u"Scipy lecture notes"
copyright = u'2012,2013,2015,2016,2017'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The short X.Y version.
# we get this from git
# this WILL break if we are not in a git-repository
p = subprocess.Popen(['git', 'describe', '--tags'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
p.wait()
version = p.stdout.read().strip().decode()

# The full version, including alpha/beta/rc tags.
release = '2017.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'
today_fmt = '%B %d, %Y'
if version:
    today_fmt += ' ({%s})' % version

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['intro/image_processing']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Monkey-patch sphinx to set the lineseparator option of pygment, to
# have indented line wrapping
from pygments import formatters

class MyHtmlFormatter(formatters.HtmlFormatter):
    def __init__(self, **options):
        options['lineseparator'] = '\n<div class="newline"></div>'
        formatters.HtmlFormatter.__init__(self, **options)

from sphinx import highlighting
highlighting.PygmentsBridge.html_formatter = MyHtmlFormatter

# Our substitutions
rst_epilog = """

.. |clear-floats| raw:: html

    <div style="clear: both"></div>

.. always clear floats at the bottom to avoid having stick out in the footer

|clear-floats|

"""

# Options for HTML output
# -----------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'scipy_lectures'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['themes']

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
#html_style = 'default.css'

html_theme_options = {
                #'nosidebar': 'true',
                'footerbgcolor': '#000000',
                'relbarbgcolor': '#000000',
                }


# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Scipy lecture notes"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = "Scipy"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['themes/scipy_lectures/static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'ScipyLectures'

# Options for epub output
# ------------------------

epub_theme = 'epub'
epub_theme_options = {'relbar1': False, 'footer': False}
epub_show_urls = 'no'
epub_tocdup = False

# Options for LaTeX output
# ------------------------

# Latex references with page numbers (only Sphinx 1.0)
latex_show_pagerefs = False

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index', 'ScipyLectures.tex', ur'Scipy lecture notes',
   ur"""Scipy lectures team. Editors: Gaël Varoquaux, Emmanuelle Gouillart, Olav Vahtras""",
   'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'images/cover.pdf'

# Latex settings
latex_toplevel_sectioning = 'part'
latex_domain_indices = False

# Additional stuff for the LaTeX preamble.
preamble = r"""
\definecolor{VerbatimColor}{rgb}{0.961, .98, 1.}
\definecolor{VerbatimBorderColor}{rgb}{0.6,0.6,0.6}
\usepackage{graphics}
\usepackage[final]{pdfpages}

\setcounter{tocdepth}{1}
\usepackage{amssymb}
\usepackage{pifont}
\DeclareUnicodeCharacter{2460}{\ding{182}}
\DeclareUnicodeCharacter{2461}{\ding{183}}
\DeclareUnicodeCharacter{2462}{\ding{184}}
\DeclareUnicodeCharacter{2794}{\ding{229}}

\definecolor{Admonition}{RGB}{249,249,249}

\usepackage{ifthen}
\usepackage{xcolor}
\usepackage{fourier}

\makeatletter
  \renewenvironment{notice}[2]{%
    \def\thishead{}%
    \ifthenelse{\equal{#1}{tip}}%
	{\colorlet{thiscolor}{white}}%
	{\ifthenelse{\equal{#1}{warning}}
	 {\colorlet{thiscolor}{red!10!white}%
	  \def\thishead{\llap{\smash{\raisebox{-1em}{\small\danger~\,~}}}}}%
	 {\colorlet{thiscolor}{Admonition}}%
	}%
    \begin{lrbox}{\@tempboxa}\begin{minipage}{\columnwidth}%
    \thishead%
  }{%
    \end{minipage}\end{lrbox}%
    \colorbox{thiscolor}{\usebox{\@tempboxa}}%
  }

\makeatother

\def\shadowbox#1{\rule{\linewidth}{1pt}\nopagebreak

\nopagebreak\hspace*{.02\linewidth}#1\nopagebreak

\nopagebreak\rule{\linewidth}{1pt}
}
"""

latex_elements = {
    'papersize': 'a4paper',
    'preamble': preamble,
    'fontpkg': '\\usepackage{lmodern}',
    'fncychap': r'''%
    \usepackage[Sonny]{fncychap}%
    \ChRuleWidth{1.5pt}%
    \ChNumVar{\fontsize{76}{80}\sffamily\slshape}
    \ChTitleVar{\raggedleft\Huge\sffamily\bfseries}''',
    'classoptions': ',oneside,openany',
    'babel': '\usepackage[english]{babel}',
    'releasename': 'Edition',
    'maketitle':
    r'''\includepdf[noautoscale]{cover.pdf}
\makeatletter%
\hypersetup{
    pdfinfo={
        Title={\@title},
        Author={\@author},
        License={CC-BY},
    }
}%
\makeatother%
\newpage\newpage
'''
    #'tableofcontents': '\\pagestyle{normal}\\pagenumbering{arabic} %\\tableofcontents',
}

_python_doc_base = 'https://docs.python.org/2.7'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    _python_doc_base: None,
    'https://docs.scipy.org/doc/numpy': None,
    'https://docs.scipy.org/doc/scipy/reference': None,
    'http://matplotlib.org/': None,
    'http://scikit-learn.org/stable': None,
    'http://scikit-image.org/docs/stable/': None,
    'http://docs.enthought.com/mayavi/mayavi/': None,
    'http://www.statsmodels.org/stable/': None,
    'http://pandas.pydata.org/pandas-docs/stable/': None,
    'http://seaborn.pydata.org/': None,
}

extlinks = {
    'simple': (_python_doc_base + '/reference/simple_stmts.html#%s', ''),
    'compound': (_python_doc_base + '/reference/compound_stmts.html#%s', ''),
}

# -- Options for imgmath ------------------------------------------------

imgmath_dvipng_args = ['-gamma 1.5', '-D 180', '-bg', 'Transparent']
immath_use_preview = True

pngmath_dvipng_args = ['-gamma 1.5', '-D 180', '-bg', 'Transparent']
pngmath_use_preview = True


# Add the 'copybutton' javascript, to hide/show the prompt in code
# examples
def setup(app):
    app.add_javascript('copybutton.js')
