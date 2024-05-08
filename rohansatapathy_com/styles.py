from pygments.style import Style
from pygments.token import (
    Token,
    Comment,
    Keyword,
    Name,
    String,
    Error,
    Generic,
    Number,
    Operator,
)


class IALight(Style):
    """A Pygments style that mirrors the theme used in the iA Writer app."""

    styles = {
        Token: "",
        Comment: "#AAAAAA",
        Keyword: "#AAAAAA",
        Name: "#AAAAAA",
        String: "#AAAAAA",
        Error: "#AAAAAA",
        Generic: "#AAAAAA",
        Number: "#AAAAAA",
        Operator: "#AAAAAA",
    }
