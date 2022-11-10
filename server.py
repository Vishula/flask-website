import psycopg2
from flask import Flask, request, redirect, render_template
import os

DB_URL = os.environ.get('DATABASE_URL', 'dbname=farfetch')

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") 
@app.route('/')
def homepage():
    
    return render_template('base.html')

@app.route('/shop')
def shop():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT id, name, price, image_url, description price FROM clothes')
    results = cur.fetchall()

    product_items = []
    for row in results: 
        id, name, price, image_url, description = row 
        price = f'${price/100:.2f}'
        product_items.append([id, name, price, image_url, description])
        
    cur.close()
    conn.close()
    
    return render_template('shop.html', product_items=product_items)

@app.route('/blog')
def blog():

    return render_template('blog.html')
@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/create')
def create():

    return render_template('signup.html')

 
if __name__ == '__main__':
    app.run(debug=True, port=5002)