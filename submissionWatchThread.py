# -*- coding: utf-8 -*-
from PySide6.QtCore import QThread, Signal
from time import sleep
from api.submit import get_submission_status

class SubmissionWatchThread(QThread):
    updateSignal = Signal(str)
    UPDATE_INTERVAL = 0.5

    def __init__(self, contest, sid, cookiejar, parent=None):
        super().__init__(parent)
        self.contest = contest
        self.sid = sid
        self.cookiejar = cookiejar

    def run(self):
        sleep(2)
        while True:
            details, summary = get_submission_status(self.contest, self.sid, self.cookiejar)
            if '/' in summary:
                self.updateSignal.emit(f'{summary} ...')
            elif summary == 'WJ':
                self.updateSignal.emit(f'{details} ...')
            else:
                self.updateSignal.emit(details)
                self.exit(0)
                return
            sleep(self.UPDATE_INTERVAL)