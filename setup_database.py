import sqlite3


def create_database():
    connection = sqlite3.connect("math_tests.db")
    cursor = connection.cursor()

    # Create Tests table
    cursor.execute(
        """CREATE TABLE tests (
                        id INTEGER PRIMARY KEY,
                        datetime TEXT,
                        operation TEXT,
                        operand1 INTEGER, 
                        operand2 INTEGER, 
                        low_range INTEGER,
                        high_range INTEGER)"""
    )

    # Create Results table
    cursor.execute(
        """CREATE TABLE results (
                        id INTEGER PRIMARY KEY,
                        test_id INTEGER,
                        problem TEXT,
                        user_answer TEXT,
                        correct_answer TEXT,
                        is_correct BOOLEAN,
                        FOREIGN KEY (test_id) REFERENCES tests (id))"""
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
