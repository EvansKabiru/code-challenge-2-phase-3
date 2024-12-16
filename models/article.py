from database.connection import get_db_connection

class Article:
    def __init__(self, id, author_id, magazine_id, title):
        self._id = id
        self._author_id = author_id
        self._magazine_id = magazine_id
        self._title = title

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        if hasattr(self, "_title"):
            return self._title
        return None

    @property
    def author(self):
        # SQL JOIN to get the author of this article
        cursor = get_db_connection().cursor()
        cursor.execute('''
            SELECT authors.name FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.id = ?
        ''', (self.id,))
        result = cursor.fetchone()
        return result['name'] if result else None

    @property
    def magazine(self):
        # SQL JOIN to get the magazine of this article
        cursor = get_db_connection().cursor()
        cursor.execute('''
            SELECT magazines.name FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.id = ?
        ''', (self.id,))
        result = cursor.fetchone()
        return result['name'] if result else None
