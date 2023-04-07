def Solve(N):
    # Write your code here
    # print YES if N is sum of its proper divisors else NO
    sum = 0
    for i in range(1, N):
        if N % i == 0:
            sum += i
    if sum == N:
        return "YES"
    else:
        return "NO"


T = int(input())
for _ in range(T):
    N = int(input())
    out_ = Solve(N)
    print(out_)
