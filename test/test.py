import auth_generator
import pull_data

def main():
    pull_data.adb_connect()
    path = input('저장경로 입력: ')
    pull_data.adb_pull(path)
    for s in auth_generator.data_extract(path):
        if s is None:
            print("추출할 데이터가 없습니다.")
        else:
            print(s)

if __name__ == "__main__":
    main()
