def most_gold_bottom_top(n, w, g, p):
    """
    :param n: 金矿数量
    :param w: 工人数量
    :param g: 每座金矿价值
    :param p: 每座金矿所需工人数
    :return: 最大价值
    """
    result = [[0 for _ in range(n + 1)] for _ in range(w + 1)]
    g.insert(0, 0)
    p.insert(0, 0)

    for i in range(1, w + 1):
        for j in range(1, n + 1):
            if i < p[j]:
                result[i][j] = result[i][j-1]
            else:
                result[i][j] = max(result[i][j-1], result[i - p[j]][j - 1] + g[j])
    return result[-1][-1]


n = 5
w = 10
g = [400, 500, 200, 300, 350]
p = [5, 5, 3, 4, 3]

print(str(most_gold_bottom_top(n, w, g, p)))
