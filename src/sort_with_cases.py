
import random

# b,c,a = (3,-4,5) a>b>c


def fill_template(a,b,c):
    return f"""
問題: {b}, {c}, x, {a} を大きい順に並び替える。ただし、x は未知数とする。

考え方:未知数xの値によって、数列の並び方が変わる。そこで、xの取りうる範囲によって場合分けを行い、それぞれの場合で最大値から最小値へと並べ替える。

解答：

場合分け:

x > {a} の場合:

x が最も大きいので、他の数はすべてxよりも小さい。
並び替え: x, {a}, {b}, {c}

{a} > x > {b} の場合:

{a} が最大、x が2番目に大きい。
並び替え: {a}, x, {b}, {c}

{b} > x > {c} の場合:

{a} が最大、{b} が2番目に大きい。
並び替え: {a}, {b}, x, {c}

x < {c} の場合:

{a} が最大、{b} が2番目に大きい。
並び替え: {a}, {b}, {c}, x

まとめ:

xの値によって、以下の並び方が考えらる。

x > {a} の場合：x, {a}, {b}, {c}
{a} > x > {b} の場合：{a}, x, {b}, {c}
{b} > x > {c} の場合: {a}, {b}, x, {c}
x < {c} の場合：{a}, {b}, {c}, x
"""

def gen_sort_with_cases():
    a_domains = [-i for i in range(1000)]+[i for i in range(1000)]
    b_domains = [-i for i in range(1000)]+[i for i in range(1000)]
    c_domains = [-i for i in range(1000)]+[i for i in range(1000)]

    random.shuffle(a_domains)
    random.shuffle(b_domains)
    for a in a_domains:
        for b in [x for x in b_domains if a>x]:
            for c in [x for x in c_domains if a>b>x]:
                return (fill_template(a,b,c))

            