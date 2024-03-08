from flask import Blueprint

bp=Blueprint('profile', __name__)

from src.profile import routes