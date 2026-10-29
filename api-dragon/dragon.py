#!/usr/bin/env python3
"""The API Dragon — slay the beast with Python."""

import json
import urllib.request

DRAGON_API = "https://jsonplaceholder.typicode.com/posts"


def slay():
    with urllib.request.urlopen(DRAGON_API, timeout=10) as r:
        posts = json.loads(r.read().decode("utf-8"))
    dragon = posts[len(posts) // 2]
    return {"dragon_name": dragon["title"], "quest": f"Slay dragon: {dragon['title']}"}


def main():
    print(json.dumps(slay(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
