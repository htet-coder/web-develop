from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title':'Data Analyst',
        'salary':'ks. 1200000',
        'country':'Myanmar'
    },
    {
        'id': 2,
        'title':'GIS Officer',
        'country':'Thailand'
    },
    {
        'id': 3,
        'title':'Remote Sensing Specialist',
        'salary':'$ 1500000',
        'country':'Remote'
    },
        {
        'id': 4,
        'title':'Trainer',
        'salary':'$ 1300000',
        'country':'Califonia'
    }
]

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS, company='Futrue Perspective Myanmar')

@app.route('/api/jobs')
def job_list():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)