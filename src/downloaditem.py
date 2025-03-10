from PySide6 import QtWidgets, QtCore

from downloadthread import DownloadTask
from ui_downloaditem import Ui_DownloadItem
from utils.open_folder import open_folder
from utils.sizefstr import sizefStr


class DownloadItem(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None:
        super().__init__(parent)
        self.ui = Ui_DownloadItem()
        self.ui.setupUi(self)
        self.button_status = 0  # 0: Restart, 1: Open
        self.info = None
        self.connect(
            self.ui.button_open,
            QtCore.SIGNAL("clicked()"),
            self.on_button_clicked,
        )

    def setup_info(self, info: dict):
        self.info = info
        self.ui.label_title.setText(info["title"])
        self.ui.label_part.setText(info["name"])

    # Slot
    def update_status(self, data: str):
        self.ui.label_status.setText(data)

    # Slot
    def update_progress(self, finished: int, total: int):
        self.ui.label_progress.setText(
            "{} / {}".format(sizefStr(finished), sizefStr(total))
        )
        if total == 0:
            val = 0
        else:
            val = round(finished / total * 100)
        self.ui.progressBar.setValue(val)

    # Slot
    def update_finished(self):
        self.button_status = 1
        self.ui.button_open.setText("打开文件夹")

    # Slot
    def enable_button(self):
        self.ui.button_open.setEnabled(True)

    def re_start(self):
        self.ui.button_open.setEnabled(False)
        self.info["thread"].disconnect(self)
        self.info["thread"].t_stop()
        thread = DownloadTask(self.info["parent"])
        thread.setup(self.info)
        self.info["thread"] = thread
        thread.connect(
            thread,
            QtCore.SIGNAL("update_progress(quint64, quint64)"),
            self,
            QtCore.SLOT("update_progress(quint64, quint64)"),
        )
        thread.connect(
            thread,
            QtCore.SIGNAL("update_status(QString)"),
            self,
            QtCore.SLOT("update_status(QString)"),
        )
        thread.connect(
            thread,
            QtCore.SIGNAL("update_finished()"),
            self,
            QtCore.SLOT("update_finished()"),
        )
        thread.connect(
            thread,
            QtCore.SIGNAL("enable_restart()"),
            self,
            QtCore.SLOT("enable_button()"),
        )
        thread.start()

    def on_button_clicked(self):
        if self.button_status == 0:
            self.re_start()
        elif self.button_status == 1:
            directory = QtCore.QDir(self.info["path"])
            directory.cd(self.info["title"])
            open_folder(directory.absolutePath(), self.info["parent"])
