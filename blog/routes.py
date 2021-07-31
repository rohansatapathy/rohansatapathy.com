from flask import render_template, redirect, url_for
from flask_flatpages import pygmented_markdown, pygments_style_defs
from pygments.formatters import HtmlFormatter

from blog import app, pages


@app.route('/')
def index():
    return render_template('posts.html', posts=pages)


@app.route('/blog/<path:path>/')
def page(path):
    post = pages.get_or_404(path)
    return render_template('post.html', post=post, title=post['title'])


@app.route('/about-me/')
def about_me():
    return render_template('about_me.html', title='About Me')


@app.route('/blog/posts/')
def posts():
    return render_template('posts.html', title="Posts", posts=pages)


@app.route('/pygments.css/')
def pygments_css():
    formatter = HtmlFormatter(style='tango')
    return formatter.get_style_defs('.highlight'), 200, {'Content-Type': 'text/css'}
