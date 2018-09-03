from modules.collection import crawler
import os

# COLLECTION 에서 크롤링 결과 저장할 데이터 폴더 : with_SCV

RESULT_DIRECTORY = '__result__'

if os.path.exists(RESULT_DIRECTORY) is False:
    os.mkdir(RESULT_DIRECTORY)