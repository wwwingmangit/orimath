import sqlite3
from datetime import datetime


def process_submission(user_answers, problems, test_id):
    feedback = []
    correct_count = 0

    # Connect to SQLite database
    connection = sqlite3.connect("math_tests.db")
    cursor = connection.cursor()

    # Process and store each problem's result
    for i, problem in enumerate(problems, start=1):
        user_answer = user_answers.get(f"answer_{i}")
        correct_answer = problem["answer"]
        is_correct = user_answer and float(user_answer) == correct_answer

        if is_correct:
            correct_count += 1
            feedback.append(f"{problem['problem']}: Correct!")
        else:
            feedback.append(
                f"{problem['problem']}: Incorrect. Correct answer was {correct_answer}."
            )

        # Insert problem result into the database
        cursor.execute(
            "INSERT INTO results (test_id, problem, user_answer, correct_answer, is_correct) VALUES (?, ?, ?, ?, ?)",
            (test_id, problem["problem"], user_answer, correct_answer, is_correct),
        )

    connection.commit()
    connection.close()

    score = (correct_count / len(problems)) * 100
    return feedback, score
