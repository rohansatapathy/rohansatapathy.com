from flask import render_template, redirect, url_for

from blog import app, pages


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


@app.route('/about_me/')
def about_me():
    return "About Me"


@app.route('/posts/')
def posts():
    return "Posts"