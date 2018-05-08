import subprocess
import data_controller
from except_data_pac import first_branch


# cmd 명령어를 받아 처리한 후의 결과값을 return 하는 함수
def cmd_output(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, bufsize=1)
    return proc.communicate()[0].decode('utf-8')


# adb에 연결하는 함수
def adb_connect():
    # 환경변수에 adb 설정되어있는지 확인
    try:
        print(cmd_output('adb --version'))
    except:
        print("adb not found error. please check path of adb...")
        exit()

    # Nox Test
    # print(cmd_output("adb connect 127.0.0.1:62001"))

    # 루트 권한 부여
    print(cmd_output('adb root'))


# adb로 필요한 데이터를 pull하는 함수
def adb_pull(path):
    data_paths = data_controller.path_database()
    exc_data_paths = data_controller.exc_path_database()
    for data_path in data_paths:
        # 예외적으로 처리해줘야할 앱의 경로
        if data_path in exc_data_paths:
            first_branch.fb(path, data_path)
            continue
        tmp_name_split_list = data_path.split('.')
        save_path = path + '\\' + tmp_name_split_list[1] + '-dump.db'
        command = cmd_output('adb pull /data/data/' + data_path + ' ' + save_path)
        # 경로가 잘못됐거나 database에 없는 정보면 출력을 무시한다.
        if command.split(':')[1] != ' error':
            print(command)
