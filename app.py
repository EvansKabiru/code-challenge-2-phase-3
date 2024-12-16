from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create an author (insert into authors table)
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid  # Get the id of the newly created author

    # Create a magazine (insert into magazines table)
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid  # Get the id of the newly created magazine

    # Create an article (insert into articles table)
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)', 
                   (article_title, article_content, author_id, magazine_id))
    conn.commit()

    # Query the database for inserted records (JOIN articles, authors, and magazines)
    cursor.execute('''
        SELECT articles.id, articles.title, articles.content, authors.name AS author_name, magazines.name AS magazine_name, magazines.category AS magazine_category
        FROM articles
        JOIN authors ON articles.author_id = authors.id
        JOIN magazines ON articles.magazine_id = magazines.id
    ''')
    articles_data = cursor.fetchall()

    conn.close()

    # Display results using model classes
    print("\nArticles:")
    for article_data in articles_data:
        # Instantiate models with data from the database query
        author = Author(article_data["author_name"])
        magazine = Magazine(article_data["magazine_name"], article_data["magazine_category"])
        article = Article(article_data["id"], article_data["title"], article_data["content"], author, magazine)

        # Print the article details
        print(f"Article ID: {article.id}")
        print(f"Title: {article.title}")
        print(f"Content: {article.content}")
        print(f"Author: {author.name}")
        print(f"Magazine: {magazine.name}, Category: {magazine.category}")
        print("-----")

if __name__ == "__main__":
    main()
