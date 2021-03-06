from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.product.models import Product

product = Blueprint('product', __name__)


@product.route('/')
@product.route('/home')
def home():
    return "Welcome to the product Home."


class ProductViewRequests(MethodView):
    '''
    ProductView to use with requests.
    '''

    def post(self):
        data = request.form
        name = data.get('name')
        price = data.get('price')
        product = Product(name, price)
        db.session.add(product)
        db.session.commit()
        product_dict = {
            product.id: {
                'name': product.name,
                'price': str(product.price),
            }
        }
        return jsonify(product_dict)


class ProductView(MethodView):

    def get(self, id=None, page=1):
        _list = []
        if not id:
            products = Product.query.paginate(page, 20).items
            for product in products:
                product_dict = {
                    'id': product.id,
                    'name': product.name,
                    'price': str(product.price),
                }
                _list.append(product_dict)
        else:
            product = Product.query.filter_by(id=id).first()
            if not product:
                abort(404)
            product_dict = {
                'id': product.id,
                'name': product.name,
                'price': str(product.price),
            }
            _list.append(product_dict)
        data = {'data': _list}
        return jsonify(data)

    def post(self):
        data = request.json
        name = data.get('name')
        price = float(data.get('price'))
        product = Product(name, price)
        db.session.add(product)
        db.session.commit()
        product_dict = {
            'id': product.id,
            'name': product.name,
            'price': str(product.price),
        }
        data = {'data': product_dict}
        return jsonify(data)

    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return

    def delete(self, id):
        # Delete the record for the provided id.
        product = Product.query.filter_by(id=id).first()
        db.session.delete(product)
        db.session.commit()
        response = {'message': 'Success'}
        return jsonify(response)


product_view_requests = ProductViewRequests.as_view('product_view_requests')
product_view = ProductView.as_view('product_view')

app.add_url_rule(
    '/product/',
    view_func=product_view,
    methods=['GET', 'POST']
)


app.add_url_rule(
    '/product/<int:id>',
    view_func=product_view,
    methods=['GET', 'DELETE']
)
