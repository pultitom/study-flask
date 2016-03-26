from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = { 'nickname' : 'Tomas' } #fake user
    posts = [
        {
            'author': { 'nickname' : 'Jonas' },
            'body' : 'Beautiful day in Vilnius'
        },
        {
            'author' : { 'nickname' : 'Susan' },
            'body' : 'The Avengers movie is cool. Except capt. America character of course'
        }
    ]

    app.logger.debug("index page requested")
    return render_template('index.html',
                            title = 'Home',
                            user = user,
                            posts = posts)


@app.route("/new")
def new():
    app.logger.debug("new page requestet")
    return render_template("index.html",
            user = { 'nickname' : 'Tomas' })


@app.errorhandler(404)
def page_not_found(e):
    app.logger.debug("page not found")
    return "not found"

