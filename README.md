# flask-vuejs

Flask api Rest and VueJS example.

Tutorial de Flask e VueJS adaptado de [building-restful-apis-with-flask](https://code.tutsplus.com/pt/tutorials/building-restful-apis-with-flask-diy--cms-26625).

## Como desenvolver?

```
git clone https://github.com/rg3915/flask-vuejs.git
cd flask-vuejs
python3 -m venv .venv
source .venv/bin/activate
cd my_app/backend
pip install -r requirements.txt
python run.py
```

A app está rodando na porta 5000.

Abra outro terminal e digite:

```
cd my_app/frontend
npm install
npm run dev
```

A app está rodando na porta 8080.

Abra mais um terminal pra inserir alguns dados:

```
Abra o Python, e digite:

```python
source .venv/bin/activate
cd my_app/backend
python
import requests
r = requests.post('http://localhost:5000/product/', data={'name': 'iPhone 6s', 'price': 699})
r = requests.post('http://localhost:5000/product/', data={'name': 'iPad Pro', 'price': 999})
r = requests.post('http://localhost:5000/product/', data={'name': 'bip', 'price': 1000})
r = requests.post('http://localhost:5000/product/', data={'name': 'walkman', 'price': 1200})
r = requests.post('http://localhost:5000/product/', data={'name': 'discman', 'price': 1800})
r = requests.post('http://localhost:5000/product/', data={'name': 'dic vinil', 'price': 450})
r = requests.get('http://localhost:5000/product/')
r.json()
r = requests.get('http://localhost:5000/product/1')
r.json()
exit()
```

## Tutorial

Comece criando duas pastas:

```
mkdir backend frontend
```

Vamos criar uma virtualenv:

```
python3 -m venv .venv
source .venv/bin/activate
pip install flask flask-sqlalchemy flask-cors
pip freeze > requirements.txt
```

[flask-cors stackoverflow](https://stackoverflow.com/a/32749344)

Dentro de `backend` vamos montar a estrutura pra usar o Flask:

```
cd backend
mkdir -p my_app/product
printf "from my_app import app\napp.run(debug=True)" > run.py
touch my_app/__init__.py
touch my_app/product/{__init__,models,views}.py
```

Você deverá ter essa estrutura:

```
.
├── backend
│   ├── my_app
│   │   ├── __init__.py
│   │   └── product
│   │       ├── __init__.py
│   │       ├── models.py
│   │       └── views.py
│   └── run.py
```

Escrevendo os arquivos:

```
cat << EOF > my_app/__init__.py
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from my_app.product.views import product
app.register_blueprint(product)

db.create_all()
EOF
```

Editando `models.py`

```
cat << EOF > my_app/product/models.py
from my_app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float(asdecimal=True))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return '<Product %d>' % self.id
EOF
```

Editando `views.py`

```
cat << EOF > my_app/product/views.py
import json
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
        if not id:
            products = Product.query.paginate(page, 10).items
            res = {}
            for product in products:
                res[product.id] = {
                    'name': product.name,
                    'price': str(product.price),
                }
        else:
            product = Product.query.filter_by(id=id).first()
            if not product:
                abort(404)
            res = {
                'name': product.name,
                'price': str(product.price),
            }
        return jsonify(res)

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
EOF
```

### Rodando a app

```
python run.py
```

A app está rodando na porta http://localhost:5000/


## Testando a api fazendo requisições com Python

Vamos instalar o [requests](http://docs.python-requests.org/en/master/).

Abra um outro terminal, ative a virtualenv e digite:

```
source .venv/bin/activate
pip install requests
```

Abra o Python, e digite:

```
python
import requests
r = requests.post('http://localhost:5000/product/', data={'name': 'iPhone 6s', 'price': 699})
r = requests.post('http://localhost:5000/product/', data={'name': 'iPad Pro', 'price': 999})
r = requests.post('http://localhost:5000/product/', data={'name': 'bip', 'price': 1000})
r = requests.post('http://localhost:5000/product/', data={'name': 'walkman', 'price': 1200})
r = requests.post('http://localhost:5000/product/', data={'name': 'discman', 'price': 1800})
r = requests.post('http://localhost:5000/product/', data={'name': 'dic vinil', 'price': 450})
r = requests.get('http://localhost:5000/product/')
r.json()
r = requests.get('http://localhost:5000/product/1')
r.json()
exit()
```


## Frontend

Vamos para a pasta `frontend`.

```
cd frontend
vue init webpack .
npm install
npm install --save axios
npm run dev
```

A app está rodando na porta http://localhost:8080

Veja alguns arquivos:

App.vue
components/Product.vue
