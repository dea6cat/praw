"""Provide the Front class."""
from .mixins import SubredditListingMixin


class Front(SubredditListingMixin):
    """Front is a Listing class that represents the front page."""

    def __init__(self, reddit):
        """Initialize a Front instance."""
        super(Front, self).__init__(reddit)
        self._path = '/'
