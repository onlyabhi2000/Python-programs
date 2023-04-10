def nsr(n):
    if n <= 1:
        return n
    return n + recurSum(n - 1)
  
# Driver code
n = 5
print(nsr(n))