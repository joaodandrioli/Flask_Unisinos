from flask import Blueprint

nome_bp = Blueprint('Olá, João Vitor! ',__name__)

@nome_bp.route('/')
def index():
    return "Olá, João Vitor!" 