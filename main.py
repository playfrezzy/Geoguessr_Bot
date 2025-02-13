import sys
from screenshot import process_screenshot
from io import BytesIO
from openai import OpenAI
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal, QObject

from ui_mainwindow import Ui_MainWindow


class Worker(QObject):
    finished = pyqtSignal(str)

    def run(self):
        try:
            client = OpenAI()

            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system",
                     "content": "You are a guessr who guesses locations from photos. You will answer briefly with a name of region such as 'Southeast France'. Finally, ignore the map in the bottom right and the text in the top left."
                     },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "Where does this photo belong?",
                            },
                            {
                                "type": "image_url",
                                "image_url": {"url": f"data:image/jpeg;base64,{process_screenshot()}"},
                            },
                        ],
                    }
                ],
            )
            result = completion.choices[0].message.content
        except Exception as e:
            result = f"Error: {str(e)}"

        self.finished.emit(result)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(self.start_worker)

    def start_worker(self):
        # Buton devre dışı bırakılıyor ve işlem mesajı gösteriliyor
        self.ui.button.setEnabled(False)
        self.ui.result_label.setText("Processing...")

        # İş parçacığı ve worker ayarlanıyor
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.on_finished)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def on_finished(self, result):
        # Sonuç ekranda gösteriliyor ve buton yeniden etkinleştiriliyor
        self.ui.result_label.setText(result)
        self.ui.button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
