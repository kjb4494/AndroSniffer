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
        self.searchPathFrame = Frame(self)
        self.searchPathFrame.pack(fill=X)

        self.dirPathEntry = Entry(self.searchPathFrame)
        self.dirPathEntry.pack(side=LEFT, fill=X, padx=5, pady=10, expand=True)
        self.execButton = Button(self.searchPathFrame, text="실행", width=10, command=self.exec)
        self.execButton.pack(side=RIGHT, fill=X, padx=5, pady=10, expand=False)
        self.searchPathButton = Button(self.searchPathFrame, text="저장경로 찾기", width=15, command=self.searchDirPath)
        self.searchPathButton.pack(side=RIGHT, fill=X, padx=5, pady=10, expand=False)

        # 로그창 프레임
        self.logFrame = Frame(self)
        self.logFrame.pack(fill=X)

        self.logText = Text(self.logFrame, height=600, state=DISABLED)
        self.logText.pack(fill=X, padx=5, pady=10, expand=True)

    def insertLogText(self, textStr):
        self.logText.config(state=NORMAL)
        self.logText.insert(END, textStr + '\n')
        self.logText.config(state=DISABLED)
        self.logText.see(END)
        self.update()

    def searchDirPath(self):
        dirName = filedialog.askdirectory()
        self.dirPathEntry.delete(0, END)
        self.dirPathEntry.insert(INSERT, dirName)

    def exec(self):
        self.execButton.config(state=DISABLED)
        # adb 연결 여부 확인
        pullData = pull_data.PullData(self)
        if pullData.adb_connect() == 0:
            self.execButton.config(state=NORMAL)
            return

        # 작업영역 생성하기
        root_dir = self.dirPathEntry.get()
        if not os.path.exists(root_dir):
            self.insertLogText("[Failed] path not found...:(")
            self.execButton.config(state=NORMAL)
            return
        now = time.localtime()
        today = "%04d-%02d-%02d-%02d-%02d-%02d" % \
                (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        pullData.path = root_dir + '/' + today   # work_dir
        try:
            if not os.path.exists(pullData.path):
                os.mkdir(pullData.path)
        except:
            self.insertLogText("[Failed] can not create workspace this path...;(")
            self.execButton.config(state=NORMAL)
            return
        # adb pull로 파일 받아오기
        pullData.adb_pull()
        # 파일을 분석해서 유효 데이터 추출하기
        authGenerator = auth_generator.AuthGenerator(self, pullData.path)
        cookies_dir = authGenerator.path_dir + '/' + 'cookies'
        if not os.path.exists(cookies_dir):
            os.mkdir(cookies_dir)
        for s in authGenerator.data_extract():
            file_name = s[0].replace('dump', 'cookie') + '.txt'
            if s[1] == '':
                self.insertLogText("[Notice] {}: 추출할 데이터가 없으므로 파일을 생성하지않습니다.".format(file_name))
            else:
                file_path = cookies_dir + '/' + file_name
                with open(file_path, 'w') as f:
                    f.write(s[1])
        self.insertLogText("[BYE] finished! :)")
        self.execButton.config(state=NORMAL)

def main():
    # GUI 프레임 생성
    root = Tk()
    MainFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
