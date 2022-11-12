import psycopg2
import requests
import bcrypt
from flask import Flask, session, request, redirect, render_template, flash
import os

DB_URL = os.environ.get('DATABASE_URL', 'dbname=farfetch')

app = Flask(__name__)
# app.secret_key="anystringhere"
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
@app.route('/loginpage')
def loginpage():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():

    email = request.form.get('email')
    password = request.form.get('password')

    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT id, email, user_password FROM users where email = %s', [email])
    
    userdata = cur.fetchone()
 
    cur.close()
    conn.close()
    
    if userdata:
        if bcrypt.checkpw(password.encode(), userdata[2].encode()):
            session['id'] = userdata[0]
            flash("You logged In")
            return redirect('shop')
    else: 
        flash("User doesn't Exist")
        return redirect('loginpage')

    return render_template('loginpage.html')

@app.route('/createpage')
def createpage():

    return render_template('signup.html')

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, email, user_password) VALUES (%s, %s, %s)', [name, email, password])
    flash('Successfully Created an Account.')
    conn.commit()
    cur.close()
    conn.close()
    return redirect ('loginpage')
 
if __name__ == '__main__':
    app.run(debug=True, port=5002)