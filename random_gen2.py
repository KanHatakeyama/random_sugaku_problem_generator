from tqdm import tqdm
import datetime
import json
import os
import random
import math

# 方程式問題の生成関数


def generate_equation_problem():
    x = random.randint(1, 20)
    c = random.randint(1, 50)
    problem = f"方程式を解きなさい: {x}x + {c} = 0"
    solution_steps = [
        f"{x}x + {c} = 0",
        f"{x}x = -{c}",
        f"x = {-c/x}"
    ]
    return problem, solution_steps

# 比と割合問題の生成関数


def generate_ratio_problem():
    p = random.randint(1, 100)
    q = random.randint(1, 100)
    problem = f"{p}の{q}%は？"
    solution_steps = [
        f"{p}の{q}% = {p} × {q}/100",
        f"{p} × {q}/100 = {round(p * q / 100, 2)}"
    ]
    return problem, solution_steps

# 面積と体積問題の生成関数


def generate_area_volume_problem():
    l = random.randint(1, 20)
    w = random.randint(1, 20)
    h = random.randint(1, 20)
    problems = [
        (f"長方形の面積は?: 縦{l}cm, 横{w}cm", [
            f"面積 = 縦 × 横",
            f"面積 = {l} × {w}",
            f"面積 = {l * w} cm²"
        ]),
        (f"立方体の体積は?: 一辺{h}cm", [
            f"体積 = 一辺³",
            f"体積 = {h}³",
            f"体積 = {h ** 3} cm³"
        ]),
        (f"円の面積は?: 半径{l}cm", [
            f"面積 = π × 半径²",
            f"面積 = π × {l}²",
            f"面積 ≈ {round(3.14 * l ** 2, 2)} cm²"
        ]),
        (f"円柱の体積は?: 半径{l}cm, 高さ{h}cm", [
            f"体積 = π × 半径² × 高さ",
            f"体積 = π × {l}² × {h}",
            f"体積 ≈ {round(3.14 * l ** 2 * h, 2)} cm³"
        ])
    ]
    return random.choice(problems)


# 三角形問題の生成関数
def generate_triangle_problem():
    while True:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = random.randint(1, 20)
        if a + b > c and a + c > b and b + c > a:
            break
    problem = f"三角形の辺の長さが {a}cm, {b}cm, {c}cm の場合の面積を求めなさい"
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    solution_steps = [
        f"ヘロンの公式を使用",
        f"s = ({a} + {b} + {c}) / 2 = {s}",
        f"面積 = √(s(s - a)(s - b)(s - c))",
        f"面積 ≈ {round(area, 2)} cm²"
    ]
    return problem, solution_steps

# 他の問題の生成関数


def generate_other_problem():
    problems = []

    # 比例と反比例の問題
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    problems.append((f"比例 y = 3x のとき、x = {x} のときの y を求めなさい", [
        f"y = 3 × {x}",
        f"y = {3 * x}"
    ]))

    problems.append((f"反比例 y = 24/x のとき、x = {x} のときの y を求めなさい", [
        f"y = 24 / {x}",
        f"y = {24 / x}"
    ]))

    # 正負の数の計算問題
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    problems.append((f"{a} + {b} の計算結果を求めなさい", [
        f"{a} + {b} = {a + b}"
    ]))

    problems.append((f"{a} - {b} の計算結果を求めなさい", [
        f"{a} - {b} = {a - b}"
    ]))

    # 平均の問題
    numbers = [random.randint(1, 100) for _ in range(5)]
    problem = f"{numbers} の平均を求めなさい"
    mean = sum(numbers) / len(numbers)
    problems.append((problem, [
        f"合計 = {sum(numbers)}",
        f"平均 = 合計 / 数 = {sum(numbers)} / {len(numbers)}",
        f"平均 ≈ {round(mean, 2)}"
    ]))

    return random.choice(problems)


def generate_lottery_probability_problem():
    total_tickets = random.randint(50, 100)
    winning_tickets = random.randint(1, total_tickets // 2)
    problem = f"{total_tickets}枚のくじの中から{winning_tickets}枚が当たりのとき、1枚引いて当たる確率は？"
    probability = winning_tickets / total_tickets
    solution_steps = [
        f"くじの総数は{total_tickets}枚です。",
        f"そのうち、当たりは{winning_tickets}枚です。",
        f"当たりの確率は{winning_tickets}/{total_tickets}です。",
        f"確率 = {round(probability, 2)}"
    ]
    return problem, solution_steps


def generate_card_probability_problem():
    total_cards = 52  # 標準デッキ
    card_types = {
        "絵札": 12,  # Jack, Queen, King of each suit
        "エース": 4,  # Aces
        "ハートのカード": 13,  # One suit
        "スペードのカード": 13,  # One suit
        "クラブのカード": 13,  # One suit
        "ダイヤのカード": 13,  # One suit
        "赤いカード": 26,  # Hearts and Diamonds
        "黒いカード": 26,  # Spades and Clubs
        "偶数のカード": 20,  # 2, 4, 6, 8, 10 of each suit
        "奇数のカード": 16  # 1, 3, 5, 7, 9 of each suit
    }

    card_type, count = random.choice(list(card_types.items()))
    problem = f"トランプのデッキ（{total_cards}枚）から1枚引いたとき、{card_type}が出る確率は？"
    probability = count / total_cards

    solution_steps = [
        f"トランプのデッキには合計{total_cards}枚のカードがあります。",
        f"そのうち、{card_type}は{count}枚です。",
        f"{card_type}が出る確率は{count}/{total_cards}です。",
        f"確率 = {round(probability, 2)}"
    ]
    return problem, solution_steps


def generate_parallelogram_area_problem():
    base = random.randint(1, 20)
    height = random.randint(1, 20)
    problem = f"底辺が{base}cm、高さが{height}cmの平行四辺形の面積を求めなさい。"
    area = base * height
    solution_steps = [
        f"面積 = 底辺 × 高さ",
        f"面積 = {base}cm × {height}cm",
        f"面積 = {area}cm²"
    ]
    return problem, solution_steps


def generate_trapezoid_area_problem():
    base1 = random.randint(1, 20)
    base2 = random.randint(1, 20)
    height = random.randint(1, 20)
    problem = f"上底が{base1}cm、下底が{base2}cm、高さが{height}cmの台形の面積を求めなさい。"
    area = ((base1 + base2) * height) / 2
    solution_steps = [
        f"面積 = (上底 + 下底) × 高さ / 2",
        f"面積 = ({base1}cm + {base2}cm) × {height}cm / 2",
        f"面積 = {(base1 + base2) * height} / 2",
        f"面積 = {area}cm²"
    ]
    return problem, solution_steps


def generate_equation_transformation_problem():

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    problem = f"{a}x + {b} = {c} を x について解きなさい。"
    solution_steps = [
        f"{a}x + {b} = {c}",
        f"{a}x = {c} - {b}",
        f"x = ({c} - {b}) / {a}",
        f"x = {round((c - b) / a, 2)}"
    ]
    return problem, solution_steps


def generate_quadratic_equation_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    problem = f"二次方程式 {a}x² + {b}x + {c} = 0 の解を求めなさい。"
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        solution_steps = [
            f"{a}x² + {b}x + {c} = 0",
            f"判別式 = b² - 4ac = {b}² - 4×{a}×{c}",
            f"判別式 = {discriminant}",
            f"実数解は存在しません。"
        ]
    else:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        solution_steps = [
            f"{a}x² + {b}x + {c} = 0",
            f"判別式 = b² - 4ac = {b}² - 4×{a}×{c}",
            f"判別式 = {discriminant}",
            f"x = (-b ± √判別式) / 2a",
            f"x1 = ({-b} + √{discriminant}) / 2×{a} = {round(x1, 2)}",
            f"x2 = ({-b} - √{discriminant}) / 2×{a} = {round(x2, 2)}"
        ]
    return problem, solution_steps


def generate_right_triangle_hypotenuse_problem():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    problem = f"直角三角形の一辺が{a}cm、もう一辺が{b}cmのとき、斜辺の長さを求めなさい。"
    hypotenuse = (a**2 + b**2) ** 0.5
    solution_steps = [
        f"斜辺の長さはピタゴラスの定理を使って計算します。",
        f"斜辺の長さ² = 一辺の長さ² + もう一辺の長さ²",
        f"斜辺の長さ² = {a}² + {b}²",
        f"斜辺の長さ² = {a**2} + {b**2}",
        f"斜辺の長さ = √({a**2} + {b**2})",
        f"斜辺の長さ ≈ {round(hypotenuse, 2)}cm"
    ]
    return problem, solution_steps


def generate_circle_circumference_problem():
    radius = random.randint(1, 20)
    problem = f"半径が{radius}cmの円の周の長さを求めなさい。"
    circumference = 2 * 3.14 * radius
    solution_steps = [
        f"円の周の長さは次の公式で計算できます。",
        f"周の長さ = 2 × π × 半径",
        f"周の長さ = 2 × 3.14 × {radius}cm",
        f"周の長さ ≈ {round(circumference, 2)}cm"
    ]
    return problem, solution_steps


def generate_similar_figures_area_ratio_problem():
    ratio = random.randint(1, 5)
    problem = f"相似な二つの図形の相似比が {ratio} : 1 のとき、面積比を求めなさい。"
    area_ratio = ratio ** 2
    solution_steps = [
        f"相似な図形の面積比は相似比の2乗です。",
        f"面積比 = {ratio}² : 1²",
        f"面積比 = {area_ratio} : 1"
    ]
    return problem, solution_steps


def generate_cube_diagonal_length_problem():
    side_length = random.randint(1, 20)
    problem = f"一辺の長さが{side_length}cmの立方体の対角線の長さを求めなさい。"
    diagonal_length = (3 * side_length**2) ** 0.5
    solution_steps = [
        f"立方体の対角線の長さは次の公式で計算できます。",
        f"対角線の長さ = √(3 × 一辺の長さ²)",
        f"対角線の長さ = √(3 × {side_length}²)",
        f"対角線の長さ = √({3 * side_length**2})",
        f"対角線の長さ ≈ {round(diagonal_length, 2)}cm"
    ]
    return problem, solution_steps


def generate_cone_volume_problem():
    radius = random.randint(1, 20)
    height = random.randint(1, 20)
    problem = f"半径が{radius}cm、高さが{height}cmの円錐の体積を求めなさい。"
    volume = (1/3) * 3.14 * radius**2 * height
    solution_steps = [
        f"円錐の体積は次の公式で計算できます。",
        f"体積 = (1/3) × π × 半径² × 高さ",
        f"体積 = (1/3) × 3.14 × {radius}² × {height}",
        f"体積 ≈ {round(volume, 2)}cm³"
    ]
    return problem, solution_steps


def generate_system_of_equations_problem():
    a1, b1, c1 = random.randint(1, 10), random.randint(
        1, 10), random.randint(1, 20)
    a2, b2, c2 = random.randint(1, 10), random.randint(
        1, 10), random.randint(1, 20)
    problem = f"次の連立方程式を解きなさい。\n{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}"

    # 解の計算
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        solution_steps = [
            f"連立方程式：",
            f"{a1}x + {b1}y = {c1}",
            f"{a2}x + {b2}y = {c2}",
            f"この連立方程式には解がありません。"
        ]
    else:
        x = (c1 * b2 - c2 * b1) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        solution_steps = [
            f"連立方程式：",
            f"{a1}x + {b1}y = {c1}",
            f"{a2}x + {b2}y = {c2}",
            f"行列式を計算します。",
            f"行列式 = {a1} * {b2} - {a2} * {b1} = {determinant}",
            f"x = ({c1} * {b2} - {c2} * {b1}) / {determinant} = {round(x, 2)}",
            f"y = ({a1} * {c2} - {a2} * {c1}) / {determinant} = {round(y, 2)}"
        ]
    return problem, solution_steps


def generate_circle_equation_problem():
    h = random.randint(-10, 10)
    k = random.randint(-10, 10)
    r = random.randint(1, 10)
    problem = f"中心が({h}, {k})、半径が{r}の円の方程式を求めなさい。"
    solution_steps = [
        f"円の方程式は次の形式です。",
        f"(x - h)² + (y - k)² = r²",
        f"h = {h}, k = {k}, r = {r}",
        f"よって、方程式は (x - {h})² + (y - {k})² = {r**2}"
    ]
    return problem, solution_steps


def generate_quadratic_vertex_problem():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    problem = f"二次関数 y = {a}x² + {b}x + {c} の頂点の座標を求めなさい。"
    h = -b / (2 * a)
    k = a * h**2 + b * h + c
    solution_steps = [
        f"二次関数の頂点の座標 (h, k) は次の公式で計算します。",
        f"h = -b / 2a = {-b} / 2×{a} = {round(h, 2)}",
        f"k = a(h)² + b(h) + c = {a}({round(h, 2)})² + {b}({round(h, 2)}) + {c} = {round(k, 2)}",
        f"頂点の座標は ({round(h, 2)}, {round(k, 2)})"
    ]
    return problem, solution_steps


def generate_cylinder_surface_area_problem():
    radius = random.randint(1, 20)
    height = random.randint(1, 20)
    problem = f"半径が{radius}cm、高さが{height}cmの円柱の表面積を求めなさい。"
    surface_area = 2 * 3.14 * radius * (radius + height)
    solution_steps = [
        f"円柱の表面積は次の公式で計算できます。",
        f"表面積 = 2 × π × 半径 × (半径 + 高さ)",
        f"表面積 = 2 × 3.14 × {radius}cm × ({radius}cm + {height}cm)",
        f"表面積 ≈ {round(surface_area, 2)}cm²"
    ]
    return problem, solution_steps


def generate_triangle_angle_problem():
    angle1 = random.randint(30, 80)
    angle2 = random.randint(30, 80)
    problem = f"三角形の内角の一つが{angle1}度、もう一つが{angle2}度のとき、残りの内角を求めなさい。"
    angle3 = 180 - angle1 - angle2
    solution_steps = [
        f"三角形の内角の和は180度です。",
        f"残りの内角 = 180度 - {angle1}度 - {angle2}度",
        f"残りの内角 = {angle3}度"
    ]
    return problem, solution_steps


def generate_solid_volume_ratio_problem():
    ratio = random.randint(2, 5)
    problem = f"相似な二つの立体図形の相似比が {ratio} : 1 のとき、体積比を求めなさい。"
    volume_ratio = ratio ** 3
    solution_steps = [
        f"相似な立体図形の体積比は相似比の3乗です。",
        f"体積比 = {ratio}³ : 1³",
        f"体積比 = {volume_ratio} : 1"
    ]
    return problem, solution_steps


def generate_consecutive_integers_sum_problem():
    n = random.randint(5, 10)
    start = random.randint(1, 20)
    end = start + n - 1
    problem = f"連続する整数 {start} から {end} までの和を求めなさい。"
    sum_value = n * (start + end) // 2
    solution_steps = [
        f"連続する整数の和は次の公式で計算できます。",
        f"和 = n × (最初の整数 + 最後の整数) / 2",
        f"和 = {n} × ({start} + {end}) / 2",
        f"和 = {sum_value}"
    ]
    return problem, solution_steps


def generate_composite_function_problem():
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    c = random.randint(1, 5)
    d = random.randint(1, 5)
    problem = f"関数 f(x) = {a}x + {b} と g(x) = {c}x + {d} の合成関数 h(x) = f(g(x)) を求めなさい。"
    h = f"{a}({c}x + {d}) + {b}"
    h_expanded = f"{a*c}x + {a*d + b}"
    solution_steps = [
        f"h(x) = f(g(x)) = f({c}x + {d})",
        f"= {a}({c}x + {d}) + {b}",
        f"= {h_expanded}"
    ]
    return problem, solution_steps


def generate_arithmetic_sequence_problem():
    a1 = random.randint(1, 10)
    d = random.randint(1, 10)
    n = random.randint(1, 20)
    problem = f"初項が{a1}、公差が{d}の等差数列の第{n}項を求めなさい。"
    an = a1 + (n - 1) * d
    solution_steps = [
        f"等差数列の一般項は次の公式で計算できます。",
        f"第n項 = 初項 + (n - 1) × 公差",
        f"第{n}項 = {a1} + ({n} - 1) × {d}",
        f"第{n}項 = {an}"
    ]
    return problem, solution_steps


def generate_function_value_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    x = random.randint(1, 10)
    problem = f"関数 f(x) = {a}x² + {b}x + {c} のとき、f({x}) を求めなさい。"
    fx = a * x**2 + b * x + c
    solution_steps = [
        f"f(x) = {a}x² + {b}x + {c}",
        f"f({x}) = {a}({x})² + {b}({x}) + {c}",
        f"= {a*x**2} + {b*x} + {c}",
        f"= {fx}"
    ]
    return problem, solution_steps


def generate_quadratic_max_min_problem():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    problem = f"二次関数 y = {a}x² + {b}x + {c} の最大値または最小値を求めなさい。"
    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    max_or_min = "最小値" if a > 0 else "最大値"
    solution_steps = [
        f"二次関数の頂点の座標を求めます。",
        f"頂点のx座標 = -b / 2a = {-b} / 2×{a} = {round(vertex_x, 2)}",
        f"頂点のy座標 = {a}({round(vertex_x, 2)})² + {b}({round(vertex_x, 2)}) + {c} = {round(vertex_y, 2)}",
        f"よって、{max_or_min}は {round(vertex_y, 2)}"
    ]
    return problem, solution_steps


def generate_combination_problem():
    n = random.randint(5, 10)
    r = random.randint(1, n)
    problem = f"{n}個の中から{r}個を選ぶ組合せの数を求めなさい。"
    combination = math.comb(n, r)
    solution_steps = [
        f"組合せの公式を使用します。",
        f"nCr = n! / (r!(n-r)!)",
        f"{n}C{r} = {n}! / ({r}!({n}-{r})!)",
        f"{n}C{r} = {combination}"
    ]
    return problem, solution_steps


def generate_discriminant_problem():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    problem = f"二次方程式 {a}x² + {b}x + {c} = 0 の判別式を求め、その性質を示しなさい。"
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        nature = "2つの異なる実数解を持つ"
    elif discriminant == 0:
        nature = "重解を持つ"
    else:
        nature = "2つの異なる虚数解を持つ"
    solution_steps = [
        f"判別式 = b² - 4ac",
        f"判別式 = {b}² - 4×{a}×{c}",
        f"判別式 = {discriminant}",
        f"この判別式の値は {nature}"
    ]
    return problem, solution_steps


def generate_triangle_area_height_problem():
    base = random.randint(1, 20)
    height = random.randint(1, 20)
    problem = f"底辺が{base}cmで、面積が{(base * height) / 2}cm²の三角形の高さを求めなさい。"
    solution_steps = [
        f"三角形の面積の公式を使用します。",
        f"面積 = (底辺 × 高さ) / 2",
        f"{(base * height) / 2} = ({base} × 高さ) / 2",
        f"高さ = 2 × {((base * height) / 2) / base}",
        f"高さ = {height}cm"
    ]
    return problem, solution_steps


def generate_parabola_vertex_problem():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    problem = f"二次関数 y = {a}x² + {b}x + {c} の頂点の座標を求めなさい。"
    h = -b / (2 * a)
    k = a * h**2 + b * h + c
    solution_steps = [
        f"頂点のx座標 = -b / 2a = {-b} / 2×{a} = {round(h, 2)}",
        f"頂点のy座標 = {a}({round(h, 2)})² + {b}({round(h, 2)}) + {c} = {round(k, 2)}",
        f"頂点の座標は ({round(h, 2)}, {round(k, 2)})"
    ]
    return problem, solution_steps


def generate_linear_inequality_problem():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    c = random.randint(1, 10)
    problem = f"{a}x + {b} > {c} を満たすxの範囲を求めなさい。"
    solution_steps = [
        f"{a}x + {b} > {c}",
        f"{a}x > {c} - {b}",
        f"x > ({c} - {b}) / {a}",
        f"x > {round((c - b) / a, 2)}"
    ]
    return problem, solution_steps


def generate_circle_center_radius_problem():
    h = random.randint(-10, 10)
    k = random.randint(-10, 10)
    r = random.randint(1, 10)
    problem = f"方程式 (x - {h})² + (y - {k})² = {r**2} で表される円の中心と半径を求めなさい。"
    solution_steps = [
        f"円の方程式 (x - h)² + (y - k)² = r² の形式です。",
        f"h = {h}, k = {k}, r = √{r**2}",
        f"中心の座標は ({h}, {k})",
        f"半径は {r}cm"
    ]
    return problem, solution_steps


def generate_linear_equation_problem():
    x1 = random.randint(1, 10)
    y1 = random.randint(1, 10)
    x2 = random.randint(1, 10)
    y2 = random.randint(1, 10)
    if x1 == x2:  # 縦の直線のケースを避けるため
        x2 += 1
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    problem = f"点 ({x1}, {y1}) と点 ({x2}, {y2}) を通る直線の方程式を求めなさい。"
    solution_steps = [
        f"直線の傾き = (y2 - y1) / (x2 - x1)",
        f"= ({y2} - {y1}) / ({x2} - {x1})",
        f"= {round(slope, 2)}",
        f"切片 = y1 - (傾き × x1)",
        f"= {y1} - ({round(slope, 2)} × {x1})",
        f"= {round(intercept, 2)}",
        f"よって、直線の方程式は y = {round(slope, 2)}x + {round(intercept, 2)}"
    ]
    return problem, solution_steps


def generate_solid_surface_area_problem():
    length = random.randint(1, 10)
    width = random.randint(1, 10)
    height = random.randint(1, 10)
    problem = f"長さが{length}cm、幅が{width}cm、高さが{height}cmの直方体の表面積を求めなさい。"
    surface_area = 2 * (length * width + width * height + height * length)
    solution_steps = [
        f"直方体の表面積の公式を使用します。",
        f"表面積 = 2 × (長さ × 幅 + 幅 × 高さ + 高さ × 長さ)",
        f"表面積 = 2 × ({length} × {width} + {width} × {height} + {height} × {length})",
        f"表面積 = 2 × ({length * width} + {width * height} + {height * length})",
        f"表面積 = {surface_area}cm²"
    ]
    return problem, solution_steps


def generate_absolute_value_inequality_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    problem = f"|{a}x + {b}| < {c} を満たす x の範囲を求めなさい。"
    solution_steps = [
        f"絶対値の不等式を解きます。",
        f"{-c} < {a}x + {b} < {c}",
        f"{-c} - {b} < {a}x < {c} - {b}",
        f"({-c} - {b}) / {a} < x < ({c} - {b}) / {a}",
        f"x の範囲は {round((-c - b) / a, 2)} < x < {round((c - b) / a, 2)}"
    ]
    return problem, solution_steps


def generate_two_variable_equation_problem():
    a1, b1, c1 = random.randint(1, 10), random.randint(
        1, 10), random.randint(1, 20)
    a2, b2, c2 = random.randint(1, 10), random.randint(
        1, 10), random.randint(1, 20)
    problem = f"次の連立方程式を解きなさい。\n{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}"

    # 解の計算
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        solution_steps = [
            f"連立方程式：",
            f"{a1}x + {b1}y = {c1}",
            f"{a2}x + {b2}y = {c2}",
            f"この連立方程式には解がありません。"
        ]
    else:
        x = (c1 * b2 - c2 * b1) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        solution_steps = [
            f"連立方程式：",
            f"{a1}x + {b1}y = {c1}",
            f"{a2}x + {b2}y = {c2}",
            f"行列式を計算します。",
            f"行列式 = {a1} * {b2} - {a2} * {b1} = {determinant}",
            f"x = ({c1} * {b2} - {c2} * {b1}) / {determinant} = {round(x, 2)}",
            f"y = ({a1} * {c2} - {a2} * {c1}) / {determinant} = {round(y, 2)}"
        ]
    return problem, solution_steps


def generate_inverse_proportion_problem():
    k = random.randint(1, 10)
    x = random.randint(1, 10)
    problem = f"反比例の関係 y = {k}/x のとき、x = {x} のときの y の値を求めなさい。"
    y = round(k / x, 2)
    solution_steps = [
        f"反比例の関係式 y = {k}/x",
        f"x = {x} のとき、",
        f"y = {k}/{x} = {y}"
    ]
    return problem, solution_steps


def generate_binomial_expansion_problem():
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    n = random.randint(2, 5)
    problem = f"(x + {a})^{n} を展開しなさい。"
    expansion = [(math.comb(n, k) * a**k, n - k) for k in range(n + 1)]
    terms = " + ".join([f"{coef if coef != 1 else ''}x^{exp}" if exp !=
                       0 else f"{coef}" for coef, exp in expansion])
    solution_steps = [
        f"二項定理を使用します。",
        f"(x + {a})^{n} = " +
        " + ".join([f"({math.comb(n, k)} * x^{n-k} * {a}^{k})" for k in range(n + 1)]),
        f"展開 = {terms}"
    ]
    return problem, solution_steps


def generate_combinatorial_counting_problem():
    items = random.randint(5, 10)
    select = random.randint(1, items)
    problem = f"{items}個の異なるものから{select}個を選ぶ場合の数を求めなさい。"
    combinations = math.comb(items, select)
    solution_steps = [
        f"組み合わせの公式を使用します。",
        f"nCr = n! / (r!(n-r)!)",
        f"{items}C{select} = {items}! / ({select}!({items}-{select})!)",
        f"{items}C{select} = {combinations}"
    ]
    return problem, solution_steps


def generate_set_operation_problem():
    universal_set = sorted(set(range(1, 21)))
    set_a = set(random.sample(universal_set, random.randint(5, 15)))
    set_b = set(random.sample(universal_set, random.randint(5, 15)))
    problem = f"集合A = {set_a}、集合B = {set_b}について、次の集合を求めなさい。\n1. A ∩ B\n2. A ∪ B\n3. A - B"
    intersection = set_a & set_b
    union = set_a | set_b
    difference = set_a - set_b
    solution_steps = [
        f"1. A ∩ B = {intersection}",
        f"2. A ∪ B = {union}",
        f"3. A - B = {difference}"
    ]
    return problem, solution_steps


def generate_probability_combination_problem():
    n = random.randint(5, 10)
    r = random.randint(1, n)
    success_count = random.randint(1, r)
    problem = f"{n}個の中から{r}個を選び、そのうち{success_count}個が特定の条件を満たす確率を求めなさい。"
    total_combinations = math.comb(n, r)
    success_combinations = math.comb(
        success_count, 1) * math.comb(n - success_count, r - 1)
    probability = success_combinations / total_combinations
    solution_steps = [
        f"全体の組み合わせの数 = {total_combinations}",
        f"成功の組み合わせの数 = {success_combinations}",
        f"確率 = 成功の組み合わせの数 / 全体の組み合わせの数",
        f"確率 = {success_combinations} / {total_combinations}",
        f"確率 = {round(probability, 2)}"
    ]
    return problem, solution_steps


def generate_permutation_problem():
    n = random.randint(5, 10)
    r = random.randint(1, n)
    problem = f"{n}個の異なるものから{r}個を並べる順列の数を求めなさい。"
    permutations = math.perm(n, r)
    solution_steps = [
        f"順列の公式を使用します。",
        f"nPr = n! / (n-r)!",
        f"{n}P{r} = {n}! / ({n}-{r})!",
        f"{n}P{r} = {permutations}"
    ]
    return problem, solution_steps


def generate_set_complement_problem():
    universal_set = sorted(set(range(1, 21)))
    set_a = set(random.sample(universal_set, random.randint(5, 15)))
    problem = f"普遍集合 U = {universal_set}、集合 A = {set_a} について、A の補集合を求めなさい。"
    complement = set(universal_set) - set_a
    solution_steps = [
        f"補集合の定義を使用します。",
        f"補集合 A' = U - A",
        f"A' = {set(universal_set)} - {set_a}",
        f"A' = {complement}"
    ]
    return problem, solution_steps


def generate_complex_probability_problem():
    total_balls = random.randint(30, 50)
    red_balls = random.randint(1, total_balls // 2)
    blue_balls = random.randint(1, total_balls // 2)
    green_balls = total_balls - red_balls - blue_balls
    draws = random.randint(2, 5)
    problem = f"袋の中に{total_balls}個のボールがあり、その中に赤が{red_balls}個、青が{blue_balls}個、緑が{green_balls}個含まれています。" \
              f"{draws}個のボールを同時に引くとき、全て赤である確率を求めなさい。"

    if draws > red_balls:
        probability = 0
    else:
        total_combinations = math.comb(total_balls, draws)
        red_combinations = math.comb(red_balls, draws)
        probability = red_combinations / total_combinations

    solution_steps = [
        f"全体の組み合わせの数 = {total_combinations}",
        f"赤いボールを引く組み合わせの数 = {red_combinations}",
        f"確率 = 赤いボールの組み合わせ / 全体の組み合わせ",
        f"確率 = {red_combinations} / {total_combinations}",
        f"確率 = {round(probability, 5)}"
    ]
    return problem, solution_steps


def generate_complex_ratio_problem():
    initial_population = random.randint(1000, 5000)
    increase_percentage = random.randint(5, 20)
    decrease_percentage = random.randint(1, 10)
    problem = f"ある都市の初期人口は{initial_population}人です。まず、人口が{increase_percentage}%増加し、次に{decrease_percentage}%減少しました。" \
              f"最終的な人口を求めなさい。"

    increased_population = initial_population * (1 + increase_percentage / 100)
    final_population = increased_population * (1 - decrease_percentage / 100)

    solution_steps = [
        f"最初の人口 = {initial_population}",
        f"人口が{increase_percentage}%増加後の人口 = {initial_population} × (1 + {increase_percentage} / 100)",
        f"= {round(increased_population, 2)}",
        f"次に、人口が{decrease_percentage}%減少",
        f"最終的な人口 = {round(increased_population, 2)} × (1 - {decrease_percentage} / 100)",
        f"= {round(final_population, 2)}"
    ]
    return problem, solution_steps


def generate_conditional_probability_problem():
    total_people = random.randint(50, 100)
    event_A_people = random.randint(5, total_people // 2)
    event_B_people = random.randint(1, total_people // 4)
    event_A_and_B_people = random.randint(
        1, min(event_A_people, event_B_people))

    problem = (f"ある集団に{total_people}人の人々がいます。この中で条件Aを満たすした人数が{event_A_people}人、"
               f"条件Bを満たすした人数が{event_B_people}人です。また、条件Aかつ条件Bを満たすした人数が"
               f"{event_A_and_B_people}人です。この集団からランダムに1人選んだとき、その人が条件Bを満たす者である"
               f"という条件のもとで、条件Aを満たすした確率を求めなさい。")

    if event_B_people == 0:
        probability = 0
    else:
        probability = event_A_and_B_people / event_B_people

    solution_steps = [
        f"条件Bを満たす者の中で条件Aを満たすした人数 = {event_A_and_B_people}",
        f"条件Bを満たす者の全体の人数 = {event_B_people}",
        f"条件付き確率 = 条件Aかつ条件Bを満たす人数 / 条件Bを満たす人数",
        f"= {event_A_and_B_people} / {event_B_people}",
        f"確率 = {round(probability, 5)}"
    ]
    return problem, solution_steps


def generate_population_change_problem():
    initial_population = random.randint(1000, 5000)
    increase_percentage = random.randint(5, 20)
    decrease_percentage = random.randint(1, 10)
    second_increase_percentage = random.randint(1, 15)

    problem = (f"ある都市の初期人口は{initial_population}人です。まず、人口が{increase_percentage}%増加し、"
               f"次に{decrease_percentage}%減少し、さらに{second_increase_percentage}%増加しました。最終的な人口を求めなさい。")

    increased_population = initial_population * (1 + increase_percentage / 100)
    decreased_population = increased_population * \
        (1 - decrease_percentage / 100)
    final_population = decreased_population * \
        (1 + second_increase_percentage / 100)

    solution_steps = [
        f"最初の人口 = {initial_population}",
        f"人口が{increase_percentage}%増加後の人口 = {initial_population} × (1 + {increase_percentage} / 100)",
        f"= {round(increased_population, 2)}",
        f"次に、人口が{decrease_percentage}%減少",
        f"減少後の人口 = {round(increased_population, 2)} × (1 - {decrease_percentage} / 100)",
        f"= {round(decreased_population, 2)}",
        f"さらに、人口が{second_increase_percentage}%増加",
        f"最終的な人口 = {round(decreased_population, 2)} × (1 + {second_increase_percentage} / 100)",
        f"= {round(final_population, 2)}"
    ]
    return problem, solution_steps


def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def generate_complex_probability_problem():
    total_balls = random.randint(5, 20)
    red_balls = random.randint(1, total_balls // 2)
    blue_balls = random.randint(1, total_balls // 2)
    green_balls = total_balls - red_balls - blue_balls
    draws = random.randint(2, 5)
    problem = (f"袋の中に{total_balls}個のボールがあり、その中に赤が{red_balls}個、青が{blue_balls}個、"
               f"緑が{green_balls}個含まれています。{draws}個のボールを同時に引くとき、"
               f"全て赤である確率を求めなさい。")

    if draws > red_balls:
        probability = 0
        total_combinations = 1
        red_combinations = 0
    else:
        total_combinations = math.comb(total_balls, draws)
        red_combinations = math.comb(red_balls, draws)
        probability = red_combinations / total_combinations

    solution_steps = [
        f"組み合わせの数を計算します。",
        f"全体の組み合わせの数 = {total_balls}C{draws} = {total_balls}! / ({draws}! × ({total_balls}-{draws})!) = {total_combinations}",
        f"赤いボールの組み合わせの数 = {red_balls}C{draws} = {red_balls}! / ({draws}! × ({red_balls}-{draws})!) = {red_combinations}",
        f"確率 = 赤いボールの組み合わせ / 全体の組み合わせ",
        f"= {red_combinations} / {total_combinations}",
        f"= {round(probability, 5)}"
    ]
    return problem, solution_steps


def generate_reverse_population_problem():
    final_population = random.randint(3000, 5000)
    increase_percentage1 = random.randint(10, 30)
    decrease_percentage = random.randint(5, 15)
    increase_percentage2 = random.randint(5, 20)

    initial_population = final_population / ((1 + increase_percentage2 / 100) * (
        1 - decrease_percentage / 100) * (1 + increase_percentage1 / 100))

    problem = (f"ある都市の最終的な人口は{final_population}人です。まず、人口が{increase_percentage1}%増加し、次に"
               f"{decrease_percentage}%減少し、さらに{increase_percentage2}%増加しました。"
               f"初期人口を求めなさい。")

    solution_steps = [
        f"最終的な人口 = {final_population}",
        f"逆算して初期人口を求めます。",
        f"1. 最初の増加を元に戻します。",
        f"人口 = {final_population} / (1 + {increase_percentage2} / 100)",
        f"= {round(final_population / (1 + increase_percentage2 / 100), 2)}",
        f"2. 次に減少を元に戻します。",
        f"人口 = {round(final_population / (1 + increase_percentage2 / 100), 2)} / (1 - {decrease_percentage} / 100)",
        f"= {round(final_population / ((1 + increase_percentage2 / 100) * (1 - decrease_percentage / 100)), 2)}",
        f"3. 最後に最初の増加を元に戻します。",
        f"人口 = {round(final_population / ((1 + increase_percentage2 / 100) * (1 - decrease_percentage / 100)), 2)} / (1 + {increase_percentage1} / 100)",
        f"初期人口 = {round(initial_population, 2)}"
    ]
    return problem, solution_steps


def generate_work_problem():
    rate1 = random.randint(5, 10)
    time1 = random.randint(1, 5)
    rate2 = random.randint(5, 10)
    problem = (f"Aさんは1時間で{rate1}個の仕事をこなします。Bさんは1時間で{rate2}個の仕事をこなします。"
               f"Aさんが{time1}時間働いた後、BさんがAさんと同じ量の仕事をするのに何時間かかりますか。")

    work_done = rate1 * time1
    time2 = work_done / rate2

    solution_steps = [
        f"Aさんの仕事量 = {rate1} × {time1} = {work_done}個",
        f"Bさんの仕事量 = {rate2}個/時間",
        f"Bさんの時間 = {work_done} / {rate2}",
        f"= {round(time2, 2)}時間"
    ]
    return problem, solution_steps


def generate_money_problem():
    price = random.randint(50, 200)
    total_amount = random.randint(1000, 5000)
    problem = (f"ある商品は1個{price}円です。全体の購入金額が{total_amount}円となるようにするには、"
               f"いくつの商品を購入する必要がありますか。")

    quantity = total_amount / price

    solution_steps = [
        f"購入金額 = 価格 × 数量",
        f"{total_amount} = {price} × 数量",
        f"数量 = {total_amount} / {price}",
        f"= {round(quantity)}個"
    ]
    return problem, solution_steps


def generate_distance_problem():
    speed1 = random.randint(30, 100)
    time1 = random.randint(1, 5)
    speed2 = random.randint(30, 100)
    problem = (f"Aさんは{speed1}km/hの速度で{time1}時間走ります。"
               f"BさんはAさんと同じ距離を{speed2}km/hの速度で走るには何時間かかりますか。")

    distance = speed1 * time1
    time2 = distance / speed2

    solution_steps = [
        f"Aさんの走行距離 = {speed1} × {time1} = {distance}km",
        f"Bさんの速度 = {speed2}km/h",
        f"Bさんの時間 = {distance} / {speed2}",
        f"= {round(time2, 2)}時間"
    ]
    return problem, solution_steps


def generate_mixture_problem():
    concentration1 = random.randint(10, 30)
    volume1 = random.randint(100, 500)
    concentration2 = random.randint(10, 30)
    volume2 = random.randint(100, 500)
    final_volume = volume1 + volume2
    final_concentration = ((concentration1 * volume1) +
                           (concentration2 * volume2)) / final_volume

    problem = (f"{concentration1}%の溶液{volume1}mlと{concentration2}%の溶液{volume2}mlを混合します。"
               f"混合後の溶液の濃度は何%になりますか。")

    solution_steps = [
        f"混合後の溶液の濃度 = (初めの溶液の濃度 × 初めの溶液の体積 + 次の溶液の濃度 × 次の溶液の体積) / 合計体積",
        f"= ({concentration1} × {volume1} + {concentration2} × {volume2}) / {final_volume}",
        f"= {round(final_concentration, 2)}%"
    ]
    return problem, solution_steps


def generate_savings_problem():
    principal = random.randint(1000, 5000)
    rate = random.randint(1, 10)
    time = random.randint(1, 5)
    problem = (f"ある人は{principal}円を年利{rate}%で{time}年間預けました。"
               f"元本と利息を合わせた合計額はいくらになりますか。")

    amount = principal * (1 + rate / 100) ** time

    solution_steps = [
        f"合計額 = 元本 × (1 + 利率)^時間",
        f"= {principal} × (1 + {rate} / 100)^{time}",
        f"= {round(amount, 2)}円"
    ]
    return problem, solution_steps


def generate_two_rectangles_area_problem():
    length1 = random.randint(1, 20)
    width1 = random.randint(1, 20)
    length2 = random.randint(1, 20)
    width2 = random.randint(1, 20)
    problem = f"長さが{length1}cm、幅が{width1}cmの長方形と、長さが{length2}cm、幅が{width2}cmの長方形の面積の和を求めなさい。"
    area1 = length1 * width1
    area2 = length2 * width2
    total_area = area1 + area2
    solution_steps = [
        f"長方形1の面積 = 長さ × 幅 = {length1} × {width1} = {area1} cm²",
        f"長方形2の面積 = 長さ × 幅 = {length2} × {width2} = {area2} cm²",
        f"面積の和 = {area1} + {area2} = {total_area} cm²"
    ]
    return problem, solution_steps


def generate_triangle_square_perimeter_problem():
    side1 = random.randint(1, 20)
    side2 = random.randint(1, 20)
    side3 = random.randint(1, 20)
    square_side = random.randint(1, 20)
    problem = f"三角形の辺の長さが{side1}cm、{side2}cm、{side3}cmのとき、この三角形の周の長さと、辺の長さが{square_side}cmの正方形の周の長さの和を求めなさい。"
    perimeter_triangle = side1 + side2 + side3
    perimeter_square = 4 * square_side
    total_perimeter = perimeter_triangle + perimeter_square
    solution_steps = [
        f"三角形の周の長さ = {side1} + {side2} + {side3} = {perimeter_triangle} cm",
        f"正方形の周の長さ = 4 × {square_side} = {perimeter_square} cm",
        f"周の長さの和 = {perimeter_triangle} + {perimeter_square} = {total_perimeter} cm"
    ]
    return problem, solution_steps


def generate_two_circles_area_problem():
    radius1 = random.randint(1, 20)
    radius2 = random.randint(1, 20)
    problem = f"半径が{radius1}cmの円と、半径が{radius2}cmの円の面積の和を求めなさい。"
    area1 = 3.14 * radius1**2
    area2 = 3.14 * radius2**2
    total_area = area1 + area2
    solution_steps = [
        f"円1の面積 = π × 半径² = 3.14 × {radius1}² = {round(area1, 2)} cm²",
        f"円2の面積 = π × 半径² = 3.14 × {radius2}² = {round(area2, 2)} cm²",
        f"面積の和 = {round(area1, 2)} + {round(area2, 2)} = {round(total_area, 2)} cm²"
    ]
    return problem, solution_steps


def generate_two_parallelograms_area_problem():
    base1 = random.randint(1, 20)
    height1 = random.randint(1, 20)
    base2 = random.randint(1, 20)
    height2 = random.randint(1, 20)
    problem = f"底辺が{base1}cm、高さが{height1}cmの平行四辺形と、底辺が{base2}cm、高さが{height2}cmの平行四辺形の面積の和を求めなさい。"
    area1 = base1 * height1
    area2 = base2 * height2
    total_area = area1 + area2
    solution_steps = [
        f"平行四辺形1の面積 = 底辺 × 高さ = {base1} × {height1} = {area1} cm²",
        f"平行四辺形2の面積 = 底辺 × 高さ = {base2} × {height2} = {area2} cm²",
        f"面積の和 = {area1} + {area2} = {total_area} cm²"
    ]
    return problem, solution_steps


def generate_two_triangles_area_problem():
    base1 = random.randint(1, 20)
    height1 = random.randint(1, 20)
    base2 = random.randint(1, 20)
    height2 = random.randint(1, 20)
    problem = f"底辺が{base1}cm、高さが{height1}cmの三角形と、底辺が{base2}cm、高さが{height2}cmの三角形の面積の和を求めなさい。"
    area1 = (base1 * height1) / 2
    area2 = (base2 * height2) / 2
    total_area = area1 + area2
    solution_steps = [
        f"三角形1の面積 = (底辺 × 高さ) / 2 = ({base1} × {height1}) / 2 = {round(area1, 2)} cm²",
        f"三角形2の面積 = (底辺 × 高さ) / 2 = ({base2} × {height2}) / 2 = {round(area2, 2)} cm²",
        f"面積の和 = {round(area1, 2)} + {round(area2, 2)} = {round(total_area, 2)} cm²"
    ]
    return problem, solution_steps


def generate_circle_triangle_area_problem():
    radius = random.randint(1, 20)
    base = random.randint(1, 20)
    height = random.randint(1, 20)
    problem = f"半径が{radius}cmの円と、底辺が{base}cm、高さが{height}cmの三角形の面積の和を求めなさい。"
    area_circle = 3.14 * radius**2
    area_triangle = (base * height) / 2
    total_area = area_circle + area_triangle
    solution_steps = [
        f"円の面積 = π × 半径² = 3.14 × {radius}² = {round(area_circle, 2)} cm²",
        f"三角形の面積 = (底辺 × 高さ) / 2 = ({base} × {height}) / 2 = {round(area_triangle, 2)} cm²",
        f"面積の和 = {round(area_circle, 2)} + {round(area_triangle, 2)} = {round(total_area, 2)} cm²"
    ]
    return problem, solution_steps


def generate_circle_inscribed_triangle_perimeter_problem():
    radius = random.randint(5, 15)
    side = radius * (3 ** 0.5)
    problem = f"半径が{radius}cmの円と、その円に内接する正三角形の周の長さの和を求めなさい。"
    circumference_circle = 2 * 3.14 * radius
    perimeter_triangle = 3 * side
    total_perimeter = circumference_circle + perimeter_triangle
    solution_steps = [
        f"円の周の長さ = 2 × π × 半径 = 2 × 3.14 × {radius} = {round(circumference_circle, 2)} cm",
        f"正三角形の辺の長さ = 半径 × √3 = {radius} × √3 = {round(side, 2)} cm",
        f"正三角形の周の長さ = 3 × {round(side, 2)} = {round(perimeter_triangle, 2)} cm",
        f"周の長さの和 = {round(circumference_circle, 2)} + {round(perimeter_triangle, 2)} = {round(total_perimeter, 2)} cm"
    ]
    return problem, solution_steps


def generate_circle_triangle_area_ratio_problem():
    radius = random.randint(1, 20)
    base = random.randint(1, 20)
    height = random.randint(1, 20)
    problem = f"半径が{radius}cmの円と、底辺が{base}cm、高さが{height}cmの三角形の面積の比を求めなさい。"
    area_circle = 3.14 * radius**2
    area_triangle = (base * height) / 2
    ratio = area_circle / area_triangle
    solution_steps = [
        f"円の面積 = π × 半径² = 3.14 × {radius}² = {round(area_circle, 2)} cm²",
        f"三角形の面積 = (底辺 × 高さ) / 2 = ({base} × {height}) / 2 = {round(area_triangle, 2)} cm²",
        f"面積比 = 円の面積 / 三角形の面積",
        f"= {round(area_circle, 2)} / {round(area_triangle, 2)}",
        f"= {round(ratio, 2)}"
    ]
    return problem, solution_steps


def generate_circle_triangle_inscribed_circumscribed_problem():
    side = random.randint(5, 15)
    radius_inscribed = side / (2 * (3 ** 0.5))
    radius_circumscribed = side / (3 ** 0.5)
    problem = (f"一辺が{side}cmの正三角形があり、この三角形に内接する円と外接する円の半径を求めなさい。")
    solution_steps = [
        f"内接円の半径 = 一辺 / (2 × √3) = {side} / (2 × √3) = {round(radius_inscribed, 2)} cm",
        f"外接円の半径 = 一辺 / √3 = {side} / √3 = {round(radius_circumscribed, 2)} cm"
    ]
    return problem, solution_steps


def generate_circle_triangle_common_area_problem():
    radius = random.randint(5, 15)
    side = random.randint(1, radius)
    area_segment = (radius**2 * (3.14 / 3) - 0.5 * radius **
                    2 * (3 ** 0.5) / 2) / 2  # 円の一部の面積
    area_triangle = (side**2 * (3 ** 0.5)) / 4
    problem = (f"半径が{radius}cmの円があり、この円に内接する正三角形の一辺が{side}cmです。"
               f"円と三角形の共通部分の面積を求めなさい。")
    solution_steps = [
        f"円の一部の面積 = (半径² × (π / 3) - 0.5 × 半径² × (√3 / 2)) / 2",
        f"= ({radius}² × (3.14 / 3) - 0.5 × {radius}² × (√3 / 2)) / 2",
        f"= {round(area_segment, 2)} cm²",
        f"正三角形の面積 = (一辺² × √3) / 4",
        f"= ({side}² × √3) / 4",
        f"= {round(area_triangle, 2)} cm²",
        f"共通部分の面積 = 円の一部の面積 + 正三角形の面積",
        f"= {round(area_segment + area_triangle, 2)} cm²"
    ]
    return problem, solution_steps


def generate_prime_numbers_problem():
    start = random.randint(1, 50)
    end = start + random.randint(10, 50)
    problem = f"{start}から{end}までの範囲に含まれる素数を求めなさい。"
    primes = []
    solution_steps = []
    for num in range(start, end + 1):
        is_prime = all(num % div != 0 for div in range(2, int(num ** 0.5) + 1))
        if is_prime and num > 1:
            primes.append(num)
            solution_steps.append(f"{num}は素数です。")
        else:
            solution_steps.append(f"{num}は素数ではありません。")
    solution_steps.insert(0, f"{start}から{end}までの範囲に含まれる素数は次の通りです。")
    if primes:
        solution_steps.append(f"まとめ: {primes}")
    else:
        solution_steps.append("条件を満たす数はありません。")
    return problem, solution_steps


def generate_even_numbers_problem():
    start = random.randint(1, 50)
    end = start + random.randint(10, 50)
    condition = random.choice(["3の倍数", "5の倍数", "7の倍数"])
    problem = f"{start}から{end}までの範囲に含まれる{condition}の偶数を求めなさい。"
    even_numbers = []
    solution_steps = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            if condition == "3の倍数" and num % 3 == 0:
                even_numbers.append(num)
                solution_steps.append(f"{num}は偶数で{condition}です。")
            elif condition == "5の倍数" and num % 5 == 0:
                even_numbers.append(num)
                solution_steps.append(f"{num}は偶数で{condition}です。")
            elif condition == "7の倍数" and num % 7 == 0:
                even_numbers.append(num)
                solution_steps.append(f"{num}は偶数で{condition}です。")
            else:
                solution_steps.append(f"{num}は偶数ですが{condition}ではありません。")
        else:
            solution_steps.append(f"{num}は偶数ではありません。")
    solution_steps.insert(0, f"{start}から{end}までの範囲に含まれる{condition}の偶数は次の通りです。")
    if even_numbers:
        solution_steps.append(f"まとめ: {even_numbers}")
    else:
        solution_steps.append("条件を満たす数はありません。")
    return problem, solution_steps


def generate_odd_numbers_problem():
    start = random.randint(1, 50)
    end = start + random.randint(10, 50)
    condition = random.choice(["4の倍数", "6の倍数", "8の倍数"])
    problem = f"{start}から{end}までの範囲に含まれる{condition}の奇数を求めなさい。"
    odd_numbers = []
    solution_steps = []
    for num in range(start, end + 1):
        if num % 2 != 0:
            if condition == "4の倍数" and num % 4 == 0:
                odd_numbers.append(num)
                solution_steps.append(f"{num}は奇数で{condition}です。")
            elif condition == "6の倍数" and num % 6 == 0:
                odd_numbers.append(num)
                solution_steps.append(f"{num}は奇数で{condition}です。")
            elif condition == "8の倍数" and num % 8 == 0:
                odd_numbers.append(num)
                solution_steps.append(f"{num}は奇数で{condition}です。")
            else:
                solution_steps.append(f"{num}は奇数ですが{condition}ではありません。")
        else:
            solution_steps.append(f"{num}は奇数ではありません。")
    solution_steps.insert(0, f"{start}から{end}までの範囲に含まれる{condition}の奇数は次の通りです。")
    if odd_numbers:
        solution_steps.append(f"まとめ: {odd_numbers}")
    else:
        solution_steps.append("条件を満たす数はありません。")
    return problem, solution_steps


def generate_multiple_divisible_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    start = random.randint(1, 50)
    end = start + random.randint(10, 50)
    problem = f"{start}から{end}までの範囲で、{a}の倍数であり{b}で割り切れる数をすべて求めなさい。"
    numbers = []
    solution_steps = []
    for x in range(start, end + 1):
        if x % a == 0:
            if x % b == 0:
                numbers.append(x)
                solution_steps.append(f"{x}は{a}の倍数であり{b}で割り切れます。")
            else:
                solution_steps.append(f"{x}は{a}の倍数ですが{b}で割り切れません。")
        else:
            solution_steps.append(f"{x}は{a}の倍数ではありません。")
    solution_steps.insert(
        0, f"{start}から{end}までの範囲で、{a}の倍数であり{b}で割り切れる数は次の通りです。")
    if numbers:
        solution_steps.append(f"まとめ: {numbers}")
    else:
        solution_steps.append("条件を満たす数はありません。")
    return problem, solution_steps


def generate_multiple_not_multiple_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    start = random.randint(1, 50)
    end = start + random.randint(10, 50)
    problem = f"{start}から{end}までの範囲で、{a}の倍数であり{b}の倍数でない数をすべて求めなさい。"
    numbers = []
    solution_steps = []
    for x in range(start, end + 1):
        if x % a == 0:
            if x % b != 0:
                numbers.append(x)
                solution_steps.append(f"{x}は{a}の倍数であり{b}の倍数ではありません。")
            else:
                solution_steps.append(f"{x}は{a}の倍数ですが{b}の倍数です。")
        else:
            solution_steps.append(f"{x}は{a}の倍数ではありません。")
    solution_steps.insert(
        0, f"{start}から{end}までの範囲で、{a}の倍数であり{b}の倍数でない数は次の通りです。")
    if numbers:
        solution_steps.append(f"まとめ: {numbers}")
    else:
        solution_steps.append("条件を満たす数はありません。")
    return problem, solution_steps


def generate_lcm_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    start = random.randint(1, 50)
    end = start + random.randint(10, 50)
    lcm = a * b // math.gcd(a, b)
    problem = f"{start}から{end}までの範囲で、{a}と{b}の最小公倍数である数をすべて求めなさい。"
    numbers = []
    solution_steps = [
        f"{a}と{b}の最小公倍数を計算します。",
        f"最小公倍数 = {lcm}"
    ]
    for x in range(start, end + 1):
        if x % lcm == 0:
            numbers.append(x)
            solution_steps.append(f"{x}は{a}と{b}の最小公倍数である{lcm}の倍数です。")
        else:
            solution_steps.append(f"{x}は{lcm}の倍数ではありません。")
    solution_steps.insert(1, f"{start}から{end}までの範囲で、{lcm}の倍数を探します。")
    if numbers:
        solution_steps.append(f"まとめ: {numbers}")
    else:
        solution_steps.append("条件を満たす数はありません。")
    return problem, solution_steps


def generate_multiple_and_not_multiple_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    start = random.randint(1, 50)
    end = start + random.randint(10, 50)
    problem = f"{start}から{end}までの範囲で、{a}で割り切れ、{b}の倍数であり、{c}の倍数でない数をすべて求めなさい。"
    numbers = []
    solution_steps = []
    for x in range(start, end + 1):
        if x % a == 0:
            if x % b == 0:
                if x % c != 0:
                    numbers.append(x)
                    solution_steps.append(
                        f"{x}は{a}で割り切れ、{b}の倍数であり、{c}の倍数ではありません。")
                else:
                    solution_steps.append(f"{x}は{a}で割り切れ、{b}の倍数ですが{c}の倍数です。")
            else:
                solution_steps.append(f"{x}は{a}で割り切れますが{b}の倍数ではありません。")
        else:
            solution_steps.append(f"{x}は{a}で割り切れません。")
    solution_steps.insert(
        0, f"{start}から{end}までの範囲で、{a}で割り切れ、{b}の倍数であり、{c}の倍数でない数は次の通りです。")
    if numbers:
        solution_steps.append(f"まとめ: {numbers}")
    else:
        solution_steps.append("条件を満たす数はありません。")
    return problem, solution_steps


def generate_range_and_not_multiple_problem():
    a = random.randint(1, 50)
    b = a + random.randint(10, 50)
    c = random.randint(1, 10)
    problem = f"{a}以上{b}以下の範囲で、{c}の倍数でない数をすべて求めなさい。"
    numbers = []
    solution_steps = []
    for x in range(a, b + 1):
        if x % c != 0:
            numbers.append(x)
            solution_steps.append(f"{x}は{c}の倍数ではありません。")
        else:
            solution_steps.append(f"{x}は{c}の倍数です。")
    solution_steps.insert(0, f"{a}以上{b}以下の範囲で、{c}の倍数でない数は次の通りです。")
    if numbers:
        solution_steps.append(f"まとめ: {numbers}")
    else:
        solution_steps.append("条件を満たす数はありません。")
    return problem, solution_steps


def generate_complex_equation_transformation_problem():
    a, b, c, d, e, f = [random.randint(1, 10) for _ in range(6)]
    variables = ['x', 'y', 'z']
    target_var = random.choice(variables)
    other_vars = [var for var in variables if var != target_var]

    equation = f"{a}{target_var} + {b}{other_vars[0]} - {c}{other_vars[1]} = {d} + {e}{other_vars[0]} - {f}{target_var}"
    problem = f"次の方程式を {target_var} について解きなさい。\n{equation}"

    # 解法のステップ
    solution_steps = [
        f"{a}{target_var} + {b}{other_vars[0]} - {c}{other_vars[1]} = {d} + {e}{other_vars[0]} - {f}{target_var}",
        f"{a}{target_var} + {f}{target_var} = {d} + {e}{other_vars[0]} - {b}{other_vars[0]} + {c}{other_vars[1]}",
        f"({a} + {f}){target_var} = {d} + ({e - b}){other_vars[0]} + {c}{other_vars[1]}",
        f"{target_var} = ({d} + ({e - b}){other_vars[0]} + {c}{other_vars[1]}) / ({a + f})",
        f"{target_var} = {round(d / (a + f), 2)} + {round((e - b) / (a + f), 2)}{other_vars[0]} + {round(c / (a + f), 2)}{other_vars[1]}"
    ]

    return problem, solution_steps


def generate_complex_equation_transformation_problem_2():
    a, b, c, d = [random.randint(1, 10) for _ in range(4)]
    variables = ['x', 'y', 'z']
    target_var = random.choice(variables)
    other_vars = [var for var in variables if var != target_var]

    equation = f"{a}{target_var} + {b}{other_vars[0]} = {c}{other_vars[1]} + {d}"
    problem = f"次の方程式を {target_var} について解きなさい。\n{equation}"

    # 解法のステップ
    solution_steps = [
        f"{a}{target_var} + {b}{other_vars[0]} = {c}{other_vars[1]} + {d}",
        f"{a}{target_var} = {c}{other_vars[1]} + {d} - {b}{other_vars[0]}",
        f"{target_var} = ({c}{other_vars[1]} + {d} - {b}{other_vars[0]}) / {a}",
        f"{target_var} = {round((c * random.randint(1, 10) + d - b * random.randint(1, 10)) / a, 2)}"
    ]

    return problem, solution_steps


def generate_complex_equation_transformation_problem_3():
    a, b, c, d, e = [random.randint(1, 10) for _ in range(5)]
    variables = ['x', 'y', 'z']
    target_var = random.choice(variables)
    other_vars = [var for var in variables if var != target_var]

    equation = f"{a}{target_var} - {b}{other_vars[0]} = {c}({target_var} + {d}) - {e}"
    problem = f"次の方程式を {target_var} について解きなさい。\n{equation}"

    # 解法のステップ
    solution_steps = [
        f"{a}{target_var} - {b}{other_vars[0]} = {c}({target_var} + {d}) - {e}",
        f"{a}{target_var} - {b}{other_vars[0]} = {c}{target_var} + {c * d} - {e}",
        f"{a}{target_var} - {c}{target_var} = {c * d} - {e} + {b}{other_vars[0]}",
        f"({a} - {c}){target_var} = {c * d - e} + {b}{other_vars[0]}",
        f"{target_var} = ({c * d - e} + {b}{other_vars[0]}) / ({a - c})"
    ]

    return problem, solution_steps


def generate_complex_equation_transformation_problem_4():
    a, b, c, d, e, f = [random.randint(1, 10) for _ in range(6)]
    variables = ['x', 'y', 'z']
    target_var = random.choice(variables)
    other_vars = [var for var in variables if var != target_var]

    equation = f"{a}{target_var} + {b}({target_var} - {c}) = {d}{other_vars[0]} + {e}{other_vars[1]} - {f}"
    problem = f"次の方程式を {target_var} について解きなさい。\n{equation}"

    # 解法のステップ
    solution_steps = [
        f"{a}{target_var} + {b}({target_var} - {c}) = {d}{other_vars[0]} + {e}{other_vars[1]} - {f}",
        f"{a}{target_var} + {b}{target_var} - {b * c} = {d}{other_vars[0]} + {e}{other_vars[1]} - {f}",
        f"({a} + {b}){target_var} - {b * c} = {d}{other_vars[0]} + {e}{other_vars[1]} - {f}",
        f"({a} + {b}){target_var} = {d}{other_vars[0]} + {e}{other_vars[1]} - {f} + {b * c}",
        f"{target_var} = ({d}{other_vars[0]} + {e}{other_vars[1]} - {f} + {b * c}) / ({a + b})"
    ]

    return problem, solution_steps


def generate_complex_equation_transformation_problem_5():
    a, b, c, d = [random.randint(1, 10) for _ in range(4)]
    variables = ['x', 'y', 'z']
    target_var = random.choice(variables)
    other_vars = [var for var in variables if var != target_var]

    equation = f"{a}{target_var} + {b}{other_vars[0]} = {c}({other_vars[1]} - {d}{target_var})"
    problem = f"次の方程式を {target_var} について解きなさい。\n{equation}"

    # 解法のステップ
    solution_steps = [
        f"{a}{target_var} + {b}{other_vars[0]} = {c}{other_vars[1]} - {c}{d}{target_var}",
        f"{a}{target_var} + {c}{d}{target_var} = {c}{other_vars[1]} - {b}{other_vars[0]}",
        f"({a} + {c}{d}){target_var} = {c}{other_vars[1]} - {b}{other_vars[0]}",
        f"{target_var} = ({c}{other_vars[1]} - {b}{other_vars[0]}) / ({a + c * d})"
    ]

    return problem, solution_steps


def generate_dice_conditional_probability_problem():
    dice_faces = 6
    event_A = random.randint(1, dice_faces)
    event_B_options = [i for i in range(1, dice_faces+1) if i != event_A]
    event_B = random.choice(event_B_options)
    problem = f"サイコロを1回振ったとき、{event_A}が出たときに限って{event_B}が出る確率は？"
    probability = 1 / (dice_faces - 1)
    solution_steps = [
        f"サイコロには{dice_faces}面があります。",
        f"{event_A}が出た場合、{event_B}が出る可能性のある面は残りの{dice_faces - 1}面です。",
        f"そのため、{event_B}が出る確率は1/({dice_faces - 1})です。",
        f"確率 = {round(probability, 2)}"
    ]
    return problem, solution_steps


def generate_lottery_conditional_probability_problem():
    total_tickets = random.randint(20, 50)
    winning_tickets = random.randint(1, total_tickets // 2)
    drawn_tickets = random.randint(1, total_tickets - 1)

    # 既に引かれたくじの中の当たりの数を設定
    drawn_winning_tickets = random.randint(
        0, min(drawn_tickets, winning_tickets))
    remaining_winning_tickets = winning_tickets - drawn_winning_tickets
    remaining_tickets = total_tickets - drawn_tickets

    problem = f"{total_tickets}枚のくじがあり、そのうち{winning_tickets}枚が当たりです。{drawn_tickets}枚がすでに引かれ、その中に{drawn_winning_tickets}枚の当たりがあります。残りのくじの中から当たりが出る確率は？"
    probability = remaining_winning_tickets / remaining_tickets
    solution_steps = [
        f"初めに{total_tickets}枚のくじがあり、そのうち{winning_tickets}枚が当たりです。",
        f"{drawn_tickets}枚のくじがすでに引かれ、その中に{drawn_winning_tickets}枚の当たりがあります。",
        f"残り{remaining_tickets}枚のくじの中には{remaining_winning_tickets}枚の当たりがあります。",
        f"したがって、当たりが出る確率は{remaining_winning_tickets}/{remaining_tickets}です。",
        f"確率 = {round(probability, 2)}"
    ]
    if probability > 1:
        solution_steps.append("確率は1を超えることはありませんので､問題設定が間違っている可能性があります。")
    return problem, solution_steps


def generate_dice_even_conditional_probability_problem():
    dice_faces = 6
    problem = f"2つのサイコロを振ったとき、少なくとも1つのサイコロの目が偶数である確率は？"

    # 全ての組み合わせの数
    total_outcomes = dice_faces * dice_faces

    # どちらのサイコロも奇数の目である組み合わせの数を数える
    odd_faces = [1, 3, 5]
    unfavorable_outcomes = sum(1 for i in odd_faces for j in odd_faces)

    # 少なくとも1つのサイコロの目が偶数である組み合わせの数を計算
    favorable_outcomes = total_outcomes - unfavorable_outcomes
    probability = favorable_outcomes / total_outcomes

    solution_steps = [
        f"2つのサイコロにはそれぞれ{dice_faces}面があります。",
        f"2つのサイコロの全ての出目の組み合わせは{total_outcomes}通りです。",
        f"そのうち、どちらのサイコロも奇数の目である組み合わせは次の通りです。",
        f"奇数の目のサイコロ: {odd_faces}",
        f"組み合わせを数えると、{unfavorable_outcomes}通りです。",
        f"したがって、少なくとも1つのサイコロの目が偶数である組み合わせは、全体の組み合わせから奇数の組み合わせを引いたものです。",
        f"{total_outcomes} - {unfavorable_outcomes} = {favorable_outcomes}通りです。",
        f"したがって、確率は{favorable_outcomes}/{total_outcomes}です。",
        f"確率 = {round(probability, 2)}"
    ]
    return problem, solution_steps
# 問題の生成関数


def generate_problems(n=10):
    problem_generators = [
        generate_complex_equation_transformation_problem,
        generate_complex_equation_transformation_problem_2,
        generate_complex_equation_transformation_problem_3,
        generate_complex_equation_transformation_problem_4,
        generate_complex_equation_transformation_problem_5,
        generate_range_and_not_multiple_problem,
        generate_multiple_and_not_multiple_problem,
        generate_lcm_problem,
        generate_multiple_not_multiple_problem,
        generate_multiple_divisible_problem,
        generate_odd_numbers_problem,
        generate_even_numbers_problem,
        generate_prime_numbers_problem,
        generate_circle_triangle_common_area_problem,
        generate_circle_triangle_inscribed_circumscribed_problem,
        generate_circle_triangle_area_ratio_problem,
        generate_circle_inscribed_triangle_perimeter_problem,
        generate_circle_triangle_area_problem,
        generate_two_triangles_area_problem,
        generate_two_parallelograms_area_problem,
        generate_two_circles_area_problem,
        generate_triangle_square_perimeter_problem,
        generate_two_rectangles_area_problem,
        generate_mixture_problem,
        generate_savings_problem,
        generate_distance_problem,
        generate_work_problem,
        generate_money_problem,
        generate_reverse_population_problem,
        generate_complex_probability_problem,
        generate_population_change_problem,
        generate_conditional_probability_problem,
        generate_complex_ratio_problem,
        generate_complex_probability_problem,
        generate_set_complement_problem,
        generate_permutation_problem,
        generate_probability_combination_problem,
        generate_set_operation_problem,
        generate_combinatorial_counting_problem,
        generate_binomial_expansion_problem,
        generate_inverse_proportion_problem,
        generate_two_variable_equation_problem,
        generate_absolute_value_inequality_problem,
        generate_solid_surface_area_problem,
        generate_linear_equation_problem,
        generate_circle_center_radius_problem,
        generate_linear_inequality_problem,
        generate_triangle_area_height_problem,
        generate_parabola_vertex_problem,
        generate_equation_problem,
        generate_ratio_problem,
        generate_area_volume_problem,
        generate_triangle_problem,
        generate_other_problem,
        generate_lottery_probability_problem,
        generate_card_probability_problem,
        generate_parallelogram_area_problem,
        generate_trapezoid_area_problem,
        generate_equation_transformation_problem,
        generate_quadratic_equation_problem,
        generate_right_triangle_hypotenuse_problem,
        generate_circle_circumference_problem,
        generate_similar_figures_area_ratio_problem,
        generate_cube_diagonal_length_problem,
        generate_cone_volume_problem,
        generate_system_of_equations_problem,
        generate_circle_equation_problem,
        generate_quadratic_vertex_problem,
        generate_cylinder_surface_area_problem,
        generate_triangle_angle_problem,
        generate_solid_volume_ratio_problem,
        generate_consecutive_integers_sum_problem,
        generate_composite_function_problem,
        generate_arithmetic_sequence_problem,
        generate_function_value_problem,
        generate_quadratic_max_min_problem,
        generate_combination_problem,
        generate_discriminant_problem,
        generate_lottery_conditional_probability_problem,
    ]
    problems = []
    for _ in range(n):
        generator = random.choice(problem_generators)
        text = ""
        problem, solution_steps = generator()
        text += "問題: "+problem+"\n"
        text += "回答\n"
        for step_idx, step in enumerate(solution_steps):
            text += (f"{step_idx + 1}: {step}\n")
        problems.append(text.strip())

    return problems


save_dir = "out_random2"
n_records = 10**2
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# ファイル名を現在の日付と時刻から生成
filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".jsonl"
filepath = os.path.join(save_dir, filename)

problem_list = [generate_problems(1)[0] for _ in tqdm(range(n_records))]
problem_list = list(set(problem_list))

with open(filepath, 'a', encoding='utf-8') as f:
    for t in tqdm(problem_list):
        d = {"text": t.strip()}
        json.dump(d, f, ensure_ascii=False)
        f.write("\n")
