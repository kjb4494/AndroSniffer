import auth_generator

def main():
    path = input('분석 경로 입력: ')
    auth_generator.data_extract(path)

if __name__ == "__main__":
    main()
