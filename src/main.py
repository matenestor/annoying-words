import sys

from annoying_words import AnnoyingWords
from db import Database


# TODO Config class?
WORDS_AMOUNT = 10


if __name__ == '__main__':
    try:
        words_amount = int(sys.argv[1])
    except Exception:
        words_amount = WORDS_AMOUNT

    app = AnnoyingWords(words_amount, Database())
    app.run()

