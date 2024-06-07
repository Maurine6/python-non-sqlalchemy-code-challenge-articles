class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a string and not empty.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        #magazines.add_article(article)
        return article
    
    def topic_areas(self):
        areas = set()
        for article in self._articles:
            areas.add(article.magazine.category)
        return list(areas) if areas else None

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)
       
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def add_articles(self, article):
        self._articles.append(article)    

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def contributing_authors(self):
        if not self._articles:
            return None
        
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        
        return [author for author, x in author_counts.items() if x > 2]
        
    def article_titles(self):
        return [article.title for article in self.articles()]

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return cls.all_magazines    

class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of the Author class.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class.")
        self._magazine = value
