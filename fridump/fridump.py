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
        # if USB:
        #     session = frida.get_usb_device().attach(APP_NAME)
        # else:
        #     session = frida.attach(APP_NAME)
        try:
            session = frida.get_usb_device().attach(APP_NAME)
        except:
            session = frida.attach(APP_NAME)
    except:
        print("Can't connect to App. Have you connected the device?")
        sys.exit(0)

    # 메모리 덤프를 저장할 디렉토리 생성 및 지정
    print("Current Directory: {}.".format(str(os.getcwd())))
    DIRECTORY = os.path.join(os.getcwd(), "MemoryDumpFolder")
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
        utils.strings(f1, DIRECTORY, process)
        i += 1
        utils.printProgress(i, l, prefix='Progress:', suffix='Complete', bar=50)

    print("Finished!")

    # 프로세스가 끝나지않는 버그가 있는거 같음...