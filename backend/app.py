# Flask backend for CloudScan Oral AI

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "CloudScan Oral AI Backend Running"

if __name__ == '__main__':
    app.run(debug=True)
