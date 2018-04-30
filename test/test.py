from fridump import fridump

def main():
    processName = input("프로세스명 입력: ")
    fridump.fridump(processName)


if __name__ == "__main__":
    main()