---
title: How I Built This Website
author: Rohan Satapathy
date: 2022-04-25
desc: A summary of my journey building this website
published: true
---

Hello and welcome to my first post! In this post, I'll be explaining how I built my blog, some of the issues I had along the way, and how I solved them. This project took a considerable amount of time as it's is the first complete project that I've made, but I had a lot of fun doing it and I'm pretty proud of how it turned out! If you would like to see the code for the blog, I've made it [open source on GitHub](https://github.com/rohansatapathy/rohansatapathy.com) so anyone can check it out and even use it as a base for their own blog. 

## Introduction

I built this website using Python because it's the language I'm most proficient in. Within Python, there are two popular web frameworks to choose from: [Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/en/2.0.x/). While Django is a fuller-featured framework that automates features like databases, user login, etc, I chose not to use it because I wanted to use this project as an opportunity to learn about how each of these features works rather than having a framework automate it all for me. Flask is considered a micro-framework rather than a framework because it enables the user to choose which features they need, so it fit the bill perfectly. 

After picking my framework, my next step was to learn how to use Flask. To do this, I turned to Miguel Grinberg's [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), which is a 23-part series that meticulously describes many different aspects of web development with Flask. After reading the first eleven parts of the tutorial (which covered application structure, templates, forms, databases, styling, etc.) I felt that I had gained enough proficiency with Flask to start writing this blog.

## Features

Before building this blog, I knew that I wanted it to be able to support several features. 

First, I wanted to be able to write posts in Markdown rather than pure HTML because it is faster to use and easier to read. To do this, I made use of flask extensions, which are libraries that add functionality to flask. Specifically, I used the `:::text flask-flatpages` extension, which creates static pages based on markdown files. 

Next, since this is partially a blog about programming, I wanted the blog to support both in-line and standalone code highlighting with support for multiple languages. Although python's `:::text markdown` library supports these features, it is limited in both functionality and customizability, which in turn led me to use [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/), a collection of extensions that enables several features, code highlighting included. I used the `:::text Highlight`, `:::text SuperFences`, and `:::text InlineHilite` extensions for syntax highlighting, code blocks, and inline code highlighting respectively. 

I also wanted to be able to write math equations in case I needed to write about mathematics concepts in the future. The `:::text Arithmatex` extension from PyMdown Extensions combined with $\KaTeX$, a JavaScript $\TeX$ rendering library, allowed me to do this. 

Finally, I wanted the website to have a consistent style across many different device types, including mobile devices. Instead of writing CSS manually to accomodate these requirements, I chose to use Bootstrap, a CSS framework that automates the creation of responsive layouts and comes with several utility classes that makes styling a website much easier. 

With these feature requirements established, it is now possible for me to discuss the application structure. 

## Application Structure

Below is a tree of the project's application structure:

```
.
├── LICENSE
├── README.md
├── app
│   ├── __init__.py
│   ├── pages
│   │   └── how-i-built-this-website.md
│   │   └──...
│   ├── routes.py
│   ├── static
│   │   ├── arithmatex-auto-render.js
│   │   ├── images
│   │   │   └── ...
│   │   └── styles.css
│   └── templates
│       ├── about_me.html
│       ├── base.html
│       ├── post.html
│       └── posts.html
├── blog.py
├── config.py
├── poetry.lock
└── pyproject.toml
```

The main code for the website is stored inside the `:::text app` directory. Inside `:::text app` there are several files and folders. The main python files that run the backend of the website are `:::text __init__.py` and `:::text routes.py`. `:::text __init__.py` exposes the application instance as well as instances of the Flask extensions mentioned earlier, and `:::text routes.py` defines which URLs map to which pages. 

The `:::text app` directory also contains the `:::text pages`, `:::text static`, and `:::text templates` subdirectories. The `:::text pages` directory is where all the blog posts are stored in markdown format. The `:::text static` directory contains the JavaScript and CSS files needed to make the website run, as well as any images I might need to include for future posts. Finally, the `:::text templates` directory stores all of the HTML files needed for the website. Since Flask uses a templating engine called Jinja2, I am able to make a single 'template' page that can be used to render all blog posts from their respective markdown files. 

Outside of the `:::text app` directory are two python files (`:::text blog.py` and `:::text config.py`) as well as two files related to dependency management (`:::text pyproject.toml` and `:::text poetry.lock`). `:::text blog.py` contains a single line of code that starts the application when run. `:::text config.py` contains the configuration variables necessary to render the blog posts, stored as class variables. `:::text pyproject.toml` and `:::text poetry.lock` are both files used by [Poetry](https://python-poetry.org/), a dependency and environment manager for python projects. Poetry has been indispensable in creating this blog because it made dependency management much easier than if I were to use `:::text pip` and `:::text venv`, the dependency and virtual environment tools built into python.  

## Displaying Blog Posts

Let's take a closer look at how blog posts are displayed. The first step in displaying blog posts is the view function, which is contained in `:::text routes.py`. 

```{.python linenums="13"}
@app.route('/blog/<path:path>/')
def page(path):
    post = pages.get_or_404(path)
    return render_template('post.html', post=post, title=post['title'])
```
The decorator `:::py3 @app.route('/blog/<path:path>/')` defines the URL that corresponds to the view function. In this case, there's a path a placeholder variable that defines where the currently requested post is. I've configured the application structure that any path after "rohansatapathy.com/blog/" corresponds to the location of the markdown file relative to the `:::text pages` directory. This path is passed into the view function as a parameter in the view function `:::py3 page()`. 

Next, the chosen post is converted to a `:::py3 Post` object via the `:::py3 get_or_404()` function, which is provided by the flask-flatpages extension and simply returns the post as an object or redirects to a 404 page. Afterwards, the `:::py3 render_template()` function is called, which parses `:::text post.html` using the data passed in the subsequent arguments and returns the resulting HTML. 

Speaking of `:::text post.html`, let's take a closer look at the blog post template:

```{.html linenums="1"}
{% extends 'base.html' %}


{% block content %}
  <div class="bg-light border rounded-2 py-4">
    <h1 class="my-3 text-center">{{ post.title }}</h1>
    <h6 class="my-3 text-center">{{ post.date }}</h6>
  </div>
  <div class="py-5">
      {{ post }}
  </div>
{% endblock %}
```

This file doesn't look like standard HTML because it makes use of Jinja2, a templating engine that comes with Flask. I've defined a base template called `:::text base.html`, which contains the general template for all pages on the website, which includes Bootstrap CSS/JS, my custom styles, and the navbar, which all have to appear on every page. This way, the same code doesn't have to be duplicated across each page. 

The first line, `:::html {% extends 'base.html' %}` allows the blog post page to share the same code as the base template. The subsequent lines are wrapped in block tags because there's a similar pair in `:::text base.html`. When the page is rendered, the resulting HTML will look like the base template with the customized post content inserted in the correct location.

The double curly-braces inside the content block work in a similar way, except they enable the addition of python code inside the template. This is why the reference to `:::py3 post.title` and `:::py3 post.date` work; they're references to the `:::py3 post` object passed in through `:::py3 render_template()`.

## Some Extra Features

### Syntax Highlighting and Code Blocks

After displaying posts, the next task I had to complete was to implement syntax highlighting, block code, and equations, all of which required the use of various extensions in the `:::py3 pymdownx` library. 

In order to integrate markdown extensions into flask-flatpages, I had to pass them into the Flask configuration, which I opted to do via the `:::py3 Config` class:

```{.python linenums="1"}
class Config:
    """Class to store configuration variables for blog"""

    # FlatPages config
    DEBUG = True
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_AUTO_RELOAD = DEBUG
    FLATPAGES_MARKDOWN_EXTENSIONS = ['pymdownx.highlight', 'pymdownx.inlinehilite', 'pymdownx.superfences', 'pymdownx.arithmatex']
    FLATPAGES_EXTENSION_CONFIGS = {
        'pymdownx.highlight': {
            'linenums': 'None',  # Setting linenums to None enables per-code-block customization
            'linenums_style': 'pymdownx-inline'
        },
        'pymdownx.superfences': {
            'css_class':  "highlight px-3 py-3 mw-100 rounded-3 border mb-3",
        },
        'pymdownx.inlinehilite': {
            'css_class': "highlight px-1 rounded-1 border",
        },
        'pymdownx.arithmatex': {
            'generic': 'True'
        }
    }
```

This class contains several class variables which get interpreted as configuration variables in `:::text __init__.py`. The two variables that are of interest here are `:::py3 FLATPAGES_MARKDOWN_EXTENSIONS` and `:::py3 FLATPAGES_EXTENSION_CONFIGS`, which allowed me to define which extensions to use and add parameters for each, respectively. 

To implement syntax highlighting and better code fences, I used the `:::text Highlight`, `:::text InlineHilite`, and `:::text SuperFences` extensions. The `:::text css_class` option allows CSS classes to be applied to all members of each extension, and I've included various Bootstrap classes for each extension to style both the inline and fenced code more efficiently. 

One feature that I found particularly useful for the reader's experience was the custom line number format in `:::python pymdownx.highlight`. Rather than display line numbers in an HTML table or in-line with the code, this format displays the line numbers using a CSS selector: 

```{.css linenums="60"}
[data-linenos]:before {
  content: attr(data-linenos);
  color: hsl(208, 7%, 60%) !important
}
```

Due to this CSS selector, if a reader wishes to copy some code from my blog in the future to try it out for themselves, the line numbers won't be a part of the text selection, meaning they won't have to go through the tedious process of editing out the line numbers manually for the code to work. In fact, you can try it out right now if you'd like - highlight the custom CSS code and see what happens.

### Math Equations

To support math equations, I used the `:::py3 pymdownx.arithmatex` extension. I chose to configure the extension to use $\KaTeX$ rather than the default rendering library, MathJax, because $\KaTeX$ is much faster. Aside from including the extension in `:::py3 Config` and configuring the appropriate rendering format, I also included some JavaScript from the Arithmatex docs which ensured that $\KaTeX$ rendered only the code that used the `:::text arithmatex` class. 

The final result is that I am able to include both inline equations, such as $y = mx+b$ and standalone equations, such as 

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.$$

## Next Steps

So that's my website! Creating this website took a lot of work because I had to learn a lot of new things along the way, but I'm really proud of how it turned out. I'm planning to write new posts as often as I can, which is going to be pretty difficult with school and college applications coming up. For now, you can expect to see posts every couple of weeks or so. 

I'm also going to be continuing to make improvements to the website in the meanwhile to make the reading experience better. One feature I want to add as soon as possible is some way to get reader feedback since I have no way to do that right now. I'm thinking of adding a comment system (such as Disqus or Commento) and/or a "like" button similar to the one on blogs on Medium. I'm also going to add a footer to the website when I get a chance. However, I want to make sure that my writing takes priority over cosmetic features on the website so I'm going to focus my time and energy on that. 

That's all for my first post. Thank you for reading!
