import webbrowser

class Movie():

    """
        This class provides a way to store movie-related information

        Bijan Marashi (bm6410@att.com)
        Most of the code is taken from the tutorials in Udacity

        Arguments:
            movie_title: A string for the title of the movie
            movie_tagline: A string for a brief tagline encapsulating the spirit of the movie
            poster_image: A link to an image, either online, or on the server
            trailer_youtube: A link to the movie trailer on youtube
    """

    
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]
    
    def __init__(self, movie_title, movie_tagline, poster_image, trailer_youtube):
        self.title = movie_title
        self.tagline = movie_tagline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    
    def show_trailer(self):
        #Opens a popup and runs the trailer for the film
        webbrowser.open(self.trailer_youtube_url)
