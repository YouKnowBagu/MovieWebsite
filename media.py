import webbrowser

class Movie():
    """Builds the structure for movie data in order to create the movie object"""
    def __init__(self,movie_title,movie_storyline,poster_image,youtube_trailer,release_date):
        """Inputs are data points for the specific movie you are creating using the class"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        self.release_date = release_date