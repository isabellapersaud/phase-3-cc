class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        self.add_review_to_movie()
        self.add_review_to_viewer()
        self.add_movie_to_viewer()
        self.add_viewer_to_movies()


    # rating property goes here!
    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        if rating == 0 < rating < 6:
            self.rating = rating
        else: 
            print("The rating must be bettween 1 and 5, inclusive.")

            raise Exception("The rating must be bettween 1 and 5, inclusive.")

    rating = property(get_rating, set_rating)
    # viewer property goes here!
    #not sure what im doing wrong here for the first deliverable of review property(viewer() and movie())
    def get_viewer(self):
        return self._viewer
    
    def set_viewer(self, viewer):
        from viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else: 
            print("Viewer is not an instance of class Viewer")

            raise Exception("Viewer is not an instance of class Viewer")
    viewer = property(get_viewer, set_viewer)

    # movie property goes here!
    def get_movie(self):
        return self._movie

    def set_movie(self, movie):
        from movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            print("Movie is not an instance of class Movie")

            raise Exception("Movie is not an instance of class Movie")

    movie = property(get_movie, set_movie)

    def add_review_to_movie(self):
        self._movie.reviews.append(self)

    def add_movie_to_viewer(self):
        if self._movie not in self._viewer.reviewed_movies:
            self._viewer.reviewed_movies.append(self._movie)

    def add_review_to_viewer(self):
        self._viewer.reviews.append(self)

    def add_movie_to_viewer(self):
        if self._viewer not in self._movie.reviewers:
            self._movie.reviewers.append(self._viewer)

