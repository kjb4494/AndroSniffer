import auth_generator


# 페이스북
# def cookie_generate(name_value, file_name) 함수로 return 시켜준다.
# name_value는 쿠키값의 name, value로 구성된 튜플
# file_name은 앱 이름-dump: 사용자가 구별하기 쉽게 하기 위해 주는 이름
def data_extract():
    name_value = (('ex01', 'ex01-value'), ('ex02', 'ex02-value'),)
    file_name = 'facebook-dump'
    return auth_generator.cookie_generate(name_value, file_name)
