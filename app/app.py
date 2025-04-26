from flask import Flask
import os 

app = Flask(__name__)

@app.route("/")
def home():
    
    return "Testeando la actividad 3"

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)