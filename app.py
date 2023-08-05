from flask import Flask #flask - module and Flask - class inside the module & importing functionalities from flask
app = Flask(__name__) #creating obj and assigning Flask functionalities into app and __name__ - script invoked __main__. 
@app.route("/") #part of the url coming after the domain name

def hello():
  return "hellognugjrgr"
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  