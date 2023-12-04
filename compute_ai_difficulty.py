import sqlite3
import pandas as pd


def extract_data_from_db(db_path):
    # Establish a connection to the database
    conn = sqlite3.connect(db_path)

    # Query to select relevant data
    query = """
    SELECT problem, user_answer, correct_answer, is_correct, 
           operation, low_range, high_range 
    FROM results
    JOIN tests ON results.test_id = tests.id
    """

    # Load the data into a pandas DataFrame
    data = pd.read_sql_query(query, conn)

    # Close the connection
    conn.close()

    return data


def main():
    # Path to your SQLite database
    db_path = "math_tests.db"

    # Extract data
    data = extract_data_from_db(db_path)

    # Print the data for testing
    print(data.head())  # Prints the first few rows of the DataFrame


if __name__ == "__main__":
    main()
