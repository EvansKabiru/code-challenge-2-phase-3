from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # Ensure that the name can be updated
        if len(new_name) >= 2 and len(new_name) <= 16:
            self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if new_category:
            self._category = new_category

    def articles(self):
        # SQL JOIN to get all articles in this magazine
        cursor = get_db_connection().cursor()
        cursor.execute('''
            SELECT articles.title FROM articles
            JOIN magazines ON magazines.id = articles.magazine_id
            WHERE magazines.id = ?
        ''', (self.id,))
        result = cursor.fetchall()
        return [article['title'] for article in result]

    def contributors(self):
        # SQL JOIN to get all authors who contributed to this magazine
        cursor = get_db_connection().cursor()
        cursor.execute('''
            SELECT authors.name FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        ''', (self.id,))
        result = cursor.fetchall()
        return [author['name'] for author in result]

    def article_titles(self):
        # SQL JOIN to get titles of all articles in this magazine
        cursor = get_db_connection().cursor()
        cursor.execute('''
            SELECT articles.title FROM articles
            JOIN magazines ON magazines.id = articles.magazine_id
            WHERE magazines.id = ?
        ''', (self.id,))
        result = cursor.fetchall()
        return [article['title'] for article in result] if result else None

    def contributing_authors(self):
        # SQL JOIN to get authors who have written more than 2 articles for this magazine
        cursor = get_db_connection().cursor()
        cursor.execute('''
            SELECT authors.name FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING COUNT(articles.id) > 2
        ''', (self.id,))
        result = cursor.fetchall()
        return [author['name'] for author in result] if result else None
