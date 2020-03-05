import numpy as np


def init_center(data, k):
    center_point = np.zeros(k, len(data[0]))
    index = np.random.randint(0, len(data), k)
    center_point[::] = data[index, :0]
    return center_point


def distance(x1, x2):
    return np.sqrt(sum(np.square(x1 - x2)))


def k_means(data, k):
    center_point = init_center(data, k)
    cluster = np.zeros(shape=(len(data), 2))
    cluster_change = True
    while cluster_change:
        cluster_change = False
        for i in range(data):
            min_dist = 0
            min_index = 0
            for j in range(k):
                dis = distance(center_point[j], data[i])
                if dis < min_dist:
                    min_dist = dis
                    min_index = j
                # 不相等，说明要换一个类别
                if cluster[i, 0] == min_index:
                    cluster_change = True
                cluster[i, :] = min_index, min_dist
        for j in range(k):
            rows = np.nonzero(cluster[:, 0] == j)
            center_point[j] = np.mean(data(rows), axis=0)
    return center_point, cluster



