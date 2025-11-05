import collections

import feedbin


def duplicates(unread_entries: list[feedbin.EntriesResponse]) -> set[feedbin.EntryID]:
    duplicates: set[feedbin.EntryID] = set()

    print("Total unread entries:", len(unread_entries))
    # Short-circuit if there are no unread entries.
    if not unread_entries:
        return duplicates

    # Figure out which feeds have the fewest unread entries.
    feed_entry_count: dict[feedbin.FeedID, int] = collections.defaultdict(int)
    for entry in unread_entries:
        feed_entry_count[entry["feed_id"]] += 1
    print("Feeds w/ unread entries:", len(feed_entry_count))

    # Sort the unread entries by feed ID unread count.
    # This allows for the feeds with the fewest unread items to keep the single
    # copy of the entry for easier reading.
    unread_entries.sort(key=lambda entry: feed_entry_count[entry["feed_id"]])

    # Find the duplicate unread entries.
    seen_entries: set[str] = set()
    for entry in unread_entries:
        if entry["url"] not in seen_entries:
            seen_entries.add(entry["url"])
        else:
            duplicates.add(entry["id"])
    print("Duplicate unread entries:", len(duplicates))
    return duplicates
