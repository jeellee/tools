def func():
    m = int(input().strip())
    n = int(input().strip())
    arry_l = []
    for i in range(n):
        arry_l.append(list(map(int, input().strip().split(","))))
    # print(arry_l)
    new_array = []
    #     left_array = []
    while arry_l:
        arry_i = arry_l.pop(0)
        if len(arry_i) < m:
            new_array.extend(arry_i)
        else:
            new_array.extend(arry_i[:m])
            arry_l.append(arry_i[m:])

    print(",".join([str(i) for i in new_array]))


def func2():
    # s_l = list(input().strip())
    s_l = "mMbbMccbc"  # mMbbMccbc
    map_s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    stack = []
    is_pop = ""
    # mMbccbc
    for s in s_l:
        if s not in map_s:
            print(0)
            return
        if s == is_pop:
            continue
        if stack:
            top = stack[-1]
            if top == s:
                stack.pop()
                is_pop = s
            else:
                stack.append(s)
                is_pop = ""
        else:
            stack.append(s)
            is_pop = ""
    print(len(stack))


"""
露营问题
2 1 1 1 2
0 1 1 3 0
0 1 1 3 0
0 0 0 0 0
"""




























"""
numbers = [2 7 11 15]  target=9
输出： [1, 2]

"""


def func5():
    while True:
        try:
            numbers = list(map(int, input().strip().split()))
            target = int(input().strip())
            for i in range(len(numbers)):
                for j in range(i+1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                        print(i+1, j+1)
        except:
            break

if __name__ == "__main__":
    # func2()
    func5()
