from collections import deque


class Solution(object):
    def simplifyPath2(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = deque()
        i = 0
        l = len(path)
        while i < l:
            if path[i] == '/':
                if len(stack) > 0 and stack[len(stack) - 1] == '/':
                    i += 1
                else:
                    stack.append(path[i])
                    i += 1
            elif path[i] == '.':
                j = i
                tmp = '.'
                while j + 1 < l and path[j + 1] != '/':
                    j += 1
                    tmp += path[j]
                if j == i:
                    i += 1
                elif j == i + 1:
                    if len(stack) > 1:
                        stack.pop()
                    while len(stack) > 1 and stack[len(stack) - 1] != '/':
                        stack.pop()
                    i = j + 1
                else:
                    for c in tmp:
                        stack.append(c)
                    i = j + 1

            else:
                stack.append(path[i])
                i += 1

        while len(stack) > 1 and stack[len(stack) - 1] == '/':
            stack.pop()

        return ''.join(list(stack))

    def simplifyPath(self, path: str) -> str:
        r = []
        for s in path.split('/'):
            r = {'': r, '.': r, '..': r[:-1]}.get(s, r + [s])
        return '/' + '/'.join(r)


a = Solution().simplifyPath("/a/../../b/../c//.//")
print(a)
