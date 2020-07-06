import sqlite3


class Ctrla:
    def __init__(self):
        pass

    @classmethod
    def run_query(cls, query):
        conn = sqlite3.connect("lynchWatch_data.db")
        conn.execute(query)
        conn.commit()
        conn.close()

    def run_read_query(self, query):
        pass

    def run_search_query(self, query):
        pass

    def add_story(self, new_story):
        sql = "INSERT INTO stories (headline, date_published, source, author, url) VALUES ('%s', '%s', '%s', '%s', " \
              "'%s')" % (
                  new_story.headline, new_story.date_published, new_story.source, new_story.author, new_story.url)
        self.run_query(sql)

    def del_story(self, story_id):
        sql = "DELETE FROM stories WHERE story_id = '%d'" % story_id
        self.run_query(sql)

    def view_stories(self):
        sql = "SELECT * FROM stories"
        self.run_read_query(sql)
