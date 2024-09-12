import os
from sqlalchemy import create_engine, text

# print(sqlalchemy.__version__)
db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    # Use .mappings() to get rows as dictionaries
    jobs = [dict(row) for row in result.mappings().all()]
    # Output the result
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
      rows = result.mappings().all()  # rows is a list of rows
      if len(rows) == 0:
          return None
      else:
          return dict(rows[0])

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    conn.execute(query, 
                 {"job_id": job_id, "full_name":data['full_name'], "email":data['email'], "linkedin_url":data['linkedin_url'], "education":data['education'], "work_experience":data['work_experience'], "resume_url":data['resume_url']})
    conn.commit()
  
'''
  print("type(result): ", type(result))
  result_all = result.all()
  print("type(result.all()): ", type(result_all))
  #print("result.all(): ", result_all)
  first_result = result_all[0]
  print("type(first_result): ", type(first_result))

  first_result_dict = dict(first_result[0])
  print("type(first_result_dict): ", type(first_result_dict))
  print(first_result_dict)
'''