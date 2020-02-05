

def getMaxTransfer(emap, elist):
    total_transfer = 0
    if "USD" not in emap:
        return 0

    fmap = dict()
    for i in range(len(elist)):
        fmap[(elist[i][0], elist[i][1])] = elist[i][3]
    
    for vdata in emap["USD"]:
        #print("->", vdata)
        vcurr, vrate, trLimit = vdata
        pq = [(vcurr, vrate*trLimit)]
        vmap = set()
        vmap.add("USD")
        #vmap.add(vcurr)
        while len(pq) > 0:
            kcurr, kinLimit = pq.pop()
            vmap.add(kcurr)
            if kcurr == "SGD":
                total_transfer += kinLimit
                continue
            if kcurr not in emap:
                continue
            for kvdata in emap[kcurr]:
                if kvdata[0] in vmap or fmap[(kcurr, kvdata[0])] <= 0:
                    continue
                amt_trs = min(kinLimit, kvdata[2], fmap[kcurr, kvdata[0]]) 
                fmap[(kcurr, kvdata[0])] -= amt_trs
                pq.append((kvdata[0], amt_trs * kvdata[1]))

    return round(total_transfer)

N = int(input())
emap = dict()
elist = []
for i in range(N):
    tokens = input().split(",")
    from_curr, to_curr, erate, trLimit = tokens[0].upper(), tokens[1].upper(), float(tokens[2]), float(tokens[3])
    if from_curr not in emap:
        emap[from_curr] = []
    emap[from_curr].append((to_curr, erate, trLimit))
    elist.append((from_curr, to_curr, erate, trLimit))

print(getMaxTransfer(emap, elist))
    

            
        


    
