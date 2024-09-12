from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
app = Flask(__name__)

'''
JOBS = [
  {
    'id':1, 
   'title':'Data Analyst', 
   'location':'Bengaluru, India', 
   'salary':'Rs. 10,00,000'
  },
  {'id':2, 
   'title':'Data Scientist', 
   'location':'Delhi, India', },
  {'id':3, 
   'title':'Frontend Engineer', 
   'location':'remote', 
   'salary':'Rs. 15,00,000'},
  {'id':4, 
   'title':'Backend Engineer', 
   'location':'San Francisco, USA', 
   'salary':'$120,000'}
]
'''

@app.route("/") #homepage
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                         jobs=jobs,
                        company_name='WEIWEI')

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404 
  return render_template('jobpage.html',job=job)

@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  # data = request.args
  # return jsonify(data)
  return render_template('application_submitted.html', 
                         application=data, job=job)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True) #debug=true to see errors and see changes