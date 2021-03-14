from mongoengine import *

from download import *
from upload import *
from edit import *


class VideoTemplate(Document):
    """Video Template
    Stores information needed to create a video from the template
    """

    # Default values
    title = StringField(required=True, unique=True)
    working = BooleanField(default=False)
    completed = BooleanField(default=False)

    def __init__(self,
                 downloader: Download = None,
                 uploader: Upload = None,
                 editor: Edit = None)