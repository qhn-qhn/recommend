from operator import itemgetter
def recom(data,datas):
    res=[]
    # print(333)
    # print(data)
    for i in data:
        s = []
        for j in datas:
            if (i[0] == j[0]):
                s.append(i[0])
                s.append((i[1]*2+j[1])/3)
                res.append(s)
        # print(res)
    print('开始')
    n = sorted(res, key=itemgetter(1), reverse=True)
    # print(n)
    result=[]
    for j in n:
        # print(j)
        result.append(j[0])
        # print(result)
    return result