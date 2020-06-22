from flask import Flask
from handlers.routes import routes_config

app = Flask(__name__, template_folder='templates')
routes_config(app)

# run the application
if __name__ == "__main__":  
    app.run(host='0.0.0.0',debug=True,port=7676)
