import sqlite3
from datetime import datetime


def process_submission(
    user_answers, correct_answers, total_problems, operation, low_range, high_range
):
    feedback = []
    correct_count = 0
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Connect to SQLite database
    connection = sqlite3.connect("math_tests.db")
    cursor = connection.cursor()

    # Insert test details and get test_id
    cursor.execute(
        "INSERT INTO tests (datetime, operation, low_range, high_range) VALUES (?, ?, ?, ?)",
        (current_time, operation, low_range, high_range),
    )
    test_id = cursor.lastrowid

    # Process and store each problem's result
    for i in range(1, total_problems + 1):
        user_answer = user_answers.get(f"answer_{i}")
        correct_answer = correct_answers.get(f"correct_answer_{i}")
        is_correct = user_answer and float(user_answer) == correct_answer

        if is_correct:
            correct_count += 1
            feedback.append(f"Problem {i}: Correct!")
        else:
            feedback.append(
                f"Problem {i}: Incorrect. Correct answer was {correct_answer}."
            )

        # Insert problem result into the database
        cursor.execute(
            "INSERT INTO results (test_id, problem, user_answer, correct_answer, is_correct) VALUES (?, ?, ?, ?, ?)",
            (test_id, f"Problem {i}", user_answer, correct_answer, is_correct),
        )

    connection.commit()
    connection.close()

    score = (correct_count / total_problems) * 100
    return feedback, score
