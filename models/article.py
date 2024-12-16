from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self._content = content  # Use a private variable for content
        self.author_id = author_id
        self.magazine_id = magazine_id
        
        # Set title only if it's not already set
        if not hasattr(self, '_title'):  
            self._title = title  # Set title during instantiation

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title  # Getter only, no setter to make it immutable

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

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
