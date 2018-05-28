import auth_generator
import re
import json

# 페이스북
# def cookie_generate(file_name, cookie_str) 함수로 return 시켜준다.
# name_value는 쿠키값의 name, value로 구성된 튜플
#   --> cookie_str_join(name_value) 함수를 이용해 cookie_str을 만들 수 있다.
# file_name은 앱 이름-dump: 사용자가 구별하기 쉽게 하기 위해 주는 이름
def data_extract(AuthGenerator, path_dir, file_name):
    name_value = list()
    # 파일 참조과정에서 인코딩 에러
    lines = open(path_dir + "\\" + file_name + ".json", 'r').read()
    m = re.search(r"\[(\{.*\})[,](\{.*\})[,](\{.*\})[,](\{.*\})\]", lines)
    for i in range(1, 4):
        #json객체를 다시 딕셔너리로 변환
        dicts = json.loads(m.group(i))
        if dicts['name'] == 'c_user':
            name_value.append(('c_user', dicts['value']))
        elif dicts['name'] == 'xs':
            name_value.append(('xs', dicts['value']))
        elif dicts['name'] == 'fr':
            name_value.append(('fr', dicts['value']))

    name_value = tuple(name_value)
    file_name = 'facebook-dump'
    cookie_str = AuthGenerator.cookie_str_join(name_value)
    return AuthGenerator.cookie_generate(file_name, cookie_str)
