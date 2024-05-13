import pyautogui
import time


# print(pyautogui.size())

# time.sleep(3)

# print(pyautogui.position())

f_time_short = 1

f_time_long = 4

cnt = 0

criteria_cnt = 518

start_time = time.time()

while cnt < criteria_cnt : 

    if cnt != 0 : 
        time.sleep(f_time_long)

        win = pyautogui.getWindowsWithTitle("Adobe Audition")[0]

        win.activate()

        time.sleep(f_time_short)

    # 파일 선택 영역 스크롤 후 클릭
    pyautogui.moveTo(260,235)
    time.sleep(f_time_short)

    if cnt != 0 : 

        pyautogui.scroll(-400)

    time.sleep(f_time_short)
    pyautogui.doubleClick()

    # 시작 영역 클릭
    pyautogui.moveTo(1650,928)
    time.sleep(f_time_short)
    pyautogui.click()
    time.sleep(f_time_short)
    pyautogui.typewrite('6')
    time.sleep(f_time_short)
    pyautogui.press('enter')

    # 끝 영역 클릭
    pyautogui.moveTo(1750,925)
    time.sleep(f_time_short)
    pyautogui.click()
    time.sleep(f_time_short)
    pyautogui.typewrite('14')
    time.sleep(f_time_short)
    pyautogui.press('enter')
    time.sleep(f_time_short)

    # 선택 영역 스캔 클릭
    pyautogui.moveTo(1185,807)
    time.sleep(f_time_short)
    pyautogui.click()
    time.sleep(f_time_short)

    # 최소 RMS 클릭 or 최대 RMS 클릭
    # pyautogui.moveTo(1466,463)  # 최소
    pyautogui.moveTo(1466,440)  # 최대
    time.sleep(f_time_short)
    pyautogui.click()
    time.sleep(f_time_short)

    # 복사 클릭
    pyautogui.moveTo(1217,747)
    time.sleep(f_time_short)
    pyautogui.click()
    time.sleep(f_time_long/2)

    # 창 전환
    win = pyautogui.getWindowsWithTitle("최대 데시벨")[0]

    win.activate()

    time.sleep(f_time_long)

    # 엑셀 클릭
    pyautogui.moveTo(1906,947)
    time.sleep(f_time_short)
    pyautogui.click(clicks=1)
    time.sleep(f_time_short)
    pyautogui.moveTo(186,315)
    time.sleep(f_time_short)
    pyautogui.click()
    time.sleep(f_time_short)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(f_time_short)
    pyautogui.hotkey('ctrl', 's')  # 저장
    time.sleep(f_time_short)

    print(str(cnt+1)+"번째 실행")

    pyautogui.moveTo(3867,1650)
    
    time.sleep(f_time_short)
    
    pyautogui.click()

    cnt += 1

    # ss = input("끝내려면 q를 눌러주세요.")

    # if ss == 'q' : 
    #     break


end_time = time.time()

time_diff = round((end_time - start_time) / 60, 2)

print("실행 시간 = ",time_diff,"분")
