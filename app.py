from flask import *

app = Flask(__name__)
app.secret_key = 'asjkdlfhasjkldfhkalsjhf'

@app.route('/')
def home():
    if 'name' in session:
        return render_template('index.html', name=session['name'] + '?')
    return render_template('index.html')

# @app.route('/<name>')
# def hello(name):
#     session['name'] = name
#     return render_template('index.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['username']
        print(request.form['username'], request.form['password'])
        return render_template('index.html', name=session['name'])
    
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/logout')
def logout():
    if 'name' in session:
        session.pop('name', None)
    return redirect(url_for('home'))

@app.errorhandler(404)
def error_404(error):
    return render_template('error.html', error=error)

if __name__ == "__main__":
    app.run(port=5500, debug=True)