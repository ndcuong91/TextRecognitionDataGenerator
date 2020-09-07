"""
Utility functions
"""

import os


def load_dict(lang, corpus_dir='corpus'):
    """Read the dictionnary file and returns all words in it.
    """

    lang_dict = []
    with open(
        os.path.join(os.path.dirname(__file__), corpus_dir, lang + ".txt"),
        "r",
        encoding="utf8",
        errors="ignore",
    ) as d:
        lang_dict = [l for l in d.read().splitlines() if len(l) > 0]
    return lang_dict


def load_fonts(lang):
    """Load all fonts in the fonts directories
    """

    if lang in ("ar", "cn", "hi"):
        return [
            os.path.join(os.path.dirname(__file__), "fonts/{}".format(lang), font)
            for font in os.listdir(
                os.path.join(os.path.dirname(__file__), "fonts/{}".format(lang))
            )
        ]
    else:
        return [
            os.path.join(os.path.dirname(__file__), "fonts/latin", font)
            for font in os.listdir(
                os.path.join(os.path.dirname(__file__), "fonts/latin")
            )
        ]
