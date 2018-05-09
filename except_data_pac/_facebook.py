import auth_generator
import re
import json

# 페이스북
# def cookie_generate(name_value, file_name) 함수로 return 시켜준다.
# name_value는 쿠키값의 name, value로 구성된 튜플
# file_name은 앱 이름-dump: 사용자가 구별하기 쉽게 하기 위해 주는 이름
def data_extract(path_dir, file_name):
    name_value = list()
    lines = open(path_dir + "\\" + file_name + ".json", 'r').read()
    m = re.search(r"\[(\{.*\})[,](\{.*\})[,](\{.*\})[,](\{.*\})\]", lines)
    for i in range(1, 4):
        dicts = json.loads(m.group(i))
        if dicts['name'] == 'c_user':
            name_value.append(('c_user', dicts['value']))
        elif dicts['name'] == 'xs':
            name_value.append(('xs', dicts['value']))
        elif dicts['name'] == 'fr':
            name_value.append(('fr', dicts['value']))

    name_value = tuple(name_value)
    file_name = 'facebook-dump'
    return auth_generator.cookie_generate(name_value, file_name)
