# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    array = list(map(str, numbers))
    return str(int("".join(sorted(array, key=lambda x: x*3, reverse=True))))