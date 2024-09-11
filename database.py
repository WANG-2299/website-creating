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