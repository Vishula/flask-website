import psycopg2
from flask import Flask, request, redirect, render_template
import os

DB_URL = os.environ.get('DATABASE_URL', 'dbname=farfetch')

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT id, name, price, image_url price FROM clothes')
    results = cur.fetchall()

    product_items = []
    for row in results: 
        id, name, price, image_url = row 
        price = f'${price/100:.2f}'
        product_items.append([id, name, price, image_url])
        print('test commit')
    cur.close()
    conn.close()
    


    return render_template('index.html', product_items=product_items)
# @app.route('/about')
# def about():
# Test Commits 
if __name__ == '__main__':
    app.run(debug=True, port=5001)