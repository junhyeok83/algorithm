N = int(input())  # 배열의 크기
K = int(input())  # target의 인덱스값

"""N*N 배열을 직접 만들어서 구하는 경우 제한시간을 초과로 인해 풀 수 없다.
따라서 특정 위치의 값을 찾는 알고리즘으로 binary search가 가장 잘 사용된다.
 """


def solution(K, start, end):
    while (start <= end):
        mid = (start+end)//2

        cnt = 0

        for i in range(1, N+1):
            cnt += min(mid//i, N)

        if cnt >= K:
            end = mid-1
        else:
            start = mid+1
    return start


print(solution(K, 1, N*N))
