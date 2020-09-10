from flask import Flask, render_template
import datetime as dt
app = Flask(__name__)
@app.route('/')
def home():
    date_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('home.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    
if __name__ == '__main__':
    app.run(debug=True)