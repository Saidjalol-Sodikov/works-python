# N = int(input())
# kor = list()

# for i in range(N):
#     d = 0
#     for j in range(1, i):
#         if i % j == 0:
#             d += j                 
#     kor.append(tuple([i,d]))     

# print(kor)

# for i in range(len(kor)):
#     for j in range(i, len(kor)):
#         if i !=j and kor[i][0] == kor[j][1] and kor[i][1] == kor[j][0]:
#             print(kor[i])

k = 10000


def sum_of_dividors(n):
    s = 0
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            s += k
    return s

for i in range(1, k + 1):
    j = sum_of_dividors(i)
    if i < j <= k and i == sum_of_dividors(j):
        print(i, j)