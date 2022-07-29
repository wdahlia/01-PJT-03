import sys

sys.stdin = open("_암호문1.txt")

# 11개 이거는 리스트의 길이임
# 근데 I 뒤에 있는 x의 값은 인덱스임 그다음 y개의 숫자는 y개를 넣으라는 소린데
# 만약 y개를 다 채우지 못하고 다른 I 삽입문의 x 인덱스가 있는경우에는 그 삽입문의 암호를 넣어주는것

while range(11):
    origin_len = int(input())
    origin_text = list(map(int, input().split()))
    N = int(input())
    command_text = input().split('I')

    command_dict = {}
    for c in command_text:
        c = c.split()
        if len(c) == 0:
            pass
        else:
            command_dict[int(c[0])] = c[2:]