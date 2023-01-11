import sys

from gui import Gui


class AnnoyingWords:
    def __init__(self, words_amount, db):
        self.words_amount = words_amount
        self.db = db
        self.gui = Gui(sys.argv, self)

    def run(self):
        self.gui.new_words()
        self.gui.main_loop()

    def new_words(self):
        # TODO put into separate method, so the class knows about
        #  the word relations in order to check correctnes
        for new_word in self.db.get_new_words(self.words_amount):
            pass

    def verify(self):
        return True

