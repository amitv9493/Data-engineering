#!/usr/bin/env python3

import logging
import sys
import requests
from yt_config import config
import pprint


def fetch_playlist_items_page(google_api_key, youtube_paylist_id, page_token=None):
    response = requests.get(
        "https://www.googleapis.com/youtube/v3/playlistItems",
        params={
            "key": google_api_key,
            "playlistId": youtube_paylist_id,
            "part": "contentDetails",
            "pageToken": page_token,
        },
    )

    return response.json()


def fetch_video_page(google_api_key, video_id, page_token=None):
    response = requests.get(
        "https://www.googleapis.com/youtube/v3/videos",
        params={
            "key": google_api_key,
            "id": video_id,
            "part": "snippet,statistics",
            "pageToken": page_token,
        },
    )

    return response.json()


def fetch_playlist_items(google_api_key, youtube_paylist_id, page_token=None):
    payload = fetch_playlist_items_page(google_api_key, youtube_paylist_id, page_token)
    yield from payload["items"]
    next_page_token = payload.get("nextPageToken")

    if next_page_token:
        yield from fetch_playlist_items(
            google_api_key, youtube_paylist_id, page_token=next_page_token
        )


def fetch_video(google_api_key, video_id, page_token=None):
    payload = fetch_video_page(google_api_key, video_id, page_token)
    yield from payload["items"]
    next_page_token = payload.get("nextPageToken")

    if next_page_token:
        yield from fetch_video_page(
            google_api_key, video_id, page_token=next_page_token
        )


def main():
    google_api_key = config["google_api_key"]
    playlist_id = config["playlist_id"]

    logging.info("start")
    for item in fetch_playlist_items(google_api_key, playlist_id):
        video_id = item["contentDetails"]["videoId"]
        for video in fetch_video(google_api_key, video_id):
            logging.info(pprint.pformat(video))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())
