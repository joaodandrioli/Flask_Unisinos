from flask import Blueprint

hello_bp = Blueprint('hello',__name__)
nome_bp = Blueprint('Olá, João Vitor! ',__name__)

@hello_bp.route('/')
def index():

    return "Hello World" 

@nome_bp.route('/')
def index():
    return "Olá, João Vitor!" 
