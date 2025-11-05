import sys
from typing import Literal

if sys.version_info < (3, 15):
    from typing_extensions import TypedDict
else:
    from typing import TypedDict

SERVER = "https://api.feedbin.com"

type EntryID = int
type FeedID = int

# Authentication: https://github.com/feedbin/feedbin-api/blob/master/content/authentication.md
AUTHENTICATION_URL = f"{SERVER}/v2/authentication.json"


# Entries: https://github.com/feedbin/feedbin-api/blob/master/content/entries.md
ENTRIES_URL = f"{SERVER}/v2/entries.json"


class EntriesParams(TypedDict, total=False, closed=True):
    page: int
    since: str
    ids: list[EntryID]
    read: bool
    starred: bool
    per_page: int
    mode: Literal["extended"]
    include_original: bool
    include_enclosure: bool
    include_content_diff: bool


class EntriesResponse(TypedDict, closed=True):
    id: EntryID
    feed_id: FeedID
    title: str | None
    url: str
    extracted_content_url: str
    author: str | None
    content: str | None
    summary: str
    published: str
    created_at: str


# Unread Entries: https://github.com/feedbin/feedbin-api/blob/master/content/unread-entries.md
# Feedbin allows for a DELETE to the normal entries endpoint, but httpx doesn't like
# sending a body with DELETE requests, so we are using the alternate endpoint dedicated
# to marking entries as read.
UNREAD_ENTRIES_DELETE_URL = f"{SERVER}/v2/unread_entries/delete.json"


class UnreadEntriesBody(TypedDict, closed=True):
    unread_entries: list[EntryID]
