from config import Config
from flask import Flask
from src.extensions import db
from flask_login import LoginManager
from flask_session import Session
import datetime

def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    app.config['PERMANENT_SESSION_LIFETIME'] =  datetime.timedelta(minutes=10)
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SECRET_KEY"]="manisharmathegod"
    Session(app)

    logInManager= LoginManager()
    logInManager.login_view='auth.login'
    logInManager.init_app(app)

    from src.models.user import User

    @logInManager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from src.main import bp as main_bp
    from src.auth import bp as auth_bp
    from src.profile import bp as profile_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)



    return app