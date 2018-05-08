from except_data_pac import *
import pull_data


def pull_branch(path, data_path):
    # 페이스북일 경우
    if data_path == 'com.facebook.katana/app_light_prefs/com.facebook.katana/authentication':
        pull_data.pull_command(path, data_path, 'json')
