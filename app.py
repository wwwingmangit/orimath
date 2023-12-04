from flask import Flask, render_template, request
from datetime import datetime
import sqlite3

from math_generator import generate_math_problem
from submission_handler import process_submission

import sqlite3

app = Flask(__name__)

# Global settings
DEFAULT_NUMBER_OF_PROBLEMS = 5
DEFAULT_LOW_RANGE = 1
DEFAULT_HIGH_RANGE = 10
DEFAULT_OPERATION = "+"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test():
    problems = []
    operation = DEFAULT_OPERATION
    low_range = DEFAULT_LOW_RANGE
    high_range = DEFAULT_HIGH_RANGE
    nb_problems = DEFAULT_NUMBER_OF_PROBLEMS

    for _ in range(nb_problems):
        problem, answer, operand1, operand2 = generate_math_problem(
            operation, low_range, high_range
        )
        problems.append(
            {
                "problem": problem,
                "answer": answer,
                "operand1": operand1,
                "operand2": operand2,
            }
        )

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

    operation = DEFAULT_OPERATION
    low_range = DEFAULT_LOW_RANGE
    high_range = DEFAULT_HIGH_RANGE
    nb_problems = DEFAULT_NUMBER_OF_PROBLEMS

    # Connect to the database
    connection = sqlite3.connect("math_tests.db")
    cursor = connection.cursor()

    # Insert test details and get test_id
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO tests (datetime, operation, low_range, high_range) VALUES (?, ?, ?, ?)",
        (current_time, DEFAULT_OPERATION, DEFAULT_LOW_RANGE, DEFAULT_HIGH_RANGE),
    )
    test_id = cursor.lastrowid

    # Call process_submission with the test_id
    feedback, score = process_submission(user_answers, problems, test_id)

    # Close the database connection
    connection.close()

    return render_template("results.html", feedback=feedback, score=score)


if __name__ == "__main__":
    app.run(debug=True)
