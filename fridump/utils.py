import sys
import string
import logging
import os
import re


# Progress bar function
def printProgress(times, total, prefix='', suffix='', decimals=2, bar=100):
    filled = int(round(bar * times / float(total)))
    percents = round(100.00 * (times / float(total)), decimals)
    bar = '#' * filled + '-' * (bar - filled)
    print('\r%s [%s] %s%s %s' % (prefix, bar, percents, '%', suffix), end="", flush=False)
    if times == total:
        print()


# A very basic implementations of Strings
def strings(filename, directory, processName, min=4):
    strings_file_name = processName + "_strings.txt"
    strings_file = os.path.join(directory, strings_file_name)
    path = os.path.join(directory, filename)
    # 어떤 덤프파일에서 문자열 변환한 것인지 표기
    with open(strings_file, 'a') as f:
        f.write('===============' + filename + '===============\n')
    str_list = re.findall(b"[A-Za-z0-9/\-:;.,_$%'!()[\]<> \#]+", open(path, "rb").read())
    with open(strings_file, "ab") as st:
        for string in str_list:
            if len(string) > min:
                logging.debug(string)
                st.write(string + "\n".encode('ascii'))
