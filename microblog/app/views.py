from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = { 'nickname' : 'Tomas' } #fake user
    app.logger.debug("index page requested")
    return render_template('index.html',
                            title = 'Home',
                            user = user)

@app.errorhandler(404)
def page_not_found(e):
    app.logger.debug("page not found")
    return "not found"

