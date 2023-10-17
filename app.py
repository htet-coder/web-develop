from flask import Flask, render_template, jsonify, url_for, redirect

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title':'QGIS Basic Training',
        'fee':'ks. 40,000',
        'duration': '3 month',
        'type':'In-Person'
    },
    {
        'id': 2,
        'title':'QGIS Intermediate Training',
        'fee':'ks. 30,000',
        'duration': '2 month',
        'type':'Online'
    },
    {
        'id': 3,
        'title':'Basic Python Programming Training',
        'fee':'ks. 40,000',
        'duration': '3 month',
        'type':'In-Person'
    },
        {
        'id': 4,
        'title':'Data Management Traning',
        'fee':'ks. 40,000',
        'duration': '3 month',
        'type':'In-Person'
    }
]

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS, company='Futrue Perspective Myanmar')

@app.route('/home', methods=['GET', 'POST'])
def home_page():
    return render_template('home.html', jobs=JOBS, company='Futrue Perspective Myanmar')

@app.route('/service', methods=['GET', 'POST'])
def services():
    return render_template('services.html')

@app.route('/api/jobs')
def job_list():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)