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
