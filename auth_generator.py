import sqlite3
import data_controller
import os
from except_data_pac import first_branch


# 인증에 유효한 데이터만 추출하는 함수
class AuthGenerator:
    def __init__(self, MainFrame, path_dir):
        self.mainFrame = MainFrame
        self.path_dir = path_dir
        self.file_name = ''
        self.cookie_str = ''

    def data_extract(self):
        try:
            file_list = os.listdir(self.path_dir)
        except:
            self.mainFrame.insertLogText('[Failed] path not found.')
            return
        file_list.sort()
        cookie_list = []
        for file in file_list:
            # file_name: daum-dump daum-dump-2 nhn-dump ...
            # file_type: db json ...
            # app_name : daum nhn facebook ...
            self.file_name = file.split('.')[0]
            file_type = file.split('.')[-1]
            app_name = self.file_name.split('-')[0]
            # 파일명이 cookies가 아닐 경우
            if self.file_name != 'cookies':
                # 확장자가 db인 경우
                if file_type == 'db':
                    db_file_name = self.path_dir + '\\' + file
                    conn = sqlite3.connect(db_file_name)
                    c = conn.cursor()
                    try:
                        for host_key in data_controller.host_key_db(app_name):
                            t = data_controller.search_db(app_name, host_key)['t']
                            sql = data_controller.search_db(app_name, host_key)['sql']
                            extracted_data = c.execute(sql, t)
                            add_str = self.cookie_str_join(extracted_data)
                            if add_str != '':
                                self.cookie_str += '[' + host_key + ']\n'
                                self.cookie_str += add_str + '\n'
                    # None Type Error 방지.
                    # data_controller에서 app_name을 찾지 못하면 모든 cookie값을 가져온다.
                    except:
                        extracted_data = c.execute('SELECT name, value FROM cookies')
                        self.mainFrame.insertLogText(
                            "[Notice] '{}'앱은 필터링이 등록되지 않았습니다. 대신 모든 쿠키값을 가져옵니다.".format(app_name))
                        self.cookie_str += self.cookie_str_join(extracted_data)
                    cookie_list.append(self.cookie_generate())
                    conn.close()
                # 확장자가 db가 아니라 다른 분석 방법이 필요한 경우
                else:
                    self.cookie_str = first_branch.data_extract_branch(self)
                    cookie_list.append(self.cookie_generate())
        return cookie_list

    # 인증에 유효한 쿠키값을 문자열로 추출하는 함수
    # 매개변수는 name, value로 구성된 튜플로 들어온다.
    def cookie_str_join(self, name_value):
        cookie_str = ''
        for s in name_value:
            cookie_str += s[0] + '=' + s[1] + '\n'
        return cookie_str

    # 최종적으로 cookie_list에 들어갈 가공이 끝난 정보
    def cookie_generate(self):
        cookie_tuple = (self.file_name, self.cookie_str)
        self.cookie_str = ''
        return cookie_tuple
