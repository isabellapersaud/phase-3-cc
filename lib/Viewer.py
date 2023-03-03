class Viewer:
    
    def __init__(self, username):
        self.username = username
        self.reviews = []
        self.reviewed_movies = []

    # username property goes here!
    def get_username(self):
        return self._username
    
    def set_username(self, username):
        if type(username) is str and 6 <= len(username) < 17: 
            self._username = username
        else: 
            print("username must be a string and between 6 and 16 charachters")

            raise Exception("username  must be a string  and between 6 and 16 charachters")

    username = property(get_username, set_username)

    def reviewed_movie(self, movie):
        if movie in self.reviewed_movies:
            return True
        else:
            False

    def rate_movie(self, movie, rating):
        from review import Review 
        Review(self, movie,rating)

    def reviews(self):
        return self.reviews