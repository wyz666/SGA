def replace_str_by_index(string, start, end, sub_str):
    ret = string[: start] + sub_str + string[end:]
    return ret

if __name__ == '__main__':
    string = 'bode11222'
    sub_str = '33'
    start = 4
    end = 6

    # ret = string[: start] + sub_str + string[end: ]
    ret = replace_str_by_index(string, start, end, sub_str)
    print(ret)