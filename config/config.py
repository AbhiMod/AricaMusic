#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# All rights reserved. © Alisha © Alexa © Yukki


import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "12227067"))
API_HASH = getenv("API_HASH","b463bedd791aa733ae2297e6520302fe")

BOT_TOKEN = getenv("BOT_TOKEN","5047622280:AAHsjd5cTs9v-rdjM8YumWQKtoZf_CQ5afs")
CHAT = getenv("CHAT","https://t.me/+jCS-YsVBVEE3NjQ1")
BOT_NAME = getenv("BOT_NAME","Erica X Yukki")
LOGS = getenv("LOGS","-1001717726836")
OWNER_USERNAME = getenv("OWNER_USERNAME","sultan11100")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Aman:Aman@cluster0.9ztuf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001971806089"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Erica X Yukki")

OWNER_ID = list(map(int, getenv("OWNER_ID", "2105971379 5360305806").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

BOT_ID = getenv("BOT_ID","5047622280")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AbhiMod/AricaMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL",None)
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+jCS-YsVBVEE3NjQ1")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", None)

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "7f92897a59464ddbbf00f06cd6bda7fc")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2a230af10e0a40638dc77c1febb47170")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "904857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "9073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQA1MvomBfT3u2-US_uDfmxKjftJnVRQvbH_kujBzC4KvVx-rv87LbsgGoSo7Lh0ihFOIlU94behbT2GxeXudxvWOaB8_8c0MHabfw76lLHtONpgVw0d3ELPoMZ915CXDiwUVvopRHiIJ2p6BGOtQIvrtpe4u440vP-2nkmYeggOBtxxi6XMj9wcbJ27N-2UBykM0YJGnm3wlBEaUnA6wV1mWEYOm4JRhhzY3zyFJCgeBfWLFvZLFjdyg6UUNkfHscsweM4NgivbKGEzeFsnEKheHWW21XjZ_v00lCpyoKVAMo7oWgD7g06ZnJdAzN74xqeUrUjeGD2qJvkPKE1kGtLIAAAAAWseAkMA")
STRING2 = getenv("STRING_SESSION2", "BQAWih4JNhg2twr2Vb99P1Es8BDTCOguzYeWW01qz9RTGFcQTaTqUwUFuB6BsQcKT1U-Mn1j3LzrzQPzCt6AhwzYMI5o_zRBVK1aaP7yFmMq7GEWbOBVwdV33rChka807TZzO48R4VunYO-A9xaAQffCGNU3WlzTZyXRbTNbCzD9GsWsrBqkla_P-mmxOTwRCMUi6tFE-QG2fpCf4sKUZsRfLAJ8SRWEbXfC0QIY-VfLAv9PexYvuInV5dr2J3j-4-_wr4aPkRnzaK7sS1YUqdN2tETecM9Aw-02hmuoTeqzXX0lHiJY_gj32Q7PZ0FjLO3M86Hf-47qL2LlaVTygGEFAAAAAYvNcHYA")
STRING3 = getenv("STRING_SESSION3","BQBTdnYZwNTNIOIOgWUjHOwtzShKxj_NXdP2aXstb_7vETATvaU21l1Ti2qJTjl6vPmBegm92-wyOmr8dnowuKHnZnLsc5DCCTuhi7ydGb3m-1LJdTAEn0X4FoOMD3cEPgj6Pmc3LvSmxle8ZI7tmGh6-l5VXDvrL3wfoBGieqmCbTCGNPMV31YTW4J7Nz08cRJ5PKECHc6C8WeplMh0gSDaDdHi3kXU1A4x1VNn8qz2qzfqPgqFbCeS-teIlDNAu1umH-c0fxc7C05h30II5Znm2YSOjZ_CvBXhVNIvZlzsJyLeNq8U0Ce5fAeBUF3UaZtqlavhyyUWGkwT7WmGBEsTAAAAAYUBeawA")
STRING4 = getenv("STRING_SESSION4",None)
STRING5 = getenv("STRING_SESSION5",None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/93e8bfd8032b6b583b65b.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL","https://graph.org/file/93e8bfd8032b6b583b65b.jpg")

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL","https://graph.org/file/93e8bfd8032b6b583b65b.jpg")

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL","https://graph.org/file/93e8bfd8032b6b583b65b.jpg")

STATS_IMG_URL = getenv(
    "STATS_IMG_URL","https://graph.org/file/93e8bfd8032b6b583b65b.jpg")

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL","https://graph.org/file/f59d6fbce5a71a6fc1bba.jpg")

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL","https://graph.org/file/f59d6fbce5a71a6fc1bba.jpg")

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL","https://graph.org/file/f59d6fbce5a71a6fc1bba.jpg")

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL","https://graph.org/file/f59d6fbce5a71a6fc1bba.jpg")

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL","https://graph.org/file/f59d6fbce5a71a6fc1bba.jpg")

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL","https://graph.org/file/f59d6fbce5a71a6fc1bba.jpg")
SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL","https://graph.org/file/f59d6fbce5a71a6fc1bba.jpg")

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL","https://graph.org/file/f59d6fbce5a71a6fc1bba.jpg")


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )


if PING_IMG_URL:
    if PING_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
