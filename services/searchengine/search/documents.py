from collections import Counter
from dataclasses import dataclass

from .analysis import analyze

@dataclass
class Answer:
    """Answer document"""
    ID: int
    category: str
    text: str
    keywords: str

    @property
    def fulltext(self):
        return ' '.join(self.keywords)

    def analyze(self):
        self.term_frequencies = Counter(analyze(self.keywords + " " + self.text))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)