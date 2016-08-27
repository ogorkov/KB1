import unittest
import sqlite3

import basis.kbRequirement

class addTagTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_addTag(self):
        """It is possible to add a tag"""
        a = basis.kbRequirement.kbRequirement()
        a.addTag("asdf")
        self.assertEquals(a.tags, ["asdf"])

    def test_addDuplicatedTag(self):
        """Equal tags should not be duplicated"""
        a = basis.kbRequirement.kbRequirement()
        a.addTag("asdf")
        a.addTag("asdf")
        self.assertEquals(a.tags, ["asdf"])

    def test_addDuplicatedTagAnotherCase(self):
        """Tags 'asdf' and 'AsDf' should be equal"""
        a = basis.kbRequirement.kbRequirement()
        a.addTag("asdf")
        a.addTag("aSDf")
        self.assertEquals(a.tags, ["asdf"])

    def test_severalTagsAdded(self):
        """More than one tag could be created"""
        a = basis.kbRequirement.kbRequirement()
        a.addTag("asdf")
        a.addTag("a77d")
        self.assertEquals(a.tags, ["asdf", "a77d"])

    def test_addDuplicatedTagStringInteger(self):
        """
        Tags could be both integer and string
        So they should not be duplicated
        """
        a = basis.kbRequirement.kbRequirement()
        a.addTag("7")
        a.addTag(7)
        self.assertEquals(a.tags, ["7"])


con = sqlite3.connect("test.dba")
cur = con.cursor()
# cur.execute('CREATE TABLE requirements (reqId INTEGER PRIMARY KEY, title VARCHAR(100), description VARCHAR(30))')
cur.execute('INSERT INTO requirements VALUES (1, "title","lalalala"), (2, "title2", "ne nado lala")')

class descriptionTests(unittest.TestCase):
    def test_loadDescription(self):
        cur.execute('SELECT description FROM requirements WHERE reqId = 1')

        a = basis.kbRequirement.kbRequirement()
        a.description = cur.fetchone()[0]
        var = "lalalala"
        self.assertEquals(a.description, var)

    def test_loadDescription2(self):
        cur.execute('SELECT description FROM requirements WHERE reqId = 2')

        a = basis.kbRequirement.kbRequirement()
        a.description = cur.fetchone()[0]
        var = "ne nado lala"
        self.assertEquals(a.description, var)

    def test_rollbackDescription(self):


if __name__ == '__main__':

    unittest.main()
