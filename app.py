from flask import Flask, render_template

from controllers.myth_controller import creatures_blueprint
from controllers.myth_controller import habitats_blueprint

app = Flask(__name__)

app.register_blueprint(creatures_blueprint)
app.register_blueprint(habitats_blueprint)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)