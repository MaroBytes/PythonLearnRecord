n = int(input())
sum2 = 0
for i in range(1, n+1, 2):
    sum1 = 1
    for j in range(1, i+1):
        sum1 *= j
    sum2 += sum1
print(sum2)
eval