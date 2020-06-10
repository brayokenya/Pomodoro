from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options





bootstrap = Bootstrap()
def create_app(config_name):
    # initialize app
    app = Flask(__name__)
    #create app configurations
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    #registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app