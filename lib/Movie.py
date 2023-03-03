class Movie:

    def __init__(self, title):
        self.title = title

        self.reviews = []
        self.reviewers = []


    def get_title(self):
        return self._title 


    def set_title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            print("Movie title must be a string and must be greater than 0 characters")

            raise Exception ("Movie title must be a string and must be greater than 0 characters")



    title = property(get_title, set_title)

    # title property goes here!

    def average_rating(self):
        total = 0 

        for review in self.reviews:
            total += review

        average = total / len(self.reviews)

        return average 

    @classmethod
    def highest_rated(cls):
        pass