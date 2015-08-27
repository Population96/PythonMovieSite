# Author: Alex Brocklebank
# Date: 7/24/15
# Created with code from Udacity Course ud036
# https://www.udacity.com/course/programming-foundations-with-python--ud036-nd

import media
import make_page

# Declaration of Movies Objects for site population:

departed = media.Movie("The Departed",
                       "2006",
                       "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
                       "https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
                       "https://www.youtube.com/watch?v=auYbpnEwBBg")

saints = media.Movie("The Boondock Saints",
                     "1999",
                     "Fraternal twins set out to rid Boston of the evil men operating there while being tracked down by an FBI agent.",
                     "https://upload.wikimedia.org/wikipedia/en/1/1b/The_Boondock_Saints_poster.jpeg",
                     "https://www.youtube.com/watch?v=ydXojYfCF3I")

hero6 = media.Movie("Big Hero 6",
                    "2014",
                    "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.",
                    "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                    "https://www.youtube.com/watch?v=z3biFxZIJOQ")

john_wick = media.Movie("John Wick",
                        "2014",
                        "An ex-hitman comes out of retirement to track down the gangsters that took everything from him.",
                        "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
                        "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")

matrix = media.Movie("The Matrix",
                     "1999",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8")

anchorman = media.Movie("Anchorman: The Legend of Ron Burgundy",
                        "2004",
                        "Ron Burgundy is San Diego's top rated newsman in the male-dominated broadcasting of the '70s, but that's all about to change for Ron and his cronies when an ambitious woman is hired as a new anchor.",
                        "https://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg",
                        "https://www.youtube.com/watch?v=NJQ4qEWm9lU")

# Creating an array of the Movie objects:

movies = [departed, saints, hero6, john_wick, matrix, anchorman]

# Pass Movie object array to page creator 'fresh_tomatoes'

make_page.open_movies_page(movies)
