import logging
import os
import time
from functools import partial

from PyQt5.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                             QLineEdit, QMainWindow, QProgressBar, QPushButton,
                             QVBoxLayout, QWidget)
from PyQt5 import QtCore

import config
from job.callables import get_available_callables, get_callable
from job.callable_return import CallableReturn
from runner.factory import RUNNER_TYPE, get_runner

logging.basicConfig(
    format='%(levelname)s: %(message)s',
)
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)


class RunnerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal(object)


class RunnerRunnable(QtCore.QRunnable):

    def __init__(self, func, args=None, kwargs=None):
        super().__init__()
        self.setAutoDelete(True)
        self.func = func
        self.args = args if args else []
        self.kwargs = kwargs if kwargs else {}

    @QtCore.pyqtSlot()
    def run(self):
        self.func(*self.args, **self.kwargs)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(config.sys_info())
        self.setGeometry(0, 0, 400, 300)
        self._central_widget = QWidget()
        self._layout = QVBoxLayout()
        self._thread_id_to_worker_id = dict()
        # Start button
        self._start_button = QPushButton('Start')
        self._start_button.clicked.connect(self._start_job)
        self._layout.addWidget(self._start_button)
        # Worker type selection
        type_selection_widget = QWidget()
        type_selection_layout = QHBoxLayout()
        type_selection_label = QLabel('Unit of execution:')
        self._worker_type_combo = QComboBox()
        self._worker_type_combo.addItem(RUNNER_TYPE.THREAD)
        self._worker_type_combo.addItem(RUNNER_TYPE.PROCESS)
        self._worker_type_combo.addItem(RUNNER_TYPE.SUBINTERPRETER)
        self._worker_type_combo.currentTextChanged.connect(self._worker_type_changed)
        type_selection_layout.addWidget(type_selection_label)
        type_selection_layout.addWidget(self._worker_type_combo)
        type_selection_widget.setLayout(type_selection_layout)
        self._layout.addWidget(type_selection_widget)
        # Function to execute selection
        function_selection_widget = QWidget()
        function_selection_layout = QHBoxLayout()
        function_selection_label = QLabel('Function to execute:')
        self._function_selection_combo = QComboBox()

        for function_name in get_available_callables():
            self._function_selection_combo.addItem(function_name)

        function_selection_layout.addWidget(function_selection_label)
        function_selection_layout.addWidget(self._function_selection_combo)
        function_selection_widget.setLayout(function_selection_layout)
        self._layout.addWidget(function_selection_widget)
        # Function args selection
        function_args_widget = QWidget()
        function_args_layout = QHBoxLayout()
        function_args_label = QLabel('Function arguments:')
        self._function_args_text_area = QLineEdit()
        self._function_args_text_area.setFixedSize(188, 25)
        self._function_args_text_area.setText('34')
        function_args_layout.addWidget(function_args_label)
        function_args_layout.addWidget(self._function_args_text_area)
        function_args_widget.setLayout(function_args_layout)
        self._layout.addWidget(function_args_widget)
        # Progress bars
        self._progress_bars = []
        self._create_progress_bars(number_of_workers=config.NUMBER_OF_WORKERS)

        for progress_bar_index, progress_bar in enumerate(
                [self._progress_bars[-1]] + self._progress_bars[:len(self._progress_bars)-1]
            ):
            if progress_bar_index == 0:
                label = 'Overall'
            else:
                label = f"Worker {progress_bar_index}"

            worker_widget = QWidget()
            worker_layout = QHBoxLayout()
            worker_label = QLabel(label)
            worker_label.setFixedSize(70, 20)
            worker_layout.addWidget(worker_label)
            worker_layout.addWidget(progress_bar)
            worker_widget.setLayout(worker_layout)
            self._layout.addWidget(worker_widget)

        # Timing
        timing_widget = QWidget()
        timing_widget.setFixedSize(400, 40)
        timing_layout = QHBoxLayout()
        self._timing_init_label = QLabel('Initialization [s]: ')
        self._timing_init_label.setFixedSize(140, 20)
        self._timing_init_value = QLabel('-')
        self._timing_init_value.setFixedSize(40, 20)
        self._timing_overall_label = QLabel('Overall [s]: ')
        self._timing_overall_label.setFixedSize(100, 20)
        self._timing_overall_value = QLabel('-')
        self._timing_overall_value.setFixedSize(40, 20)
        timing_layout.addWidget(self._timing_init_label)
        timing_layout.addWidget(self._timing_init_value)
        timing_layout.addWidget(self._timing_overall_label)
        timing_layout.addWidget(self._timing_overall_value)
        timing_widget.setLayout(timing_layout)
        self._layout.addWidget(timing_widget)
        # Finalizing
        self._central_widget.setLayout(self._layout)
        self.setCentralWidget(self._central_widget)
        self._time_start = None
        self.signals = RunnerSignals()
        self.signals.finished.connect(self.on_runner_finished)
        self._pid_to_memory_usage = dict()

    def _clear(self) -> None:
        for progress_bar in self._progress_bars:
            progress_bar.setValue(0)
        
        self._timing_init_value.setText('-')
        self._timing_overall_value.setText('-')
        self._pid_to_memory_usage.clear()
        self._thread_id_to_worker_id.clear()

    def _worker_type_changed(self, _) -> None:
        self._clear()

    def _callback(
            self,
            callable_return: CallableReturn | None = None
        ) -> None:
        if callable_return:
            self._pid_to_memory_usage.update(callable_return.pid_to_memory_usage)

        self.signals.finished.emit(callable_return)

    def _get_worker_id(self, thread_id: int) -> int:
        if thread_id not in self._thread_id_to_worker_id:
            self._thread_id_to_worker_id[thread_id] = len(self._thread_id_to_worker_id)

        return self._thread_id_to_worker_id[thread_id]

    def on_runner_finished(
            self,
            callable_return: CallableReturn | None = None
        ) -> None:
        worker_id = None

        if callable_return is not None:
            worker_id = self._get_worker_id(thread_id=callable_return.thread_id)
            _logger.info(f'Task completed. Worker id = {worker_id}, result = {callable_return.result}')
        else:
            _logger.info('Tasks started successfully.')

        if worker_id is not None:
            self._advance_progress_bar(worker_index=worker_id)
            self._advance_progress_bar()
        else:
            init_time = int((time.time() - self._time_start) * 100)/100
            self._timing_init_value.setText(str(init_time))
        
        self.repaint()

    def _start_job(self) -> None:
        _logger.info('#' * 50)
        self._clear()
        self._worker_type_combo.setDisabled(True)
        self._start_button.setDisabled(True)
        self._function_selection_combo.setDisabled(True)
        self._function_args_text_area.setDisabled(True)
        self._start_button.setText("Running ...")
        self.repaint()
        runner = get_runner(runner_type=self._worker_type_combo.currentText())
        self._time_start = time.time()
        args = self._function_args_text_area.text().split(',')
        selected_callable = get_callable(
            callable_name=self._function_selection_combo.currentText(),
            args=args,
            use_psutil=self._worker_type_combo.currentText() != RUNNER_TYPE.SUBINTERPRETER
        )
        callables_list = [
            selected_callable
            for _ in range(config.NUMBER_OF_JOBS)
        ]
        main_process_pid = os.getpid()
        _logger.info(
            f'Starting runner "{runner.runner_type}" with {runner.no_workers} workers.\n'
            f'Number of tasks: {config.NUMBER_OF_JOBS}\n'
            f'Main process PID = {main_process_pid}\n'
        )
        runnable = RunnerRunnable(
            func=partial(
                runner.start,
                callables_list=callables_list,
                callback=self._callback
            )
        )
        QtCore.QThreadPool.globalInstance().start(runnable)

    def _advance_progress_bar(self, worker_index: int | None = None) -> None:
        global_progress_bar_index = len(self._progress_bars) - 1
        
        if worker_index is None:
            worker_index = global_progress_bar_index

        progress_bar = self._progress_bars[worker_index]
        current_value = progress_bar.value()
        progress_bar.setValue(int(current_value + 1))
        global_progress_bar = self._progress_bars[global_progress_bar_index]
        # If all tasks finished
        if global_progress_bar.value() == config.NUMBER_OF_JOBS:
            init_time = self._timing_init_value.text()
            overall_time = str(int((time.time() - self._time_start) * 100)/100)
            self._timing_overall_value.setText(overall_time)
            _logger.info('-' * 10 + 'SUMMARY' + '-' * 10)
            _logger.info(f'All tasks completed successfully in {overall_time} [s]. Init time: {init_time} [s].')
            self._worker_type_combo.setDisabled(False)
            self._start_button.setDisabled(False)
            self._start_button.setText("Start")
            self._function_selection_combo.setDisabled(False)
            self._function_args_text_area.setDisabled(False)
            _logger.info(f'PID to memory usage (in MB): {self._pid_to_memory_usage}')
            _logger.info(f'Overall memory usage: {sum(self._pid_to_memory_usage.values())} [MB]')

    def _create_progress_bars(self, number_of_workers: int) -> None:
        for _ in range(number_of_workers):
            worker_progress_bar = QProgressBar()
            worker_progress_bar.setRange(0, config.NUMBER_OF_JOBS)
            worker_progress_bar.setValue(0)
            self._progress_bars.append(worker_progress_bar)
        
        job_progress_bar = QProgressBar()
        job_progress_bar.setRange(0, config.NUMBER_OF_JOBS)
        job_progress_bar.setValue(0)
        self._progress_bars.append(job_progress_bar)


if __name__ == '__main__':
    _logger.info(config.sys_info())
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
