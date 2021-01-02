import settings
from handler import *


def main():
    try:
        log("Starting...")
        handler = Handler(
            settings.username,
            settings.password,
            settings.content_id,
            settings.author_id,
            settings.words_blacklist,
            settings.users_blacklist,
            settings.users_whitelist
        )
        log("Working..")

        while True:
            time.sleep(5)
            handler.parse_comments()
    except (KeyboardInterrupt, SystemExit):
        log("Shutting down")


if __name__ == "__main__":
    main()
