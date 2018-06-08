from except_data_pac import *


# adb pull로 인증 파일을 가져올 때 분기점 함수
# 앱의 인증파일 경로를 비교하고 분석에 적절한 확장자를 지정해준다.
def pull_branch(PullData):
    # 페이스북일 경우
    if PullData.data_path == 'com.facebook.katana/app_light_prefs/com.facebook.katana/authentication':
        PullData.extension = 'json'
        # real device 환경
        PullData.pull_command()
        # 가상 환경
        # PullData.pull_command_for_nox()


# 파일을 분석할 때 분기점 함수
# file_name = 앱의 인증파일 경로를 '.'으로 split한 두번째 단어-dump
# _앱이름.data_extract()로 맵핑
def data_extract_branch(AuthGenerator):
    # 페이스북일 경우
    if AuthGenerator.file_name == 'facebook-dump':
        return _facebook.data_extract(AuthGenerator)
