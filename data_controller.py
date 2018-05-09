def path_database():
    # 분석이 끝난 앱의 인증파일 경로
    data_list = ['com.nhn.android.search/app_webview/Cookies',
                 'net.daum.android.daum/app_webview/Cookies',
                 'com.facebook.lite/app_webview/Cookies',
                 'com.facebook.katana/app_light_prefs/com.facebook.katana/authentication']
    return data_list


def exc_path_database():
    # 예외적으로 처리해야할 앱의 인증파일 경로
    data_exception_list = ['com.facebook.katana/app_light_prefs/com.facebook.katana/authentication']
    return data_exception_list


# =============================================================

def file_name_list():
    # 분석 가능한 파일명
    return [i.split('.')[1] + '-dump' for i in path_database()]

def search_db(file_name):
    # 각 앱의 인증에 유효한 데이터를 추출하는데 필요한 변수 모음
    # 네이버
    if file_name == 'nhn-dump.db':
        t = ('nid_inf', 'NID_AUT', 'NID_JKL', 'NID_SES',)
        sql = 'SELECT name, value ' \
              'FROM cookies ' \
              'WHERE name=? or name=? or name=? or name=?'
        return {'t': t, 'sql': sql}
    # 다음
    elif file_name == 'daum-dump.db':
        t = ('TS', 'HTS', 'HM_CU', 'PROF', 'ALID', 'LSID',)
        sql = 'SELECT name, value ' \
              'FROM cookies ' \
              'WHERE name=? or name=? or name=? or name=? or name=? or name=?'
        return {'t': t, 'sql': sql}
    # 페이스북
    elif file_name == 'facebook-dump.db':
        t = ('c_user', 'xs', 'fr',)
        sql = 'SELECT name, value ' \
              'FROM cookies ' \
              'WHERE name=? or name=? or name=?'
        return {'t': t, 'sql': sql}
    return
