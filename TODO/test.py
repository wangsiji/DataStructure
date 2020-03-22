# -*- coding: utf-8 -*-
# @Time    : 2020/03/20 9:30 下午
# @Author  : siJi
# @File    : test.py
# @Desc    :

def main(t, CF, rf, MV):
    import sympy
    # 申明未知数spread
    spread = sympy.symbols("spread")
    sum = 0
    for i in range(1, t + 1):
        sum += CF[i - 1] / ((1 + rf[i - 1] + spread) ** (i / 12)) -MV[i-1]
    res = sympy.solve([sum-0], [spread])
    return res


if __name__ == "__main__":
    t = 2
    CF = [1,0,0]
    rf = [6,0,2]
    MV = [1,0,1]
    print(main(t, CF, rf, MV))
