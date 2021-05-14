"""Main module."""
from uplink import Consumer, get, post, Header, Path, Query, Body
from uplink.returns import json

__all__ = ["Notion"]


class Notion(Consumer):
    def __init__(self, api_token, base_url="https://api.notion.com/v1/"):
        super().__init__(base_url=base_url)
        self.session.headers["Authorization"] = "Bearer: {}".format(api_token)

    @json
    @get("databases")
    def get_user(
        self,
        *,
        notion_version: Header("Notion-Version"),
        start_cursor: Query("start_cursor") = None,
        page_size: Query("page_size") = None,
    ):
        """Retrieve all databases."""

    @json
    @get("databases/{database_id}")
    def get_database(self, database_id: Path, notion_version: Header("Notion-Version")):
        """Fetch a database by database_id"""

    @json
    @get("users")
    def get_users(self, *, notion_version: Header("Notion-Version")):
        """Retrieve all users."""

    @json
    @get("users/{user_id}")
    def get_user(
        self,
        *,
        user_id: Path,
        notion_version: Header("Notion-Version"),
        start_cursor: Query("start_cursor") = None,
        page_size: Query("page_size") = None,
    ):
        """Retrieve a user by user_id."""

    @json
    @get("pages/{page_id}")
    def get_page(self, *page_id: Path, notion_version: Header("Notion-Version")):
        """Retrieve a page by page_id"""

    @json
    @post("pages")
    def create_page(self, *, notion_version: Header("Notion-Version"), **page: Body):
        """Create a page"""
