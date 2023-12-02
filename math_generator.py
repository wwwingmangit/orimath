import random


def generate_math_problem(operation, low, high):
    if low <= 0 or high <= 0 or high < low:
        raise ValueError(
            "Internal Error in generate_math_problem. Low and High of Range must be 0<Low<=High"
        )

    # Randomly select two numbers within the given range
    num1 = random.randint(low, high)
    num2 = random.randint(low, high)

    # Generate the problem and calculate the answer
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = num1 / num2
    else:
        raise ValueError("Internal Error in generate_math_problem. Invalid operation.")

    problem = f"{num1} {operation} {num2}"
    return problem, answer
