import os
import re
import subprocess
import sys
import time
from abc import abstractmethod


class Bookmarks:

    parent = "* Inbox\n"
    heading_lvl = "*" * (parent.count("*") + 1)
    time_format = ":PROPERTIES:\n:CREATED:  [%Y-%m-%d %a %H:%M]\n:END:"
    entry = heading_lvl + " [[{url}][{title}]]    {tags}\n{time}\n{content}"
    emacs_bin = "/usr/bin/emacs"

    def __init__(self, org_file):
        self.org_file = org_file
        with open(org_file, "rt") as f:
            self.lines = list(f)
        self.ins_point = self.lines.index(self.parent) + 1
        self.new_bookmarks = []

    def add_bookmark(self, url, title, tags=None, content=""):
        for line in self.lines:
            if url in line:
                self.show_message("Bookmark already added")
                return None
        tags_str = ":" + ":".join(tags) + ":" if tags else ""
        self.new_bookmarks.append(self.entry.format(url=url, title=title,
                                                    tags=tags_str, time=time.strftime(self.time_format), content=content + "\n")
                                  )

    def write(self):
        if not self.new_bookmarks:
            return None
        for b in self.new_bookmarks:
            self.lines.insert(self.ins_point, b)
        with open(self.org_file, "w") as f:
            for l in self.lines:
                f.write(l)
        self.show_message("Bookmark added")
        process = subprocess.run([self.emacs_bin, self.org_file,
                                  "--batch",  "-f",
                                  "org-html-export-to-html", "--kill"],
                                 cwd=os.path.dirname(self.org_file))

    @abstractmethod
    def show_message(self, message):
        pass
