import media
import fresh_tomatoes

"""
This module aims to populate the movie data and call the page
rendering (fresh_tomatoes)
"""

# Instantiates Movie class passing some params.
xmen = media.Movie("X-Men: Dark Phoenix",
                   "The X-Men is a superheroes Movie",
                   "https://upload.wikimedia.org/wikipedia/en/a/a4/"
                   "Dark_Phoenix_poster.jpg",
                   "https://www.youtube.com/watch?v=whbar1UW1cs")

creed2 = media.Movie("Creed II",
                     "Creed II American sports drama film directed by"
                     "Steven Caple Jr",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/e/e6/"
                     "Creed_ii_poster.jpg/220px-Creed_ii_poster.jpg",
                     "https://www.youtube.com/watch?v=ApQbQ0iJQO0")

mid90s = media.Movie("Mid90s",
                     "Mid90s is a American comedy-drama film written and "
                     "directed by Jonah Hill",
                     "https://upload.wikimedia.org/wikipedia/en/4/4d/"
                     "Mid90s.png",
                     "https://www.youtube.com/watch?v=j4-B6-rDmiw")

# Creates a list of the movie instance
movies = [xmen, creed2, mid90s]

# Finally, calls method which renders the page
fresh_tomatoes.open_movies_page(movies)
