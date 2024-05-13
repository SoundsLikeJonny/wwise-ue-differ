import functools
import os
from pathlib import (
    Path
)

from PySide6.QtCore import QThreadPool

"""
#######################################
########## DECORATORS #############
#######################################
"""

# class Threaded:
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#         self.threadpool = QThreadPool()
# 
#     def __call__(self, *args, **kwargs):
#         # return self.threadpool.start(self.func(*args, **kwargs))
#         return self.func(*args, **kwargs)


# def threaded(threadpool: QThreadPool = QThreadPool()):
#     def decorator_threaded(func):
#         @functools.wraps(func)
#         def wrapper_threaded(*args, **kwargs):
#             print(f'Starting Threaded function {func.__name__}')
#             threadpool.start(func(*args, **kwargs))
#             print(f'Threaded function {func.__name__} ended')
# 
#         return wrapper_threaded
# 
#     return decorator_threaded
