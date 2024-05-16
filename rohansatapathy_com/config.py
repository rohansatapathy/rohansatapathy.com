import pymdownx.arithmatex as arithmatex


class Config:
    """Class to store configuration variables for blog."""

    # FlatPages config
    DEBUG = True
    FLATPAGES_ROOT = "../posts/"
    FLATPAGES_EXTENSION = ".md"
    FLATPAGES_AUTO_RELOAD = DEBUG
    FLATPAGES_MARKDOWN_EXTENSIONS = [
        "pymdownx.highlight",
        "pymdownx.inlinehilite",
        "pymdownx.superfences",
        "pymdownx.arithmatex",
    ]
    FLATPAGES_EXTENSION_CONFIGS = {
        "pymdownx.highlight": {
            "linenums": "None",  # Setting linenums to None enables per-code-block customization
            "linenums_style": "pymdownx-inline",
        },
        "pymdownx.superfences": {
            "css_class": "highlight p-3 mw-100 rounded-3 border mb-3",
            "custom_fences": [
                {
                    "name": "math",
                    "class": "arithmatex",
                    "format": arithmatex.arithmatex_fenced_format(which="generic"),
                }
            ],
        },
        "pymdownx.inlinehilite": {
            "css_class": "highlight px-1 rounded-1 border",
        },
        "pymdownx.arithmatex": {"generic": "True"},
    }
