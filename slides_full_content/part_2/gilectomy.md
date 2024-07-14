It was only ever an experimental project, and the last update I saw (Pycon 2019) was that after significant work he was still able to get the performance of his non-GIL version to match that of to Python with the GIL, but with a significant caveat; the default Python version ran only on a single core (as expected) - the non GIL version needed to run on 7 cores to keep up.

Larry Hastings has admitted that work has stalled, and he needs a new approach since the general idea of trying to maintain the general reference counting system, but protect the reference counts without a Global lock is not tenable.

https://www.quora.com/What-happened-to-Larry-Hastings-and-the-Python-GILectomy-GIL-removal-project