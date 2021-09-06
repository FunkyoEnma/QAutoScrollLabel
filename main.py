# importing libraries
import sys
from time import sleep

from PyQt6.QtCore import Qt, QObject, pyqtSignal, QThread
from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QLabel, QScrollBar, QHBoxLayout, QApplication


class ScrollLabel(QScrollArea):

    def __init__(self, a0: str, parent: QWidget = None):
        """This is the widget where the text is going to be placed, if you wantd the AutoScroll Label use
        QAutoScrollLabel instead"""
        QScrollArea.__init__(self, parent)  # Initialize QScrollArea

        self.setWidgetResizable(True) # making widget resizable

        # making qwidget object to content the QLabel
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        self.__lay = QHBoxLayout(content)

        # creating label
        self.__label = QLabel(content)

        # adding label to the layout
        self.__lay.addWidget(self.__label)

        self.scrollbar = QScrollBar()

        self.setHorizontalScrollBar(self.scrollbar)

        self.setText(a0)

    def setText(self, a0: str):

        self.__label.setText(a0)

        self.__label.adjustSize()
        self.__lay.setContentsMargins(0, 0, 0, 0)
        print(self.__label.height())
        self.resize(200, self.__label.height() + 4)


class QAutoScrollLabel(ScrollLabel):

    # noinspection PyShadowingNames
    def __init__(self, parent: QWidget=None):

        text = "Este label se mueve automaticamente si es mas grande el texto"

        super(QAutoScrollLabel, self).__init__(text, parent)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.__debug = False

    class Worker(QObject):
        finished = pyqtSignal()
        progress = pyqtSignal(int)

        def __init__(self, scroll: QScrollBar):
            QObject.__init__(self)
            self.__scrollbar = scroll
            self.__orient = 1
            self.vel = 10

        def run(self):
            """Long-running task."""
            while True:

                if self.__scrollbar.maximum() > 0:
                    if self.__orient == 1:
                        if self.__scrollbar.maximum() - self.__scrollbar.value() < self.vel:
                            self.__scrollbar.setValue(self.__scrollbar.maximum())
                        self.__scrollbar.setValue(self.__scrollbar.value() + self.vel)

                    elif self.__orient == -1:
                        if self.__scrollbar.value() < self.vel:
                            self.__scrollbar.setValue(self.__scrollbar.minimum())
                        self.__scrollbar.setValue(self.__scrollbar.value() - self.vel)

                    print(self.__scrollbar.maximum(), self.__scrollbar.value())

                    if self.__scrollbar.value() == self.__scrollbar.maximum():
                        self.__orient = -1
                        sleep(1)

                    elif self.__scrollbar.value() == self.__scrollbar.minimum():
                        self.__orient = 1
                        sleep(1)

                else:

                    pass

                sleep(0.7)

    def show(self) -> None:
        QWidget.show(self)
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = self.Worker(self.scrollbar)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def debug(self, debug: bool = None):

        if debug is None:
            if not self.__debug:
                self.__debug = True

            else:
                self.__debug = False

        if self.__debug:

            self.setStyleSheet("")

        else:

            self.setStyleSheet("border: 0px solid black")

    def change_text(self, a0):

        self.__label.setText(a0)

    def closeEvent(self, a0: QCloseEvent) -> None:
        a0.accept()


app = QApplication(sys.argv)
noti = QAutoScrollLabel()
noti.show()
app.exec()
