from collection import crawler
from collection import collect
import os

RESULT_DIRECTORY = '__result__'

if os.path.exists(RESULT_DIRECTORY) is False:
    os.mkdir(RESULT_DIRECTORY)