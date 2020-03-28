import pandas as pd


def my_quantile(s, loc):
    s = list(s)
    pos = (len(s) - 1) * loc
    a = int(pos)
    b = pos - a

    if b == 0:
        return s[a]
    else:
        return (s[a] + s[a + 1]) * b


origin = [1, 2, 3, 4, 7, 23, 78, 99, 100]
a = pd.Series(origin)

num = 0.60
sys_num = a.quantile(num)
def_num = my_quantile(a, num)


print("{} == {}".format(sys_num, def_num))
assert sys_num == def_num
