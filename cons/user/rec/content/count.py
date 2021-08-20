def count(userdatas,schmajdatas):
    us = len(userdatas)
    sm = len(schmajdatas)
    result = []
    for j in range(1,sm):
        s=0
        m=0
        line = []
        line.append(schmajdatas[j][0])
        for i in range(1,us):
            a=schmajdatas[j][i]*userdatas[i]
            # 分子
            s=a+s
            b = (schmajdatas[j][i]*schmajdatas[j][i])**0.5
            c = (userdatas[i]*userdatas[i])**0.5
            # 分母
            m = b + c + m
        # 相似度计算结果
        res = s/m
        if (res>0.2):
            line.append(res)
            result.append(line)
    return(result)