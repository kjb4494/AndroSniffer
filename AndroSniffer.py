# 메인 모듈
import auth_generator
import pull_data
import time
import os
from tkinter import *
from tkinter import filedialog

class MainFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("AndroSniffer")
        self.master.minsize(width=700, height=700)
        self.master.maxsize(width=700, height=700)
        self.pack(fill=BOTH, expand=True)

        # 폴더 선택 프레임
        searchPathFrame = Frame(self)
        searchPathFrame.pack(fill=X)

        dirPathEntry = Entry(searchPathFrame)
        dirPathEntry.pack(side=LEFT, fill=X, padx=5, pady=10, expand=True)
        execButton = Button(searchPathFrame, text="실행", width=10)
        execButton.pack(side=RIGHT, fill=X, padx=5, pady=10, expand=False)
        searchPathButton = Button(searchPathFrame, text="저장경로 찾기", width=15)
        searchPathButton.pack(side=RIGHT, fill=X, padx=5, pady=10, expand=False)

        # 로그창 프레임
        logFrame = Frame(self)
        logFrame.pack(fill=X)

        logText = Text(logFrame, height=600, state=DISABLED)
        logText.pack(fill=X, padx=5, pady=10, expand=True)
        # self.insertLogText(logText, "Hello")

    def insertLogText(self, logText, textStr):
        logText.config(state=NORMAL)
        logText.insert(INSERT, textStr)
        logText.config(state=DISABLED)

    def searchDirPath(self, dirPathEntry):
        dirName = filedialog.askdirectory()
        dirPathEntry.insert(INSERT, dirName)

def main():
    root = Tk()
    MainFrame(root)
    root.mainloop()

    # adb 연결 여부 확인
    pull_data.adb_connect()

    # 작업영역 생성하기
    root_dir = input('저장경로 입력: ')
    if not os.path.exists(root_dir):
        print("[Failed] path not found...:(")
        return
    now = time.localtime()
    today = "%04d-%02d-%02d-%02d-%02d-%02d" % \
            (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    work_dir = root_dir + '/' + today
    try:
        if not os.path.exists(work_dir):
            os.mkdir(work_dir)
    except:
        print("[Failed] can not create workspace this path...;(")
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
            print("[Notice] {}: 추출할 데이터가 없으므로 파일을 생성하지않습니다.".format(file_name))
        else:
            file_path = cookies_dir + '/' + file_name
            with open(file_path, 'w') as f:
                f.write(s[1])
    print("[BYE] finished! :)")


if __name__ == "__main__":
    main()
