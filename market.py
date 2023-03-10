from flask import Flask,redirect,url_for,render_template,request
import jinja2
from flask_sqlalchemy import SQLAlchemy


from sqlalchemy import(
    Boolean,
    Integer,
    String,
    Column,

)


# Database details
username    = "market"
password    = "mosudstrongpassword"
dbhost      = "localhost"
db_name     = "market"

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{username}:{password}@{dbhost}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app)


with app.app_context():
    db.create_all()



class Item(db.Model):
    id      = Column(Integer(), primary_key=True )
    name    = Column(String(20), nullable=False)
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
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]

    return render_template('market.html', items=items)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)