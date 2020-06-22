from flask import render_template

def routes_config(app):

    @app.route('/')
    def get_data():
        data = "Hello, World"
        return render_template('index.html', data=data)
