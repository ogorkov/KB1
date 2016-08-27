import sqlite3

class kbRequirement(object):
    """
    Basic requirement class

    """
    def __init__(self):
        self.reqId = 0
        self.tags = []
        self.description = ""
        self.__description = ""

    def loadRequirement(self, cur: sqlite3.Cursor, rid: int):
        cur.execute('SELECT description FROM requirements WHERE reqId = ?', str(rid))
        if rid > 0:
            self.reqId = rid
            self.description = str(cur.fetchone()[0])
            self.__description = self.description

    def rollback(self):
        self.description = self.__description

    def addTag(self, tag):
        """
        A method to add a new tag to the list of tags
        :param tag: a tag to be added
        :return: nothing is return
        """
        a = [x.upper() for x in self.tags]
        b = str(tag)
        if not a.__contains__(b.upper()):
            self.tags.append(tag)

