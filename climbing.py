def clib(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return clib(n - 1) + clib(n - 2)


def clib2(n, dic):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in dic.keys():
        return dic[n]
    else:
        result = clib2(n - 1, dic) + clib2(n - 2, dic)
        dic[n] = result
        return result


def clib_dp(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    a = 1
    b = 2
    tmp = 0
    for i in range(3, n + 1):
        tmp = a + b
        a = b
        b = tmp
    return tmp


if __name__ == '__main__':
    print(clib(10))
    print(clib2(10, dic={}))
    print(clib_dp(10))
