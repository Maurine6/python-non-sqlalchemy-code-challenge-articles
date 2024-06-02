class Article:
    def __init__(self,title):
        if not isinstance(title, str) or not (5<=len(title) <= 50):
            raise valueError("title must be a str")
        self.__title = name

       

    @property
    def title(self):
        return self.__title  


          