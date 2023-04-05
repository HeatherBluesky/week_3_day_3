from app import app
from flask import render_template
from models.toorder import orders

@app.route('/')
def index():
    return render_template('index.html', title='Home', orders_var=orders)

@app.route('/<int:id>')
def  eren_order(id):
   return render_template('eren.html', title='Eren order', order=orders)

