"""Defines the Talk class that contains the details of a TEDx talk."""
import webbrowser

class Talk(object):
    """This class provides a way to store TEDx talk related information.

    Attributes:
        title: A string to store the title of the talk.
        summary: A string to store the main idea of the talk.

        
        poster_image_url: A string to store the URL of the talk thumbnail.
        talk_youtube_url: A string to store the URL of the TEDx talk video.
        publish_date: A string to store the publish date of the talk.
    """

    def __init__(self, talk_title, talk_summary, poster_image,
                 talk_youtube, talk_publish_date):
        """Initialises Talk class instance variables."""
        self.title = talk_title
        self.summary = talk_summary
        self.poster_image_url = poster_image
        self.talk_youtube_url = talk_youtube
        self.publish_date = talk_publish_date

    def play_talk(self):
        """Opens the TEDx talk video in the web browser."""
        webbrowser.open(self.talk_youtube_url)