# 메인 모듈

import pull_data
import auth_generator

def main():
    pull_data.adb_connect()
    path = input('저장경로 입력: ')
    pull_data.adb_pull(path)


if __name__ == "__main__":
    main()
