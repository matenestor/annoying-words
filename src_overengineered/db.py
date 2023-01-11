import random


class Database:
    def __init__(self):
        # TODO separate to JSON file
        self.words = [
            # nominative
            ('I', 'jeg'),
            ('you', 'du'),
            ('he', 'han'),
            ('she', 'hun'),
            ('we', 'vi'),
            ('you', 'i'),
            ('they', 'de'),
            # axcusative
            ('me', 'mig'),
            ('you', 'dig'),
            ('him', 'ham'),
            ('her', 'hende'),
            ('us', 'os'),
            ('you', 'jer'),
            ('them', 'dem'),
        ]

    def get_new_words(self, amount):
        return random.sample(self.words, amount)

