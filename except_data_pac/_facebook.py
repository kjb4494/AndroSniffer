# 페이스북
import pull_data

def pull_exc_data(path, data_path):
    tmp_name_split_list = data_path.split('.')
    save_path = path + '\\' + tmp_name_split_list[1] + '-dump.json'
    command = pull_data.cmd_output('adb pull /data/data/' + data_path + ' ' + save_path)
    # 경로가 잘못됐거나 database에 없는 정보면 출력을 무시한다.
    if command.split(':')[1] != ' error':
        print(command)