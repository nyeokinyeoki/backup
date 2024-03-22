import os
import re

file_path = str(input("파일명(혹은 파일 경로)를 입력하세요 : "))
extension = str(input("확장자를 입력하세요(예시 : .png) : "))

# sample_rate 리스트
sample_rate = ["임의의 sample"]

regexp = re.compile(r"(?<=:\\).+")  # :\ 뒤로 후방탐색

# 경로에 있는 파일을 리스트로
list_start_path = os.listdir(file_path)

list_file_path = []

cnt = 1

for path, dir, files in os.walk(file_path) :  # 하위 디렉토리 전부 탐색

    # dir는 비어있고, path랑 files는 비어있지 않을 때
    if not dir and path and files : 

        list_file_path.append(path)


std_bit = 0

for path_ in list_file_path : 

    path_reg = regexp.findall(path_)[0]
    
    change_path = re.sub(r"\\", "_", path_reg)  # \를 _로

    lists_path_ = os.listdir(path_)

    sorted_files = sorted(lists_path_, key=lambda x: int(x.split('tek')[1].split('.')[0]))

# 정렬된 파일 출력
    # print(sorted_files)

    # filelist = [s for s in lists_path_ if os.path.isfile(os.path.join(path_, s))]

    # filelist.sort(key=lambda s: os.path.getctime(os.path.join(path_, s)))  # 생성한 날짜 순으로 정렬


    r_cnt = 1

    for rate in sample_rate : 

        bit_width0 = ["임의의 bit"]
        bit_width1 = ["임의의 bit"]
        bit_width2 = ["임의의 bit"]

        bit_width = globals()["bit_width"+str(std_bit % 3)]

        length_bits = len(bit_width)
        b_cnt = len(bit_width)

        for bit in bit_width :

            try :                  
                multi_len = length_bits * r_cnt - b_cnt
                src = os.path.join(path_, sorted_files[multi_len])
                print(src)
                dst = change_path+"_"+str(rate)+"_"+str(bit)+extension
                dst = os.path.join(path_, dst)
                os.rename(src, dst)   # 원래 파일을 지정한 파일명으로 변경(dst)

                print(str(cnt)+"번째 성공!")

                b_cnt -= 1

                cnt += 1

            except : 
                pass
        
        r_cnt += 1

    std_bit += 1

