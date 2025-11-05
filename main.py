import asyncio
import os

import httpx

import dedupe
import feedbin


async def check_auth(client: httpx.AsyncClient) -> None:
    """Check authentication works, raising an exception if not."""
    response = await client.get(feedbin.AUTHENTICATION_URL)
    response.raise_for_status()


async def unread_entries(client: httpx.AsyncClient) -> list[feedbin.EntriesResponse]:
    params: feedbin.EntriesParams = {"read": False}
    response = await client.get(feedbin.ENTRIES_URL, params=params)
    return response.raise_for_status().json()


async def mark_entries_as_read(
    client: httpx.AsyncClient, entry_ids: list[feedbin.FeedID]
) -> None:
    body: feedbin.UnreadEntriesBody = {"unread_entries": entry_ids}
    response = await client.post(feedbin.UNREAD_ENTRIES_DELETE_URL, json=body)
    response.raise_for_status()


async def main(username: str, password: str) -> None:
    async with httpx.AsyncClient(auth=(username, password)) as client:
        # Make sure authentication works.
        if __debug__:
            await check_auth(client)
            print("Authentication successful")

        # Find the duplicates.
        all_unread_entries = await unread_entries(client)
        duplicates = dedupe.duplicates(all_unread_entries)

        # Mark the duplicate entries as read.
        await mark_entries_as_read(client, list(duplicates))


if __name__ == "__main__":
    username = os.getenv("FEEDBIN_USERNAME")
    password = os.getenv("FEEDBIN_PASSWORD")
    if not username or not password:
        raise RuntimeError("FEEDBIN_USERNAME and FEEDBIN_PASSWORD must be set")

    asyncio.run(main(username, password))
