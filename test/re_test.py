# import re
#
# pattern = re.compile('[a-z]+')  # re.compile('정규표현식 패턴')을 하면 해당 '정규표현식 패턴' 해당하는 패턴 객체가 생성된다
# match = pattern.match("python")  # 위에서 생성된 패턴 객체로 특정 텍스트에서 결과를 가져올 수 있다.
#
# print(match.group()) # 결과는 group()에 저장이 된다.



#

# pattern = re.compile('[\.\,\?\!a-zA-Z0-9\u3131-\u3163\uac00-\ud7a3]+') # 한글과 영어 숫자
# pattern = re.compile('[a-z]+') # 패턴 객체를 가져옴

# result = pattern.match('''hello123asdcc6&ASWQA\nasdaf2\t asdfasdf''') # 위에서 얻은 패턴 객체로 매칭함

import re
pattern = re.compile(u'[^ ~`!@#$%^&*()_\-+={\[}\]:<.>/?\'\"\n\ta-zA-Z0-9\u3131-\u3163\uac00-\ud7a3]+') # 한글 키보드 특문 영어 숫자

input = ''
result = re.sub(pattern, ' ', input)

print(result)