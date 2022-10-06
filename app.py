#imports nd stuff
from flask import Flask
import os

app = Flask(__name__)

#Function "hello" that returs "Flask inside docker!!"

@app.route("/")
def hello():
    return "Flask inside Docker!!"

#Binding to port 5000 nd running app which just happens to be flask

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)


    
