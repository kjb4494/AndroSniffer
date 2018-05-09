import sqlite3
import data_controller
import os
from except_data_pac import first_branch


# 인증에 유효한 데이터만 추출하는 함수
def data_extract(path_dir):
    try:
        file_list = os.listdir(path_dir)
    except:
        print('path not found.')
        return
    file_list.sort()
    cookie_list = []
    for file in file_list:
        file_name = file.split('.')[0]
        file_type = file.split('.')[-1]
        # 분석 가능한 파일만 분석한다.
        if file_name in data_controller.file_name_list():
            # 확장자가 db인 경우
            if file_type == 'db':
                db_file_name = path_dir + '\\' + file
                conn = sqlite3.connect(db_file_name)
                c = conn.cursor()
                # t = data_controller.search_db(file)['t']
                # sql = data_controller.search_db(file)['sql']
                # extracted_data = c.execute(sql, t)
                extracted_data = c.execute('SELECT name, value FROM cookies')
                cookie_str = cookie_generate(extracted_data, file_name)
                cookie_list.append(cookie_str)
                conn.close()
            # 확장자가 db가 아니라 다른 분석 방법이 필요한 경우
            else:
                cookie_str = first_branch.data_extract_branch(file_name)
                cookie_list.append(cookie_str)
    return cookie_list


# 인증 쿠키값을 추출하는 함수
# 매개변수는 name, value로 구성된 튜플로 들어온다.
def cookie_generate(name_value, file_name):
    cookie_str = ''
    for s in name_value:
        cookie_str += s[0] + '=' + s[1] + '\n'
    return file_name, cookie_str[:-1]
