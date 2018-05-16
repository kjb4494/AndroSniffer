# AndroSniffer
> Kitri Security Project

## 구동 조건
- Python 3.6+
- 시스템 환경변수 설정된 adb

## 모듈 구조
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
- 리스트 형식으로 인증 파일 경로를 보관
- 각 앱별 분석시 필요한 변수 템플릿(딕셔너리 형식)을 보관

> 분석 방식이 다른 예외적인 앱에 대한 처리를 위한 패키지
>> except_data_pac
>>> first_branch.py  
>>> _앱이름.py
- first_branch.py는 프로세스 진행 중 첫번째로 예외처리가 진행될 분기점이다.
- _앱이름.py에서 해당 앱에 대한 처리를 독립적인 모듈로 수행한다.

## 유지보수
> 일반적인 앱 추가 시 수정항목
- data_controller.py의 data_list 리스트에 앱의 인증파일 경로 추가.
- data_controller.py의 search_db 함수에 앱의 인증에 유효한 데이터를 추출하는데 필요한 변수 추가
> 예외적인 분석이 필요한 앱 추가 시 수정항목
- data_controller.py의 data_list 리스트 및 data_exception_list 리스트에 앱의 인증파일 경로 추가.
- except_data_pac 패키지의 first_branch에 elif문 추가
- except_data_pac 패키지에 _앱이름.py을 추가하여 data_extract 함수에 분석 알고리즘 작성

## 분석 가능한 앱
- 다음
- 네이트
- 네이버
- 페이스북

## 분석 계획 중인 앱
- 트위터
- 인스타

## 메모
- 페이스북  
페이스북 앱의 인증 데이터를 찾는데 성공했지만 페이스북 라이트에서는 저장소 경로가 다르다. 동적 분석으로 추적을 시도했지만 진척이 없다.

- 트위터  
분석 예정