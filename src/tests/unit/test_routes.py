from flask import Flask
from handlers.routes import routes_config

def test_get_route():
    app = Flask(__name__, template_folder='../../templates')
    routes_config(app)
    app.config['TESTING'] = True
    client = app.test_client()

    response = client.get('/')

    assert ('Hello World!' in response.data.decode('utf-8')) == True

def test_post_route():
    app = Flask(__name__, template_folder='../../templates')
    routes_config(app)
    app.config['TESTING'] = True
    client = app.test_client()

    response = client.post('/', data=('banana'))

    print(response)

    # assert ('Hello World!' in response.data.decode('utf-8')) == True
    assert 0

