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
        # file_name: daum-dump daum-dump-2 nhn-dump ...
        # file_type: db json ...
        # app_name : daum nhn facebook ...
        file_name = file.split('.')[0]
        file_type = file.split('.')[-1]
        app_name = file_name.split('-')[0]
        # 파일명이 cookies가 아닐 경우
        if file_name != 'cookies':
            # 확장자가 db인 경우
            if file_type == 'db':
                db_file_name = path_dir + '\\' + file
                conn = sqlite3.connect(db_file_name)
                c = conn.cursor()
                try:
                    t = data_controller.search_db(app_name)['t']
                    sql = data_controller.search_db(app_name)['sql']
                    extracted_data = c.execute(sql, t)
                # None Type Error 방지.
                # data_controller에서 app_name을 찾지 못하면 모든 cookie값을 가져온다.
                except:
                    extracted_data = c.execute('SELECT name, value FROM cookies')
                    print("app_name: '{}' not found! select all cookie datas...".format(app_name))
                cookie_str = cookie_generate(extracted_data, file_name)
                cookie_list.append(cookie_str)
                conn.close()
            # 확장자가 db가 아니라 다른 분석 방법이 필요한 경우
            else:
                cookie_str = first_branch.data_extract_branch(path_dir, file_name)
                cookie_list.append(cookie_str)
    return cookie_list


# 인증 쿠키값을 추출하는 함수
# 매개변수는 name, value로 구성된 튜플로 들어온다.
def cookie_generate(name_value, file_name):
    cookie_str = ''
    for s in name_value:
        cookie_str += s[0] + '=' + s[1] + '\n'
    return file_name, cookie_str[:-1]
