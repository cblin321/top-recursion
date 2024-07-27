def fibs(n):
    ans = [0, 1]
    if n < 3:
        return ans[:n]
    left = 0
    right = 1
    for i in range(3, n + 1):
        ans.append(left + right)
        left = ans[i - 2]
        right = ans[i - 1]
    return ans

def fibsRec(n):
    ans = []
    if n == 0:
        return []
    
    if n == 1:
        return [0]
    
    if n == 2:
        return [0, 1] 
    ans = fibsRec(n - 1)
    ans.append(ans[-1] + ans[-2])
    return ans
print(fibsRec(8))
print(fibs(8))
# print(fibs(0))