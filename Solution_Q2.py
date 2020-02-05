
def getZidShare(N, C, K):
    sid, eid = min(N), sum(N)
    while eid-sid>1:
        mid = sid + (eid-sid)//2
        pval = pts(N, C, mid)
        #print("->", mid, pval)
        if pts(N, C, mid) >= K:
            sid = mid
        else:
            eid = mid
            
    if pts(N, C, eid) >= K:
        return eid
    if pts(N, C, sid) >= K:
        return sid
    return 0

def pts(N, C, v):
    mval = float('inf')
    npts = 0
    lval = 0
    for i in range(len(N)):
        lval += N[i]
        if lval >= v and i not in C:
            mval = min(mval, lval)
            npts += 1
            lval = 0
    return npts-1

nums = input().split()
nums = [int(x) for x in nums]

temp_C = input().split()
caramels = []
no_cuts = set()
for cstr in temp_C:
    tokens = cstr.split(",")
    k1, k2 = int(tokens[0]), int(tokens[1])
    caramels.append([k1, k2])
    for kcut in range(k1, k2):
        no_cuts.add(kcut)
    
K = int(input())

print(getZidShare(nums, no_cuts, K))
