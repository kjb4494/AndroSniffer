# 메인 모듈
import auth_generator
import pull_data
import time
import os

def main():
    # adb 연결 여부 확인
    pull_data.adb_connect()

    # 작업영역 생성하기
    root_dir = input('저장경로 입력: ')
    if not os.path.exists(root_dir):
        print("path not found...:(")
        return
    now = time.localtime()
    today = "%04d-%02d-%02d-%02d-%02d-%02d" % \
            (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    work_dir = root_dir + '/' + today
    try:
        if not os.path.exists(work_dir):
            os.mkdir(work_dir)
    except:
        print("can not create workspace this path...;(")
        return

    # adb pull로 파일 받아오기
    pull_data.adb_pull(work_dir)

    # 파일을 분석해서 유효 데이터 추출하기
    cookies_dir = work_dir + '/' + 'cookies'
    if not os.path.exists(cookies_dir):
        os.mkdir(cookies_dir)
    for s in auth_generator.data_extract(work_dir):
        file_name = s[0].replace('dump', 'cookie') + '.txt'
        if s[1] == '':
            print("{}: 추출할 데이터가 없습니다.".format(file_name))
        else:
            file_path = cookies_dir + '/' + file_name
            with open(file_path, 'w') as f:
                f.write(s[1])
    print("finished! :)")


if __name__ == "__main__":
    main()
