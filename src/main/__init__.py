from flask import Blueprint

bp=Blueprint('main',__name__)

from src.main import label
from src.main import task
from src.main import worspace