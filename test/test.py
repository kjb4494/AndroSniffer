import pull_data

def main():
    pull_data.adb_connect()
    path = input('저장경로 입력: ')
    pull_data.adb_pull(path)

if __name__ == "__main__":
    main()
