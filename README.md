# AndroSniffer

> Kitri Security Project
* Python 3.6+
* 시스템 환경변수 설정된 adb

## Memo
1. adb로 인증 관련 데이터 가져오기
+ adb root connect
+ adb pull
1. 데이터를 해석해서 문자열 조합으로 Cookie 생성
+ sqlite 라이브러리로 관련 데이터만 추출
+ 추출된 데이터를 문자열로 조합해서 쿠키값 생성