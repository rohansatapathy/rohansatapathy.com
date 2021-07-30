from flask import render_template, redirect, url_for
from flask_flatpages import pygmented_markdown, pygments_style_defs
from pygments.formatters import HtmlFormatter

from blog import app, pages


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:path>/')
def page(path):
    post = pages.get_or_404(path)
    return render_template('post.html', post=post, title=post.meta['title'])


@app.route('/about_me/')
def about_me():
    return "About Me"


@app.route('/posts/')
def posts():
    return "Posts"


@app.route('/pygments.css/')
def pygments_css():
    formatter = HtmlFormatter(style='tango')
    return formatter.get_style_defs('.highlight'), 200, {'Content-Type': 'text/css'}
