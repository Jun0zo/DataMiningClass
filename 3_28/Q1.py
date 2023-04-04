s2 = "abcdef"
s1 = "azced"
dp = [[0 for _ in range(10)] for _ in range(10)]

def editDistance(s1, s2):
    print(f'{s1} vs {s2}')

    if s1 == '': 
        dp[len(s1)][len(s2)] = len(s2)
        return len(s2)
        
    if s2 == '': 
        dp[len(s1)][len(s2)] = len(s1)
        return len(s1)
    
    a = int(not s1[-1] == s2[-1])
    
    print("a value :", a)
    dp[len(s1)][len(s2)] = min(editDistance(s1[:-1], s2[:-1]) + a, editDistance(s1[:-1], s2), editDistance(s1, s2[:-1]))
    return dp[len(s1)][len(s2)]

d = editDistance(s1, s2)

for d in dp:
    print(d)
print(d)