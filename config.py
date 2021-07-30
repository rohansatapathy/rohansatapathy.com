class Config:
    """Class to store configuration variables for blog"""

    # FlatPages config
    DEBUG = True
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_AUTO_RELOAD = DEBUG
    FLATPAGES_MARKDOWN_EXTENSIONS = ['pymdownx.highlight', 'pymdownx.inlinehilite', 'pymdownx.superfences']
    FLATPAGES_EXTENSION_CONFIGS = {
        'pymdownx.highlight': {
            'linenums': 'True',
            'linenums_style': 'inline',
        },
        'pymdownx.superfences': {
            'css_class':  "highlight pt-3 pb-1 px-2 mw-100 rounded-3 border" ,
        },
        'pymdownx.inlinehilite': {
            'css_class': "highlight py-1 px-1 rounded-1 border"
        }
    }