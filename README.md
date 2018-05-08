# AndroSniffer

> Kitri Security Project
- Python 3.6+
- 시스템 환경변수 설정된 adb

## Memo
> adb로 인증 관련 데이터 가져오기
>> pull_data.py
- adb root connect
- adb pull

> 데이터를 해석해서 문자열 조합으로 Cookie 생성
>> auth_generator.py
- sqlite 라이브러리로 관련 데이터만 추출
- 추출된 데이터를 문자열로 조합해서 쿠키값 생성

> 인증 데이터 경로를 관리할 모듈
>> data_controller.py
- 리스트 형식으로 인증 데이터 경로를 보관