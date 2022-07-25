from PyQt6.QtCore import QSize, QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self, logic):
        super().__init__()

        # application attributes

        self.logic = logic

        # windows and timer

        self.setWindowTitle('Annoying words')
        self.settings = SettingsWindow(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.action_new_words)

        # define all layouts

        self.root = QWidget()
        self.vbox_root = QVBoxLayout()
        self.hbox_top = QHBoxLayout()
        self.hbox_buttons = QHBoxLayout()
        self.vbox_labels = QVBoxLayout()
        self.vbox_inputs = QVBoxLayout()

        # connect all layouts

        self.root.setLayout(self.vbox_root)
        self.vbox_root.addLayout(self.hbox_top)
        self.vbox_root.addLayout(self.hbox_buttons)
        self.hbox_top.addLayout(self.vbox_labels)
        self.hbox_top.addLayout(self.vbox_inputs)

        # word labels and inputs

        self.word_labels = []
        self.word_inputs = []

        for _ in range(self.logic.words_amount):
            word_label = QLabel()
            word_input = QLineEdit()
            word_input.setFixedSize(QSize(140, 40))

            self.word_labels.append(word_label)
            self.word_inputs.append(word_input)
            self.vbox_labels.addWidget(word_label)
            self.vbox_inputs.addWidget(word_input)

        # verification button

        self.button_verify = QPushButton('Verify')
        self.button_verify.setFixedSize(QSize(100, 50))
        self.button_verify.clicked.connect(self.action_verify)
        self.hbox_buttons.addWidget(self.button_verify)

        # finalize

        self.setCentralWidget(self.root)

    def action_new_words(self):
        self.timer.stop()

        new_words = self.logic.new_words()

        for word_label, word_input, word in zip(self.word_labels, self.word_inputs, new_words):
            native = word[0]
            foreign = word[1]

            word_label.setText(native)
            word_input.clear()

        self.show()

    def action_verify(self):
        # TODO verify words
        #  - correct: activate HIDE button and set new timer
        #  - wrong:   notify which words are incorrect

        if self.logic.verify():
            pass
        else:
            pass

        self.timer.start(1000)

    def action_hide(self):
        self.hide()

    # event methods

    def closeEvent(self, event):
        if self.settings:
            self.settings.close()


class SettingsWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel('Settings Window')
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.main_window = main_window

        self.setWindowTitle('Annoying words settings')

