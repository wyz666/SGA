import random
import math
import numpy as np

"""
遗传算法
@param iteratorNum 迭代次数
@param chromosomeNum 染色体数量
求三数之和最大解
可行解域 0~15
"""


# 目标函数
def target_function(solution_set):
    return pow(solution_set[1], 2) + pow(solution_set[2], 2) + pow(solution_set[0], 2)


# 解集
def target_set(list):
    deset = []
    for i in range(len(list)):
        deset.append(target_function(list[i]))
    return deset


# 轮盘
def roulette_prob_calc(list):
    list_soft = []
    list_sum = sum(list)
    temp_sum = 0
    for i in range(len(list)):
        temp_sum += list[i]
        list_soft.append(temp_sum / list_sum)
    return list_soft


# 选择下一代
def next_genaration(decode_set, roulette_prob):
    next_gen = []
    chromosomeNum = len(decode_set)
    for i in range(chromosomeNum):
        probability = random.random()
        for j in range(len(roulette_prob)):
            if probability < roulette_prob[j]:
                next_gen.append(decode_set[j])
                break
    return next_gen


# 编码
def code(solution_set):
    code_set = []
    for i in range(len(solution_set)):
        code_set.append('{:04b}'.format(solution_set[i][0]) + '{:04b}'.format(solution_set[i][1]) + '{:04b}'.format(
            solution_set[i][2]))
    return code_set


# 解码
def decode(code_set):
    decode_set = []
    for i in range(len(code_set)):
        decode_set.append([int(code_set[i][0:4], 2), int(code_set[i][4:8], 2), int(code_set[i][8:12], 2)])
    return decode_set


# 交叉（邻居、奇偶配对）
def cross(code_set):
    child_set = []
    for i in range(math.floor(len(code_set) / 2)):
        exchange_place = random.randint(1, 11)
        father = code_set[2 * i]
        mather = code_set[2 * i + 1]
        child_set.append(father[0:exchange_place] + mather[exchange_place:])
        child_set.append(mather[0:exchange_place] + father[exchange_place:])
    return child_set


# 替换字符串
def replace_str_by_index(string, start, end, sub_str):
    ret = string[: start] + sub_str + string[end:]
    return ret


# 变异
def variation(code_set, variation_rate=0.1):
    for i in range(len(code_set)):
        randval = random.random()
        if randval < variation_rate:
            variation_place = random.randint(0, 11)
            if code_set[i][variation_place] == '1':
                replace_str_by_index(code_set[i], variation_place, variation_place + 1, "0")
            else:
                replace_str_by_index(code_set[i], variation_place, variation_place + 1, "1")
    return code_set


# 遗传算法
def ga_loop(solution_set):
    code_set = code(solution_set)

    cross_set = cross(code_set)

    variation_set = variation(cross_set)

    decode_set = decode(variation_set)

    deset = target_set(decode_set)

    roulette_prob = roulette_prob_calc(deset)

    next_gen = next_genaration(decode_set, roulette_prob)

    return next_gen


# 搜索过程
def ga_search(chromosome_num, iterator_num):
    solution_set = np.random.randint(0, 16, size=[chromosome_num, 3])

    for i in range(iterator_num):
        solution_set = ga_loop(solution_set)

    return solution_set


# Python的程序入口
if __name__ == '__main__':

    solution_set = ga_search(10, 100)

    print(solution_set)
