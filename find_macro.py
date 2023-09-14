import re
import csv
import os

print("본 파이썬 파일은 .txt 형식의 C 언어 코드에서")
print("\'#define\'으로 정의된 매크로 함수를 추출하는 코드입니다.")
print("(별도로 설치해야하는 라이브러리는 없습니다.)")
print("(Python 3.11 버전에서 작성됐습니다.)")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

openFile = str(input("매크로 함수를 추출할 파일명(혹은 파일 경로)를 입력하세요 : "))
saveFile = str(input("저장할 파일명(혹은 파일 경로)를 입력하세요 : "))

# 결과를 저장할 빈 리스트를 생성합니다.
define_statements = []
define_name = []

# open할 파일을 읽기 모드로 엽니다.
with open(openFile, 'r') as file:
    # 파일을 한 줄씩 읽어옵니다.
    lines = file.readlines()
    # 읽어온 파일을 iterator 객체로 변환합니다.
    lines_iter = iter(lines)

    # 라인을 하나씩 조사합니다.
    for line in lines_iter:
        # 만약 라인이 '#define'으로 시작하면 이 라인을 저장합니다.
        if line.lstrip().startswith('#define'):
            statement = line

            # 매크로명 저장 과정
            s = line.split()[1]

            # 한 줄에 입력된 매크로라면
            if s.endswith(")") : 
                p = re.compile(r"(.*?)\(.*?\)")
                s = p.findall(s)[0]

            define_name.append(s)
            # '\n'로 끝나는 문장이면 다음 라인도 추가합니다.
            if line.endswith('\\\n'):
                try : 
                    # next로 iterator의 다음 요소를 불러옵니다.
                    next_line = next(lines_iter)
                    statement += next_line
                except StopIteration: 
                    break

            # statement = statement.strip()
            define_statements.append(statement)

# 매크로 이름과 매크로 함수를 zip
lists = zip(define_name,define_statements)

with open(saveFile, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    
    # 첫 번째 리스트 쓰기
    writer.writerow(["매크로명", "매크로설명"])
    
    for z in lists : 
    # zip 요소를 .csv에 추가
        writer.writerow(z)

# 저장 경로에 존재하는 파일과 디렉토리를 리스트로 저장

dir_split = saveFile.split("/")

dir_nonfile = saveFile.replace(dir_split[-1],"")

listDir = os.listdir(dir_nonfile)

if dir_split[-1] in listDir : 
    print("파일이 성공적으로 저장됐습니다.")

exit()