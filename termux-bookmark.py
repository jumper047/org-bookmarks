#!/usr/bin/python3

import os
import sys

from org_bookmarks import Bookmarks

ORG_FILE = "/data/data/com.termux/files/home/storage/shared/OrgBookmarks/Bookmarks.org"


class TermuxBookmarks(Bookmarks):

    emacs_bin = "/data/data/com.termux/files/usr/bin/emacs"

    def show_message(self, message):
        pass

if __name__ == "__main__":
    bmarks = TermuxBookmarks(ORG_FILE)
    if len(sys.argv) > 3:
        tags = sys.argv[3:]
    else:
        tags = None
    bmarks.add_bookmark(sys.argv[1], sys.argv[2], tags)
    bmarks.write()
