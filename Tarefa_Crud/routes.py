from flask import render_template, request, redirect, url_for
from models import db, Tarefa

def init_routes(app):
    @app.before_first_request
    def create_tables():
        db.create_all()

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            descricao = request.form.get('descricao', '').strip()
            if descricao and not Tarefa.query.filter_by(descricao=descricao).first():
                nova = Tarefa(descricao=descricao)
                db.session.add(nova)
                db.session.commit()
            return redirect(url_for('index'))

        tarefas = Tarefa.query.order_by(Tarefa.id.desc()).all()
        return render_template('index.html', tarefas=tarefas)

    @app.route('/delete/<int:tarefa_id>', methods=['POST'])
    def delete(tarefa_id):
        tarefa = Tarefa.query.get_or_404(tarefa_id)
        db.session.delete(tarefa)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/edit/<int:tarefa_id>', methods=['GET', 'POST'])
    def edit(tarefa_id):
        tarefa = Tarefa.query.get_or_404(tarefa_id)
        if request.method == 'POST':
            descricao = request.form.get('descricao', '').strip()
            if descricao and not Tarefa.query.filter(Tarefa.descricao == descricao, Tarefa.id != tarefa.id).first():
                tarefa.descricao = descricao
                db.session.commit()
            return redirect(url_for('index'))
        return render_template('edit.html', tarefa=tarefa)
