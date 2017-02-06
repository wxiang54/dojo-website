from flask import Flask, render_template
from sys import argv
from werkzeug.contrib.fixers import ProxyFix

from lib.security.security import security
from lib.views.public import public_views
from lib.views.private import private_views
from lib.util import log_name

####  ALL OF THIS STUFF SHOULD REMAIN FREE FLOATING ####
app = Flask(__name__)
app.register_blueprint(security)
app.register_blueprint(public_views)
app.register_blueprint(private_views)

app.wsgi_app = ProxyFix(app.wsgi_app)
try:
    app.secret_key = argv[argv.index('--key') + 1]
except ValueError:
    app.secret_key = 'afsdhghjkasdfUASGFDHusdfhyaYYJHJSDF'

@app.errorhandler(404)
@log_name
def page_not_found(error):
    return render_template('404.html'), 404

#### FREE FLOATING SECTION ENDS HERE ####
    
def run():
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)

if __name__ == '__main__':
    run()
