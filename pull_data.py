import subprocess
import data_controller
import os
from except_data_pac import first_branch


# cmd 명령어를 받아 처리한 후의 결과값을 return 하는 함수
def cmd_output(command):
    proc = subprocess.Popen(command, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, bufsize=1)
    return proc.communicate()[0].decode('utf-8')

# adb pull 명령어를 처리하는 함수
def pull_command(path, data_path, extension):
    tmp_name_split_list = data_path.split('.')
    # tmp_name: nhn, daum, facebook ...
    tmp_name = tmp_name_split_list[1]
    # save_path: PC에 저장될 파일 경로
    # ex) nhn-dump.db nhn-dump-2.db ... (동일명의 파일이 올 경우)
    save_path = path + '\\' + tmp_name + '-dump.' + extension
    # 권한 우회를 위해 내부 저장소에서 외부 저장소로 옮긴다.
    cmd_output('adb shell "su -c cp -f /data/data/' + data_path + ' /mnt/sdcard/' + tmp_name + '-tmp"')
    # 동일명의 파일이 있을 경우 파일명을 변경하고 PC로 가져온다.
    i = 2
    while os.path.exists(save_path):
        save_path = path + '\\' + tmp_name_split_list[1] + '-dump-' + str(i) + '.' + extension
        i += 1
    command = cmd_output('adb pull /mnt/sdcard/' + tmp_name + '-tmp ' + save_path)
    # PULL 작업이 끝나면 외부 저장소의 임시파일을 지운다.
    cmd_output('adb shell "su -c rm -rf /mnt/sdcard/' + tmp_name + '-tmp"')
    # 경로가 잘못됐거나 database에 없는 정보면 출력을 무시한다.
    if command.split(':')[1] != ' error':
        print(command)


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

    # 디바이스 연결 확인 및 루트 권한 부여
    if len(cmd_output('adb root')) > 0:
        print('no devices/emulators found')
        exit()


# adb로 필요한 데이터를 pull하는 함수
def adb_pull(path):
    data_paths = data_controller.path_database()
    exc_data_paths = data_controller.exc_path_database()
    for data_path in data_paths:
        # 예외적으로 처리해줘야할 앱의 경로
        if data_path in exc_data_paths:
            first_branch.pull_branch(path, data_path)
            continue
        pull_command(path, data_path, 'db')
