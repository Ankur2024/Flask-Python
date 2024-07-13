from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',)
    # return 'Hello, World'
@app.route('/products')
def products():
    return 'Hello, World in the product.'

if __name__ == "main":
    app.run(debug=True)