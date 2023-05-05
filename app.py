from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from main import make_changes_and_push

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form['input_text']
    try:
        make_changes_and_push(input_text)
        return jsonify({"status": "success", "message": "HTML content generated and pushed to GitHub successfully!"})
    except Exception as e:
        print(e)
        return jsonify({"status": "error", "message": "An error occurred. Please try again."})

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form["input_text"]
        make_changes_and_push(input_text)
        return redirect(url_for("success"))
    return render_template("index.html")

@app.route("/success")
def success():
    return "HTML content generated and pushed to GitHub successfully! "

if __name__ == "__main__":
    app.run(debug=True)
