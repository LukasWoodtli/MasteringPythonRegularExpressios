import unittest

import re


class GroupingTests(unittest.TestCase):
    def test_group(self):
        self.assertIsNotNone(re.match(r"(\d-\w){2,3}", ur"1-a2-b"))

        self.assertIsNotNone(re.search(r"(ab)+c", ur"ababc"))
        self.assertIsNone(re.search(r"(ab)+c", ur"abbc"))

    def test_spain(self):
        self.assertIsNotNone(re.search(r"Espana|ol", "Espanol"))
        self.assertIsNotNone(re.search(r"Espana|ol", "Espana"))
        self.assertIsNotNone(re.search(r"Espana|ol", "ol")) # not as intended

        # cheracter classes
        self.assertIsNotNone(re.search(r"Espan[aol]", "Espanol"))
        self.assertIsNotNone(re.search(r"Espan[aol]", "Espana"))
        self.assertIsNotNone(re.search(r"Espan[aol]", "Espano")) # not as intended
        self.assertIsNotNone(re.search(r"Espan[aol]", "Espanl")) # not as intended
        self.assertIsNotNone(re.search(r"Espan[a|ol]", "Espanol"))
        self.assertIsNotNone(re.search(r"Espan[a|ol]", "Espana"))
        self.assertIsNotNone(re.search(r"Espan[a|ol]", "Espano")) # not as intended
        self.assertIsNotNone(re.search(r"Espan[a|ol]", "Espanl")) # not as intended

    def test_spain_grouping(self):
        self.assertIsNotNone(re.search(r"Espan(a|ol)", "Espana"))
        self.assertIsNotNone(re.search(r"Espan(a|ol)", "Espanol"))

        self.assertIsNone(re.search(r"Espan(a|ol)", "Espan"))
        self.assertIsNone(re.search(r"Espan(a|ol)", "Espano"))
        self.assertIsNone(re.search(r"Espan(a|ol)", "ol"))

    def test_capturing(self):
        pattern = re.compile(r"(\d+)-\w+")
        it = pattern.finditer(r"1-a\n20-baer\n34-afcr")

        match = it.next()
        self.assertEqual('1', match.group(1))

        match = it.next()
        self.assertEqual('20', match.group(1))

        match = it.next()
        self.assertEqual('34', match.group(1))


    def test_backreferences_1(self):
        pattern = re.compile(r"(\w+) \1")
        match = pattern.search(r"hello hello world")
        self.assertEqual(('hello',), match.groups())

    def test_backreferences_2(self):
        pattern = re.compile(r"(\d+)-(\w+)")
        self.assertEqual("a-1\nbear-20\nafcr-34",
                         pattern.sub(r"\2-\1", "1-a\n20-bear\n34-afcr"))

    def test_named_groups(self):
        pattern = re.compile(r"(?P<first>\w+) (?P<second>\w+)")
        match = pattern.search("Hello world")
        self.assertEqual("Hello", match.group("first"))
        self.assertEqual("world", match.group("second"))

if __name__ == '__main__':
    unittest.main()   # pragma: no cover