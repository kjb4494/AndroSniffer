from except_data_pac import *


def fb(path, data_path):
    # 페이스북일 경우
    if data_path == 'com.facebook.katana/app_light_prefs/com.facebook.katana/authentication':
        _facebook.pull_exc_data(path, data_path)
