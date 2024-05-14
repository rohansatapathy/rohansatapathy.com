from pygments.style import Style
from pygments.token import (
    Comment,
    Keyword,
    Name,
    String,
    Error,
    Generic,
    Number,
    Operator,
)

BLACK = "#1A1A1A"
DARK_GREY = "#606060"
LIGHT_GREY = "#767676"
RED = "#CC6262"
ORANGE = "#D88568"
YELLOW = "#B99353"
GREEN = "#83A471"
DULL_BLUE = "#7C9CAE"
LIGHT_BLUE = "#72A5B3"
PURPLE = "#B36BA3"


class IALight(Style):
    """A Pygments style that mirrors the theme used in the iA Writer app."""

    styles = {
        Comment: LIGHT_GREY,
        Keyword: PURPLE,
        Keyword.Namespace: LIGHT_BLUE,
        Keyword.Type: YELLOW,
        Keyword.Constant: RED,
        Name: ORANGE,
        Name.Builtin: DARK_GREY,
        Name.Class: YELLOW,
        Name.Constant: RED,
        Name.Function: LIGHT_BLUE,
        String: GREEN,
        Error: RED,
        Generic: BLACK,
        Number: RED,
        Operator: BLACK,
    }
