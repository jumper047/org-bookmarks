#!/usr/bin/python3
import os
import sys

from org_bookmarks import Bookmarks

ORG_FILE = os.path.expanduser(
    "~/.config/qutebrowser/org-bookmarks/Bookmarks.org")


def qute_command(command):
    """send commands to qutebrowser"""
    with open(os.environ['QUTE_FIFO'], 'w') as fifo:
        fifo.write(command + '\n')
        fifo.flush


class QuteBookmarks(Bookmarks):

    def add_bookmark(self, tags):
        title = os.getenv("QUTE_TITLE")
        url = os.getenv("QUTE_URL")
        super().add_bookmark(url, title, tags)

    def show_message(self, message):
        qute_command("message-info \"{}\"".format(message))

if __name__ == "__main__":
    bmarks = QuteBookmarks(ORG_FILE)
    if len(sys.argv) > 1:
        tags = sys.argv[1:]
    else:
        tags = None
    bmarks.add_bookmark(tags)
    bmarks.write()
