import sys

#A = day, B = night, V = height
def snail_day(A, B, V):
    V_n = V - A #마지막 날 낮시간 동안 갈 수 있는 거리
    days = (V_n // (A-B))   #낮에가는 거리 - 밤에가는 거리만큼 하루동안 가므로 이것의 몫이 걸린 날이 된다
    days += 1   #마지막날
    if (V_n % (A-B)) != 0: # 만약 나머지 조금의 거리가 있다면 이거대로 하루를 더 추가해야하기 때문에 하루를 더 추가한다.
        days += 1
    print(days)

A, B, V = map(int, sys.stdin.readline().split())
snail_day(A,B,V)