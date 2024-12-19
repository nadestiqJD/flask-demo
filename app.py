from logging import exception

from flask import Flask, render_template, request, Response, redirect, url_for

from services import configurationService as conf
from requestHandlers import importsRequestHandler, emailsRequestHandler
from viewmodels import indexViewmodel, emailViewmodel, importsViewmodel

app = Flask(__name__)



# TODO documentation for routes, request handlers and services
@app.route('/')
def index():
    """
    Home page endpoint.
    @return: View of home page.
    """
    vm = indexViewmodel.IndexViewmodel()
    return render_template('index.html', Model=vm)

@app.route('/imports', methods=['GET'])
def imports_get():
    """
    Import recipients page.
    @return: View of imports page.
    """
    vm = importsViewmodel.ImportsViewmodel()
    return render_template('imports.html', Model=vm)

@app.route('/imports', methods=['POST'])
def imports_post():
    """
    [POST] Handler of import recipients form.
    @return: Redirect to email sender page.
    """
    importsRequestHandler.PostHandler(request)
    return redirect(url_for('email_get'))
@app.route('/email', methods=['GET'])
def email_get():
    """
    Email sender page.
    @return: View of email sender page.
    """
    data = emailsRequestHandler.GetHandler()
    vm = emailViewmodel.EmailViewmodel(data)
    return render_template('email.html', Model=vm)

@app.route('/email', methods=['POST'])
def email_post():
    """
    [POST] Handler of email sender.
    @return: Redirect to home page.
    """
    emailsRequestHandler.PostHandler(request)
    return redirect(url_for('index'))

if __name__ == '__main__':
    "settings"
    configuration = conf.getConfiguration()

    env = configuration["env"]
    _HOST = env["Host"] or "0.0.0.0"
    _PORT = env["Port"]
    _ENV = env["Debug"] or False

    "check if application port has been provided"
    if _PORT is None:
        raise exception("No port specified. You must specify a port in appsettings.json.")

    "start flask app"
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(
        host=_HOST,
        port=_PORT,
        debug=_ENV
    )