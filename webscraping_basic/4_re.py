# regular expression?

# 주민등록번호는 6-7자리 숫자로 표현되지요.
# 이메일 주소는 asdf@naver.com 이런 식으로죠

import re

# 교통사고를 목격했는데 뺑소니야! 차 번호판을 보는 거죠!
# abcd, book, desk
# 4글자가 모두 기억이 안나.. ca?e 인거같아.

p = re.compile("ca.e") # 주어진 문자열의 처음부터 일치하는지 확인.

# .: 하나의 문자를 의미
# ^: 문자열의 시작 (^de): desk, debug(ok), fade (x)
# $: 문자열의 끝 (se$): case, sense(ok), bases (x)

m = re.compile("ca.e").match("cafe")# print(m.group()) # 매치 안되면 error

def print_match(m):
    if m:
        print(m.group()) # 일치하는 문자열 반환
        print(m.string) # 입력받은 문자열
        print(m.start()) # 일치하는 문자열 시작 index
        print(m.end()) #일치하는 문자열의 끝 index
        print(m.span()) # 일치하는 문자열의 시작, 끝 index
    else:
        print("no matching")


# m = p.search("good care") # 주어진 문자열 중에 일치하는 것이 있는가?
# print_match(m)

lst = p.findall("case carelss cafe cadef fesdf") #일치하는 무든 것을 리스트 형태로 반환
print(lst)

# 1. p = re.complie("원하는 형태")
# 2. m = p.match("비교할 문자열") 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") 주어진 문자열 중에 일치하는게 있늕
# 4. m = p.findall("비교할 문자열") 일치하는 모든 것을 리스트로 반환

# 원하는 형태 : 정규식

# .: 하나의 문자를 의미
# ^: 문자열의 시작 (^de): desk, debug(ok), fade (x)
# $: 문자열의 끝 (se$): case, sense(ok), bases (x)
