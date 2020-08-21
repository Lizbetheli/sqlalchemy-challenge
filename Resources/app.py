# 1. Import Flask
from flask import Flask


# 2. Create an app
app = Flask(__name__)


# 3. Define static routes
@app.route("/")
def index():
    return "Hello, world!"


@app.route("/about")
def about():
    name = "Liz"
    location = "Unknown"

    return f"My name is {name}, and I live in {location}."


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
