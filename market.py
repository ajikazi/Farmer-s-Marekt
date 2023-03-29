from flask import Flask,redirect,url_for,render_template,request
from flask_mysqldb import MySQL
import jinja2
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import(
    Boolean,
    Integer,
    String,
    Column,

)



app=Flask(__name__)

app.config['MYSQL_HOST'] ="localhost"
app.config['MYSQL_USER'] ="market"
app.config['MYSQL_PASSWORD'] ="mosudstrongpassword"
app.config['MYSQL_DB'] ="market"

mysql = MySQL(app)


class Item(db.Model):
    id      = Column(Integer(), primary_key=True )
    name    = Column(String(30), nullable=False)
    price   = Column(Integer(), nullable=False, unique=True)
    barcode     = Column(String(12), nullable=False, unique=True)
    description = Column(String(1024), nullable=False, unique=True)



@app.route('/',methods=['GET','POST'])
def home_page():
    if request.method=='POST':
        # Handle POST Request here
        
        return render_template('home.html')
    return render_template('home.html')

@app.route('/market')
def market_page():

    items = [
    {'id': 1, 'name': 'Honey Beans', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Jamila Rice', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Long-grained Rice', 'barcode': '231985128446', 'price': 150}
]

    return render_template('market.html', items=items)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)