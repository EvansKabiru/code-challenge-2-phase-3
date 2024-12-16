from .connection import get_db_connection

def create_tables():
    # Establish connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create authors table with id and name
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create magazines table with id, name, and category
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')

    # Create articles table with id, title, content, and foreign keys to authors and magazines
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER,
            magazine_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (id)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
