import textwrap
import frida
import os
import sys
import frida.core
import argparse
import logging

from fridump import *


def fridump(process):
    print("Operating Fridump Module...")

    APP_NAME = process
    DEBUG_LEVEL = logging.INFO
    MAX_SIZE = 20971520
    PERMS = 'rw-'

    logging.basicConfig(format='%(levelname)s:%(message)s', level=DEBUG_LEVEL)

    # 세션 수립
    session = None
    try:
        try:
            session = frida.get_usb_device().attach(APP_NAME)
        except:
            session = frida.attach(APP_NAME)
    except:
        print("Can't connect to App... {}".format(APP_NAME))
        return

    # 메모리 덤프를 저장할 디렉토리 생성 및 지정
    print("Current Directory: {}.".format(str(os.getcwd())))
    
    # 디렉토리를 만들기 위해 프로세스명의 다음과 같은 문자를 '-'로 대체
    process_name = process
    process_name = process_name.replace('\\', '-')
    process_name = process_name.replace('/', '-')
    process_name = process_name.replace(':', '-')
    process_name = process_name.replace('*', '-')
    process_name = process_name.replace('?', '-')
    process_name = process_name.replace('"', '-')
    process_name = process_name.replace('<', '-')
    process_name = process_name.replace('>', '-')
    process_name = process_name.replace('|', '-')

    DIRECTORY = os.path.join(os.getcwd(), "MemoryDumpFolder/"+process_name)
    print("Output directory is set to: {}".format(DIRECTORY))
    if not os.path.exists(DIRECTORY):
        print("Creating directory...")
        os.makedirs(DIRECTORY)

    # 메모리 덤프 시작
    print("Starting Memory dump of '{}' process...".format(process))
    mem_access_viol = ""
    Memories = session.enumerate_ranges(PERMS)
    i = 0
    l = len(Memories)

    # 덤프 데이터 저장
    for memory in Memories:
        base = memory.base_address
        logging.debug("Base Address: " + str(hex(base)))
        logging.debug("")
        size = memory.size
        logging.debug("Size: " + str(size))
        if size > MAX_SIZE:
            logging.debug("Too big, splitting the dump into chunks")
            mem_access_viol = dumper.splitter(session, base, size, MAX_SIZE, mem_access_viol, DIRECTORY)
            continue
        mem_access_viol = dumper.dump_to_file(session, base, size, mem_access_viol, DIRECTORY)
        i += 1
        utils.printProgress(i, l, prefix='Progress:', suffix='Complete', bar=50)
    print()

    # 덤프 데이터의 문자열 추출
    files = os.listdir(DIRECTORY)
    i = 0
    l = len(files)
    print("Running strings on all files:")
    for f1 in files:
        utils.strings(f1, DIRECTORY, process_name)
        i += 1
        utils.printProgress(i, l, prefix='Progress:', suffix='Complete', bar=50)

    print("Finished!")

    # 프로세스가 끝나지않는 버그가 있는거 같음...


# 연결된 디바이스의 모든 프로세스명을 가져오는 함수
def fridump_all():
    try:
        device = frida.get_device_manager().enumerate_devices()[-1]
    except:
        print("you must connect device")
        return
    processes = device.enumerate_processes()
    ps_list = []
    for process in processes:
        ps_list.append(process.name)
    return ps_list