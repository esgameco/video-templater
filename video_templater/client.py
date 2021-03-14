from mongoengine import *

from template import *


class Client():
    """Client for Mongoengine
    Processes database requests and creates videos from templates
    """

    def __init__(self, mongo_uri: str) -> None:
        """Initializes mongoengine

        Parameters:

        mongo_uri: str
          The uri used to initialize mongoengine
        """
        connect(mongo_uri)
    
    def create_video(self, video: VideoTemplate):
        """Creates video from a template

        Parameters:

        video: VideoTemplate
          The video to be created
        """
        video.make()
        video.upload()