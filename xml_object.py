class XmlObject:
    raw_string = ""

    year = ""
    title_terms = list()
    author_terms = list()
    other_terms = list()

    def __init__(self, raw_string):
        self.raw_string = raw_string
        self.year = ""
        self.title_terms = list()
        self.author_terms = list()
        self.other_terms = list()
