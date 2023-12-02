def process_submission(user_answers, correct_answers, total_problems):
    feedback = []
    correct_count = 0

    for i in range(1, total_problems + 1):
        user_answer = user_answers.get(f"answer_{i}")
        correct_answer = correct_answers.get(f"correct_answer_{i}")

        if not user_answer:
            feedback.append(f"Problem {i}: No answer provided.")
            continue

        try:
            if float(user_answer) == correct_answer:
                feedback.append(f"Problem {i}: Correct!")
                correct_count += 1
            else:
                feedback.append(
                    f"Problem {i}: Incorrect. Correct answer was {correct_answer}."
                )
        except ValueError:
            feedback.append(f"Problem {i}: Invalid answer format.")

    score = (correct_count / total_problems) * 100
    return feedback, score
