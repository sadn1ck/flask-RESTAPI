# Simple REST API using Flask, SQLAlchemy

## Instructions to setup local server:
* `pip3 install pipenv`
* `git clone https://github.com/sadn1ck/flask-RESTAPI`
* `cd flask-RESTAPI`
* `pipenv install`
* `pipenv shell`
* `python app.py`

## How to check its working?

* Use Postman
* Data returned is JSON
* POST to `https://localhost:5000/product` to create new product
* GET to `https://localhost:5000/product` to get all products
* GET to `https://localhost:5000/product/2` to get second product
* PUT to `https://localhost:5000/product/2` to update second product
* DELETE to `https://localhost:5000/product/1` to delete first product

## Future

* Thinking of changing this to a random quote generator
* Maybe get the most words searched last week on Google and cobble them to form random garbage LOL
* PRs welcome