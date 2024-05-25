import math

from flask import render_template
from pygments.formatters import HtmlFormatter

from rohansatapathy_com.styles import IALight

from .app import app, pages


@app.route("/")
def index():
    return posts()


@app.route("/blog/<path:path>")
def post(path):
    post = pages.get_or_404(path)
    WORDS_PER_MIN = 130
    num_words = len([word for word in post.body.split() if word.isalnum()])
    read_time = math.ceil(num_words / WORDS_PER_MIN)
    return render_template(
        "post.html", post=post, title=post["title"], read_time=read_time
    )


@app.route("/about")
def about():
    return render_template("about.html", title="About Me")


@app.route("/blog/")
def posts():
    posts = sorted(pages, reverse=True, key=lambda p: p.meta["date"])
    return render_template(
        "posts.html", title="Posts", posts=posts, debug=app.config["DEBUG"]
    )


@app.route("/pygments.css")
def pygments_css():
    formatter = HtmlFormatter(style=IALight)
    return formatter.get_style_defs(".highlight"), 200, {"Content-Type": "text/css"}
