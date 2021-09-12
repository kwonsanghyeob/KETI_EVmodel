import numpy as np
import matplotlib.pyplot as plt
import os


path = os.getcwd()
os.chdir('/Users/sueb4/PycharmProjects/pythonProject/KETI_EV')

Start_time = np.array([[1,3,6,10,14,16,20], [1,5,8,11,13,16,18],[1,7,9,13,19,21]])
Stop_time = np.array([[2, 5, 7, 13, 15, 19, 23], [3, 7, 10, 12, 15, 17, 19], [3, 8, 10, 18, 20, 23]])


def EV_charging_station(number_of_charger = 3, duration = 24, start_time = np.array([[1,2,3],[4,5], [5,9]]), stop_time = np.array([[2,5,4],[5,8], [7,11]]), rated_power = 50, charging_efficiency= 0.9):
    EV_charging_schedule = np.zeros([duration]).reshape(-1,1)  #0~기간
    for k in range(number_of_charger): #충전기 수
        for i in range(len(start_time[k])-1): #각 충전기의 충전시작 스케쥴 횟수
            if start_time[k][int(i)] <= stop_time[k][int(i)]:  #충전시작시간<충전종료시간
                EV_charging_schedule[int(start_time[k][i]):int((stop_time[k][i] + 1))] += rated_power*charging_efficiency #전기차 충전전력 정격50kW
    print("전력", EV_charging_schedule.reshape(-1), "총 사용 전력량", sum(EV_charging_schedule))
    return EV_charging_schedule.reshape(-1), sum(EV_charging_schedule) #전기차 충전전력 정격50kW

# 예제파일 불러와서 코드실행
Power, Energy = EV_charging_station(number_of_charger=3, duration=24, start_time=Start_time, stop_time=Stop_time)