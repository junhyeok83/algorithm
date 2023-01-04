from math import sqrt
x, y, c = map(float, input().split())

start, end = 0, min(x, y)


def find_c(mid):
    h1 = sqrt(x**2-mid**2)
    h2 = sqrt(y**2-mid**2)
    return h1*h2/(h1+h2)


result = 0
while end-start > 1e-6:
    mid = (start+end)/2
    if find_c(mid) >= c:
        result = mid
        start = mid
    else:
        end = mid

print(round(result, 3))
