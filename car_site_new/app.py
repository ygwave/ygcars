from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cars')
def cars():
    cars_list = ['BMW', 'Audi', 'Mercedes', 'Lada', 'Toyota']
    return render_template('cars.html', cars=cars_list)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)