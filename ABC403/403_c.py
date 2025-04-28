n,m,q=map(int,input().split())
query=[]
for i in range(q):
    query.append(list(map(int,input().split())))

view=[[] for _ in range(n)]

for i in range(q):
    if query[i][0]==1:
        #XにYを付与
        if query[i][2] not in view[query[i][1]-1]:
            view[query[i][1]-1].append(query[i][2])
        else:
            pass
    elif query[i][0]==2:
        #Xにすべて付与
        view[query[i][1]-1].append("all")
    else:
        #XがY見れるか答える
        if ("all" in view[query[i][1]-1]) or (query[i][2] in view[query[i][1]-1]):
            print("Yes")
        else:
            print("No")


