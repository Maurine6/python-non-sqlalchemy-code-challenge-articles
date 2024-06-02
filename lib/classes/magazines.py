class Magazine:
    all_magazines = []
    def __init__(self,name, category):
        if not isinstance(name, str) or not (2<=len(name) <= 16):
            raise valueError("name must be a str")
        self.name = name

        if not isinstance(category, str) or len(category) == 0:
            raise valueError("categor not empty")
        self._category = category

    @property
    def name(self):
        return self.__name  

    @property
    def category(self):
        return self._category 

    def add_articles(self,article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author forarticle in self._articles })

    def contributing_authors(self):
        if not self._articles
        return None  
        count = {}
        for article in self._articles:
            count[article.author] = count.get(article.author,0) + 1 
            return [author for author, x in count.items() if x > 2]        

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return cls._all_magazines            