import math
import itertools
import numpy as np

import lib.category_mapping
from .timing import timing
from .analysis import analyze


class Index:
    def __init__(self):
        self.index = {}
        self.documents = {}

    def index_document(self, document):
        if document.ID not in self.documents:
            self.documents[document.ID] = document
            document.analyze()

        for token in analyze(document.keywords + " " + document.text):
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(document.ID)

    def document_frequency(self, token):
        return len(self.index.get(token, set()))

    def inverse_document_frequency(self, token):
        doc_freq = self.document_frequency(token)
        if doc_freq != 0:
            return math.log10(len(self.documents) / doc_freq)
        return 0

    def _results(self, analyzed_query):
        return [self.index.get(token, set()) for token in analyzed_query]

    def search(self, query, category, search_type='AND', rank=False):
        """
        Search; this will return documents that contain words from the query,
        and rank them if requested (sets are fast, but unordered).

        Parameters:
          - query: the query string
          - search_type: ('AND', 'OR') do all query terms have to match, or just one
          - score: (True, False) if True, rank results based on TF-IDF score
        """

        category_text = lib.category_mapping.map_category_to_string(category)

        if search_type not in ('AND', 'OR'):
            return []

        analyzed_query = analyze(query)
        results = self._results(analyzed_query)

        if len(results) == 0:
            return []

        documents = []
        if search_type == 'AND':
            for doc_id in set.intersection(*results):
                doc = self.documents[doc_id]
                if doc.category == category_text:
                    documents.append(doc)

        if search_type == 'OR':
            for doc_id in set.union(*results):
                doc = self.documents[doc_id]
                if doc.category == category_text:
                    documents.append(doc)

        if rank:
            return self.rank(analyzed_query, documents)
        return documents

    def rank(self, analyzed_query, documents):
        results = []
        if not documents:
            return results
        for document in documents:
            score = 0.0
            for token in analyzed_query:
                tf = document.term_frequency(token)
                idf = self.inverse_document_frequency(token)
                score += tf * idf
            results.append((document, score))
        return sorted(results, key=lambda doc: doc[1], reverse=True)
