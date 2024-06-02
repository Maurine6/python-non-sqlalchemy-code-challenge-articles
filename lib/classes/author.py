from article import Article

class Author:
    def __init__(self,name):
        if not isinstance(name, str) or len(name) == 0:
            raise valueError("name not empty")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name 

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_articles(self,magazine, title):
        article = Article(self, magazine,title)
        self._articles.append(article)
        magazine.add_articles(article)
        return article
        