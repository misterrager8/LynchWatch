class Story:
    def __init__(self, headline, date_published, source, author, url, story_id=None):
        self.headline = headline
        self.date_published = date_published
        self.source = source
        self.author = author
        self.url = url
        self.story_id = story_id
