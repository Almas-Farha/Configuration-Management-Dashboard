from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')


'''from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Configuration  # Ensure this import exists

main = Blueprint('main', __name__)

@main.route('/')
def home():
    configurations = Configuration.query.all()
    return render_template('index.html', configurations=configurations)

@main.route('/add_configuration', methods=['GET', 'POST'])
def add_configuration():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        new_config = Configuration(name=name, description=description)
        db.session.add(new_config)
        db.session.commit()

        return redirect(url_for('main.home'))

    return render_template('add_configuration.html')'''

from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute_playbook', methods=['POST'])
def execute_playbook():
    try:
        command = "ansible-playbook ansible/playbook.yml -i ansible/inventory"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()
        return jsonify({"status": "success", "output": output.decode()}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

