# Author: Alex Brocklebank
# Date: 8/01/15
# Created with code from Udacity Course ud036
# https://www.udacity.com/course/programming-foundations-with-python--ud036-nd

import webbrowser

class Movie():
    # Using the __doc__ variable pulls up this comment as documentation.
    # Triple quotes allow strings to span lines.
    """This class provides a way to store movie related information"""

    # Class Variables predefined in python store classname and module.
    __name__ = "Movie"
    __module__ = "media"

    # Creating a constant class variable.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Class Constructor:
    def __init__(self, movie_title, year, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.year = year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Defined Class Function:
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
