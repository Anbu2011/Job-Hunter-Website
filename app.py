from flask import Flask , render_template , jsonify

app = Flask(__name__) 

JOBS=[
  {
    "id":1,
    "title":"Data Analyst",
    "location":"Bengaluru , India",
    "salary":"Rs. 10,00,000"
  },
  {
    "id":2,
    "title":"Full Stack Developer",
    "location":"chennai , India",
    "salary":"Rs. 12,00,000"
  },
  {
    "id":3,
    "title":"Data Scientist",
    "location":"pune , India",
    "salary":"Rs. 15,00,000"
  },
  {
    "id":4,
    "title":"Frontend Engineer",
    "location":"Hyderabad , India",
    "salary":"Rs. 8,00,000"
  }
]

@app.route("/")            #url for html endpoint
def hello():                  
  return render_template("home.html",
                        jobs=JOBS,
                        company_name="Jovi")

@app.route("/api/jobs")
def list_jobs():         #url to return json file. just                             not like html... json endpoint
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  