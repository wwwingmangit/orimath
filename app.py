from flask import Flask, render_template, request
from math_generator import generate_math_problem
from submission_handler import process_submission

app = Flask(__name__)

# Global variable for the number of problems
NUMBER_OF_PROBLEMS = 5


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test():
    problems = []
    operation = "+"  # Choose the operation
    low_range = 1
    high_range = 10

    for _ in range(NUMBER_OF_PROBLEMS):
        problem, answer = generate_math_problem(operation, low_range, high_range)
        problems.append((problem, answer))

    return render_template("test.html", problems=problems)


@app.route("/results")
def results():
    return render_template("results.html")


@app.route("/submit-answers", methods=["POST"])
def submit_answers():
    user_answers = {
        key: request.form[key]
        for key in request.form.keys()
        if key.startswith("answer_")
    }
    correct_answers = {
        key: float(request.form[key])
        for key in request.form.keys()
        if key.startswith("correct_answer_")
    }

    feedback, score = process_submission(
        user_answers, correct_answers, NUMBER_OF_PROBLEMS
    )
    return render_template("results.html", feedback=feedback, score=score)


if __name__ == "__main__":
    app.run(debug=True)
