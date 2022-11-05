import psycopg2
from models.repository import sql_select
from flask import Flask, request, redirect, render_template


app = Flask(__name__)

@app.route('/')
def index():
    results = sql_select("SELECT id, name, price, description, image_url")
    items = []
    for row in results:
        (product_id, name, price) = row
        items.append({'id': product_id, 'name':name, 'price': price})

    return render_template('index.html', items=items)
 

app.run(debug=True, port=5001)