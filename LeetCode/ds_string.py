# case1
def simple_matching(string, sub):
    len_str = len(string)
    len_sub = len(sub)
    if len_str < len_sub:
        return -1
    for i in range(len_str-len_sub+1):
        for j in range(len_sub):
            if sub[j] == string[i+j]:
                j += 1
            else:
                break
            if j == len_sub:
                return i
        i += 1
    return -1

# if __name__ == '__main__':
#     string = 'shanghai'
#     sub = 'hai'
#     res = simple_matching(string, sub)
#     print(res)

# case2, kmp
def get_next(sub):
    length = len(sub)
    res = [0] * (length+1)
    res[0], res[1] = -1, 0
    i = 1  # 后缀单个字符
    j = 0  # 前缀单个字符
    while i < length:
        if j == 0 or sub[i-1] == sub[j-1]:
            i += 1
            j += 1
            res[i] = j
        else:
            j = res[j]  # 字符不同，j回溯
    return res

def get_nextval(sub):
    length = len(sub)
    res = [0] * (length+1)
    res[0], res[1] = -1, 0
    i = 1  # 后缀单个字符
    j = 0  # 前缀单个字符
    while i < length:
        if j == 0 or sub[i-1] == sub[j-1]:
            i += 1
            j += 1
            if sub[i-1] != sub[j-1]:
                res[i] = j
            else:
                res[i] = res[j]
        else:
            j = res[j]  # 字符不同，j回溯
    return res

def kmp(string, sub):
    len_str = len(string)
    len_sub = len(sub)
    i, j = 1, 1
    matching_num = 0
    next_j = get_next(sub)
    # next_j = get_nextval(sub)  # improved kmp
    while i < len_str and j < len_sub:
        matching_num += 1
        if string[i-1] == sub[j-1]:
            i += 1
            j += 1
        elif j != 0:  # 模式串游标没有退到最前面
            j = next_j[j]
        else:
            i += 1
            j += 1

    if j == len_sub:
        return i-j, matching_num
    else:
        return -1, matching_num

# if __name__ == '__main__':
#     string = 'shainghaiaishang'
#     sub = 'aiais'
#     index, num = kmp(string, sub)
#     print('index, num', index, num)

# case3, sunday
def get_shift_matrix(sub):
    dic = {}
    for i in range(len(sub)-1, -1, -1):
        if not dic.get(sub[i]):
            dic[sub[i]] = len(sub) - i
    dic['ot'] = len(sub) + 1
    return dic

def sunday(string, sub):
    len_str = len(string)
    len_sub = len(sub)
    dic = get_shift_matrix(sub)
    i = 0
    matching_num = 0
    while i + len_sub <= len_str:
        matching_num += 1
        ref = string[i: i+len_sub]
        if ref == sub:
            return i, matching_num
        else:
            if i + len_sub >= len_str:
                return -1, matching_num
            curr_s = string[i+len_sub]
            if dic.get(curr_s):
                i += dic[curr_s]
            else:
                i += dic['ot']
    return -1, matching_num

# if __name__ == '__main__':
#     string = 'shainghaiaishang'
#     sub = 'aiais'
#     index, num = sunday(string, sub)
#     print('index, num', index, num)




