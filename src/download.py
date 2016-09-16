import urllib.request
import os
from html.parser import HTMLParser

class Link:
    def __init__(self, href, baseurl):
        self.href = href
        self.name = ""
        self.baseurl = baseurl

    def url(self):
        return self.baseurl + "/" + self.href

    def download(self):
        trash, ext = os.path.splitext(self.href)
        if ext != ".xls":
            return

        fn = self.name.replace(" ", "-").lower()
        urllib.request.urlretrieve(self.url(), fn + ext)


class LinkParser(HTMLParser):
    def __init__(self, baseurl):
      HTMLParser.__init__(self)
      self.baseurl = baseurl
      self.data = []
      self.recording = False

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.data.append(Link(attrs[0][1], self.baseurl))
            self.recording = True

    def handle_data(self, data):
        if self.recording:
            self.data[-1].name = data
            self.recording = False

url = "http://www.tessellation.com/david_fish"
req = urllib.request.urlopen("http://www.tessellation.com/david_fish")
parser = LinkParser(url)
parser.feed(str(req.read()))

for link in parser.data:
    print("downloading " + link.url())
    link.download()
# print(req.read())
# urllib.request.urlretrieve("http://www.tessellation.com/david_fish/140930.xls", "test.xls")


