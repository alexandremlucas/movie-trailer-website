import webbrowser

"""
This class intends to handle the movie object
At this moment, it only has a constructor setter
"""


class Movie():
    def __init__(self, title, story_line, poster_image_url, youtube_url):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = youtube_url
