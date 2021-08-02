"""Handle session management with the Notion SDK."""

import notion_client


class Session(object):
    """An active session with the Notion SDK."""

    def __init__(self, **kwargs):
        self.client = notion_client.Client(**kwargs)

    @property
    def databases(self):
        """Direct access to the databases API endpoint."""
        return self.client.databases

    @property
    def users(self):
        """Direct access to the users API endpoint."""
        return self.client.users

    @property
    def pages(self):
        """Direct access to the pages API endpoint."""
        return self.client.pages

    @property
    def blocks(self):
        """Direct access to the blocks API endpoint."""
        return self.client.blocks

    @property
    def search(self):
        """Direct access to the search API endpoint."""
        return self.client.search
