import psycopg2
from flask import Flask, request, redirect, render_template


app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect('dbname=farfetch')
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

app.run(debug=True, port=5001)