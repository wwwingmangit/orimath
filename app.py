from flask import Flask, render_template
from math_generator import generate_math_problem

app = Flask(__name__)


@app.route("/")
def home():
    try:
        operation = "+"  # You can change this to any of the four operations
        low_range = 1
        high_range = 10
        problem, answer = generate_math_problem(operation, low_range, high_range)
        return render_template("home.html", problem=problem, answer=answer)
    except ValueError as e:
        return str(e)  # Or handle the error in a way that fits your application


if __name__ == "__main__":
    app.run(debug=True)
