from flask import Flask, render_template, Response, request, redirect, url_for, jsonify
from flask import session, flash

app = Flask(__name__, template_folder="ugestor_template")

@app.route('/page1', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=8000, debug=True, threaded=True) #, host='0.0.0.0'