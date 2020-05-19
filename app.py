from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db = SQLAlchemy(app)
# init marshmallow (object deserialisation)
ma = Marshmallow(app)
# marshmallow is used to convert datatypes into python readable data

# product class/model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # id being primary integer means its value will increase automatically on product addition
    name = db.Column(db.String(100),unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    # creating constructor to assign passed values to created object
    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# product schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

# init schema
product_schema = ProductSchema()
# for multiple prodcuts
products_schema = ProductSchema(many=True)

# route to create a product

@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# route to Get all products
@app.route("/product", methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

# route to Get single products
@app.route("/product/<id>", methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# route to update a product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    # get data from response
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    # overwrite db data with response data
    product.name = name
    product.description = description
    product.price - price
    product.qty = qty
    # commit necessary to update data
    db.session.commit()

    return product_schema.jsonify(product)


# route to deleted a single product
@app.route("/product/<id>", methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)

# server run
if __name__ == '__main__':
    app.run(debug=True)