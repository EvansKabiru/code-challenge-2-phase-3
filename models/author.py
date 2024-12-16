from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        # Ensure the name is valid (non-empty)
        if not name or len(name) == 0:
            raise ValueError("Author name must be longer than 0 characters.")
        
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        if hasattr(self, "_name"):
            return self._name
        return None

    @name.setter
    def name(self, new_name):
        # Ensure the name cannot be changed and it must be longer than 0 characters
        if not new_name or len(new_name) == 0:
            raise ValueError("Author name must be longer than 0 characters.")
        if hasattr(self, '_name'):
            raise AttributeError("Author name cannot be changed after instantiation.")
        self._name = new_name

    def articles(self):
        # SQL JOIN to get all articles written by this author
        cursor = get_db_connection().cursor()
        cursor.execute('''
            SELECT articles.title FROM articles
            JOIN authors ON authors.id = articles.author_id
            WHERE authors.id = ?
        ''', (self.id,))
        result = cursor.fetchall()
        return [article['title'] for article in result]

    def magazines(self):
        # SQL JOIN to get all magazines this author has contributed to
        cursor = get_db_connection().cursor()
        cursor.execute('''
            SELECT magazines.name FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        ''', (self.id,))
        result = cursor.fetchall()
        return [magazine['name'] for magazine in result]
