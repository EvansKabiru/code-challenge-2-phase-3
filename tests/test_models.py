import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        assert article.title == "Test Title"
        assert article.content == "Test Content"

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        assert magazine.name == "Tech Weekly"
        assert magazine.category == "Technology"

if __name__ == "__main__":
    unittest.main()
