import os, sys
sys.path.insert(0, 'venv/bin/lib/python3.10/site-packages') 
from flask import Flask,redirect,url_for,render_template,request
#from flask_mysqldb import MySQL
import jinja2
from flask_sqlalchemy import SQLAlchemy
import time

from sqlalchemy import(
    Boolean,
    Integer,
    String,
    Column,

)



app=Flask(__name__)

dbuser = 'root'
dbpass = 'MyN3wP4ssw0rd'
dbhost = 'localhost'
dbname = 'market'

print(dbuser,dbpass,dbhost,dbname); #time.sleep(100)
app.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://{dbuser}:{dbpass}@{dbhost}/{dbname}".format(
						                                        dbuser=dbuser,
						                                        dbpass=dbpass,
						                                        dbhost=dbhost,
						                                        dbname=dbname)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://market:mosudstrongpassword@localhost/market'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# app.config['MYSQL_HOST'] ="localhost"
# app.config['MYSQL_USER'] ="market"
# app.config['MYSQL_PASSWORD'] ="mosudstrongpassword"
# app.config['MYSQL_DB'] ="market"

#mysql = MySQL(app)
db = SQLAlchemy(app)


class Items(db.Model):
    id      = Column(Integer(), primary_key=True )
    name    = Column(String(30), nullable=False)
    price   = Column(Integer(), nullable=False, unique=True)
    barcode     = Column(String(12), nullable=False, unique=True)
    description = Column(String(1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'


@app.route('/',methods=['GET','POST'])
def home_page():
    if request.method=='POST':
        # Handle POST Request here
        
        return render_template('home.html')
    return render_template('home.html')

@app.route('/market')
def market_page():

    items = Items.query.all()
    return render_template('market.html', items=items)



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)