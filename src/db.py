import random


class Database:
    def __init__(self):
        # TODO separate to JSON file
        self.words = [
            # nominative
            ('I', 'jeg'),
            ('you (s. nom.)', 'du'),
            ('he', 'han'),
            ('she', 'hun'),
            ('we', 'vi'),
            ('you (p. nom.)', 'i'),
            ('they', 'de'),
            # accusative
            ('me', 'mig'),
            ('you (s. acc.)', 'dig'),
            ('him', 'ham'),
            ('her', 'hende'),
            ('us', 'os'),
            ('you (s. acc.)', 'jer'),
            ('them', 'dem'),
        ]

    def get_new_words(self, amount):
        return random.sample(self.words, amount)

