

class kbRequirement(object):
    """
    Basic requirement class

    """
    def __init__(self):
        self.reqId = None
        self.tags = []

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

