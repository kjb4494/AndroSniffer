def path_database():
    # 분석이 끝난 앱의 인증파일 경로
    data_list = ['com.nhn.android.search/app_webview/Cookies',
                 'com.nhn.android.search/app_xwalkcore/Default/Cookies',
                 'net.daum.android.daum/app_webview/Cookies',
                 'com.twitter.android/app_webview/Cookies',
                 'com.nate.android.portalmini/app_webview/Cookies',
                 'com.google.android.googlequicksearchbox/app_webview/Cookies',
                 'com.google.android.gms/app_webview/Cookies']
    return data_list


def exc_path_database():
    # 예외적으로 처리해야할 앱의 인증파일 경로
    data_exception_list = ['com.facebook.katana/app_light_prefs/com.facebook.katana/authentication']
    return data_exception_list


# =============================================================


def search_db(app_name):
    # 각 앱의 인증에 유효한 데이터만을 추출하는데 필요한 변수 모음
    # 네이버
    if app_name == 'nhn':
        t = ('nid_inf', 'NID_AUT', 'NID_JKL', 'NID_SES',)
        sql = 'SELECT name, value ' \
              'FROM cookies ' \
              'WHERE name=? or name=? or name=? or name=?'
        return {'t': t, 'sql': sql}
    # 다음
    elif app_name == 'daum':
        t = ('TS', 'HTS', 'HM_CU', 'PROF', 'ALID', 'LSID',)
        sql = 'SELECT name, value ' \
              'FROM cookies ' \
              'WHERE name=? or name=? or name=? or name=? or name=? or name=?'
        return {'t': t, 'sql': sql}
    # 페이스북
    elif app_name == 'facebook':
        t = ('c_user', 'xs', 'fr',)
        sql = 'SELECT name, value ' \
              'FROM cookies ' \
              'WHERE name=? or name=? or name=?'
        return {'t': t, 'sql': sql}
    elif app_name == 'nate':
        t = ('.nate.com', 'SFN',)
        sql = 'SELECT name, value ' \
              'FROM cookies ' \
              'WHERE host_key=? and name=?'
        return {'t': t, 'sql': sql}
    return
