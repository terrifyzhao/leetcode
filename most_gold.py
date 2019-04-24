# w人挖n个金矿，最多能挖多少
# https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653190796&idx=1&sn=2bf42e5783f3efd03bfb0ecd3cbbc380&chksm=8c990856bbee8140055c3429f59c8f46dc05be20b859f00fe8168efe1e6a954fdc5cfc7246b0&scene=21#wechat_redirect


def most_gold_rec(n, w, g, p):
    # 边界条件
    if n <= 1 and w < p[0]:
        return 0
    if n <= 1 and w >= p[0]:
        return g[0]

    # 如果人数不够挖最后一个矿，则不挖，某则取挖与不挖的最大值
    if w < p[n - 1]:
        return most_gold_rec(n - 1, w, g, p)
    else:
        return max(most_gold_rec(n - 1, w, g, p), most_gold_rec(n - 1, w - p[n - 1], g, p) + g[n - 1])


def most_gold_rec_dict(n, w, g, p, dic):
    if n <= 1 and w < p[0]:
        return 0
    if n <= 1 and w >= p[0]:
        return g[0]
    key = f'{n}_{w}'
    if key in dic.keys():
        return dic[key]
    else:
        if w < p[n - 1]:
            result = most_gold_rec_dict(n - 1, w, g, p, dic)
            key = f'{n}_{w - 1}'
            dic[key] = result
            return result
        else:
            res1 = most_gold_rec_dict(n - 1, w, g, p, dic)
            res2 = most_gold_rec_dict(n - 1, w - p[n - 1], g, p, dic) + g[n - 1]
            if res1 > res2:
                key = f'{n}_{w - 1}'
                dic[key] = res1
                return res1
            else:
                key = f'{n - 1}_{w - p[n - 1]}'
                dic[key] = res2
                return res2


def most_gold_bottom_top(n, w, g, p):
    result = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

    g.insert(0, 0)
    p.insert(0, 0)

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j < p[i]:
                result[i][j] = result[i - 1][j]
            else:
                result[i][j] = max(result[i - 1][j], result[i - 1][j - p[i]] + g[i])
    return result[-1][-1]


def most_gold(n, w, g, p):
    """
    :param n: 金矿数量
    :param w: 工人数量
    :param g: 每座金矿价值
    :param p: 每座金矿所需工人数
    :return: 最大价值
    """
    row_result = [0] * w

    # 初始化第一行的结果
    for i in range(w):
        if i + 1 < p[0]:
            row_result[i] = 0
        else:
            row_result[i] = g[0]

    result = row_result.copy()
    # 外层循环矿数，内层循环工人
    for i in range(n):
        for j in range(w):
            # 如果工人数少于当前矿的所需人数，则更新为原始row_result
            if j + 1 < p[i]:
                result[j] = row_result[j]
            else:
                # 如果人数够了，则考虑是采矿还是不采矿，不采则为原来的值，采则减去对应人数，然后加上对应矿的价值
                # i表示几号矿，j表示有几个人，j-p[i]表示采集i号矿之后剩下的人，g[i]表示i号矿的价值
                tmp = 0 if j - p[i] < 0 else j - p[i]
                result[j] = max(row_result[j], row_result[tmp] + g[i])
        # 更新行
        row_result = result.copy()
    # 输出最后一行最后一列的值
    return result[- 1]


n = 5
w = 10
g = [400, 500, 200, 300, 350]
p = [5, 5, 3, 4, 3]
print(str(most_gold(n, w, g, p)))
print(str(most_gold_rec(n, w, g, p)))
print(str(most_gold_rec_dict(n, w, g, p, dic={})))
print(str(most_gold_bottom_top(n, w, g, p)))
