from flask import render_template
from pygments.formatters import HtmlFormatter

from .app import app, pages


@app.route("/")
def index():
    posts = sorted(pages, reverse=True, key=lambda p: p.meta["date"])
    return render_template("posts.html", posts=posts)


@app.route("/blog/<path:path>/")
def page(path):
    post = pages.get_or_404(path)
    return render_template("post.html", post=post, title=post["title"])


@app.route("/about-me/")
def about_me():
    return render_template("about_me.html", title="About Me")


@app.route("/blog/")
def posts():
    return render_template("posts.html", title="Posts", posts=pages)


@app.route("/pygments.css/")
def pygments_css():
    formatter = HtmlFormatter(style="tango")
    return formatter.get_style_defs(".highlight"), 200, {"Content-Type": "text/css"}
