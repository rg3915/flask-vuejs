from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.product.models import Product

product = Blueprint('product', __name__)


@product.route('/')
@product.route('/home')
def home():
    return "Welcome to the product Home."


class ProductView(MethodView):

    def get(self, id=None, page=1):
        _list = []
        if not id:
            products = Product.query.paginate(page, 10).items
            for product in products:
                _list.append(
                    {
                        'name': product.name,
                        'price': str(product.price),
                    }
                )
        else:
            product = Product.query.filter_by(id=id).first()
            if not product:
                abort(404)
            _list.append(
                {
                    'name': product.name,
                    'price': str(product.price),
                }
            )
        data = {'data': _list}
        return jsonify(data)

    def post(self):
        name = request.form.get('name')
        price = request.form.get('price')
        product = Product(name, price)
        db.session.add(product)
        db.session.commit()
        return jsonify({product.id: {
            'name': product.name,
            'price': str(product.price),
        }})

    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return

    def delete(self, id):
        # Delete the record for the provided id.
        return


product_view = ProductView.as_view('product_view')
app.add_url_rule(
    '/product/', view_func=product_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/product/<int:id>', view_func=product_view, methods=['GET']
)
