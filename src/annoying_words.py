import sys

from gui import QApplication as GuiApp
from gui import MainWindow as Gui


class AnnoyingWords:
    def __init__(self, words_amount, db):
        self.words_amount = words_amount
        self.db = db

        self.app = GuiApp(sys.argv)
        self.gui = Gui(self)

    def run(self):
        self.gui.action_new_words()
        self.gui.show()
        self.app.exec()

    def new_words(self):
        # TODO cache generated words, so the class knows about
        #  the word relations in order to check correctnes
        return self.db.get_new_words(self.words_amount)

    def verify(self):
        return True

