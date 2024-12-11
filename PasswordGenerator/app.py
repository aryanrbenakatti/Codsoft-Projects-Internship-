from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        length = int(request.form.get("length", 12))  # Default length is 12
        if length < 6:
            return jsonify({"error": "Password length must be at least 6."}), 400
        password = generate_password(length)
        return jsonify({"password": password})
    except ValueError:
        return jsonify({"error": "Invalid input. Length must be an integer."}), 400

if __name__ == "__main__":
    app.run(debug=True)
