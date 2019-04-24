# w人挖n个金矿，最多能挖多少
# https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653190796&idx=1&sn=2bf42e5783f3efd03bfb0ecd3cbbc380&chksm=8c990856bbee8140055c3429f59c8f46dc05be20b859f00fe8168efe1e6a954fdc5cfc7246b0&scene=21#wechat_redirect

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
    for i in range(1, n):
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
