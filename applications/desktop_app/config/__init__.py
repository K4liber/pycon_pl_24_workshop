import sys


NUMBER_OF_WORKERS = 8
NUMBER_OF_JOBS = 40


def sys_info() -> str:
    gil_disabled = False

    if hasattr(sys, "_is_gil_enabled"):
        gil_disabled = bool(not sys._is_gil_enabled())

    gil_info = f'(GIL ' + ('disabled)' if gil_disabled else 'enabled)')
    return f'{gil_info} {sys.version})'
