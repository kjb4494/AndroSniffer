from except_data_pac import *
import pull_data


# adb pull로 인증 파일을 가져올 때 분기점 함수
def pull_branch(path, data_path):
    # 페이스북일 경우
    if data_path == 'com.facebook.katana/app_light_prefs/com.facebook.katana/authentication':
        pull_data.pull_command(path, data_path, 'json')


# 파일을 분석할 때 분기점 함수
def data_extract_branch(file_name):
    # 페이스북일 경우
    if file_name == 'facebook-dump':
        _facebook.data_extract()
