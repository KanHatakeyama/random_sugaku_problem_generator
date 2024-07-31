from sympy import Rational, N
import random

# ランダムな数値を生成する関数


def generate_random_number():
    return round(random.uniform(-100, 100), 1)

# 数値を四捨五入する関数


def rounded(number, digits=1):
    return round(float(number), digits)

# 問題と回答を生成する関数


def generate_seifu_problem():
    n_problems = random.randint(1, 10)
    digit = random.randint(0, 2)
    base_numbers = [Rational(generate_random_number())
                    for _ in range(n_problems)]
    diff_numbers = [Rational(generate_random_number())
                    for _ in range(n_problems)]

    problems = ["次の数を求めなさい。"]
    solutions = []

    for i in range(n_problems):
        base = rounded(base_numbers[i], digit)
        diff = rounded(abs(diff_numbers[i]), digit)
        operation = "大きい" if diff_numbers[i] > 0 else "小さい"
        base_sign = "+" if base_numbers[i] >= 0 else "-"
        diff_sign = "+" if diff_numbers[i] >= 0 else "-"
        result = rounded(base_numbers[i] + diff_numbers[i], digit)

        # 問題の作成
        problems.append(f"({i+1}) {base} より {diff} {operation}数")

        # 解答の作成
        intermediate_calculation = f"{base_sign}{abs(base)} {diff_sign} {abs(diff)}"
        solutions.append(
            f"({i+1}) {intermediate_calculation} = {result}"
        )
    problems = "\n".join(problems)
    solutions = "\n".join(solutions)
    return f"""問題: \n{problems}\n\n解答: \n{solutions}"""


def generate_product_problem_and_answer_seki():
    # 整数の積を求める
    target_product = random.randint(-50, 50)
    while target_product == 0:  # 0だと組み合わせが無限になるため避ける
        target_product = random.randint(-50, 50)

    pairs = set()  # 重複を避けるためセットを使用

    # 1からtarget_productの絶対値の平方根までの範囲でループ
    for i in range(1, int(abs(target_product) ** 0.5) + 1):
        if target_product % i == 0:
            # 商を求める
            j = target_product // i
            # i, jおよびその逆のペアをセットに追加
            pairs.add((i, j))
            pairs.add((-i, -j))
            pairs.add((-i, j))
            pairs.add((i, -j))

    # 重複を避けるためソートして正規化
    unique_pairs = set(tuple(sorted(pair)) for pair in pairs)

    filtered_pairs = []
    for pair in unique_pairs:
        if pair[0]*pair[1] == target_product:
            filtered_pairs.append(pair)
    unique_pairs = filtered_pairs

    problem_text = f"問題:\n積が {target_product} となる 2 つの整数の組をすべて求めなさい｡ただし，数の並び順は考えないものとします。"
    answer_text = "\n\n解答:\n"
    answer_text += f"積が {target_product} となる整数の組は次の通りです:\n"
    answer_text += ", ".join([f"({a}, {b})" for a, b in unique_pairs]) + "\n"

    return problem_text + answer_text

def generate_product_problem_and_answer_seki_count():
    # 整数の積を求める
    target_product = random.randint(-50, 50)
    while target_product == 0:  # 0だと組み合わせが無限になるため避ける
        target_product = random.randint(-50, 50)

    pairs = set()  # 重複を避けるためセットを使用

    # 1からtarget_productの絶対値の平方根までの範囲でループ
    for i in range(1, int(abs(target_product) ** 0.5) + 1):
        if target_product % i == 0:
            # 商を求める
            j = target_product // i
            # i, jおよびその逆のペアをセットに追加
            pairs.add((i, j))
            pairs.add((-i, -j))
            pairs.add((-i, j))
            pairs.add((i, -j))

    # 重複を避けるためソートして正規化
    unique_pairs = set(tuple(sorted(pair)) for pair in pairs)

    filtered_pairs = []
    for pair in unique_pairs:
        if pair[0]*pair[1] == target_product:
            filtered_pairs.append(pair)
    unique_pairs = filtered_pairs

    problem_text = f"問題:\n積が {target_product} となる 2 つの整数の組はいくつあるか?｡ただし，数の並び順は考えないものとする。"
    answer_text = "\n\n解答:\n"
    answer_text += f"積が {target_product} となる整数の組は次の通りです:\n"
    answer_text += ", ".join([f"({a}, {b})" for a, b in unique_pairs]) + "\n"
    answer_text += f"したがって，積が {target_product} となる整数の組は {len(unique_pairs)} 組です。"

    return problem_text + answer_text





def generate_mean_problem_and_answer():
    # ランダムに生成する数値の範囲と個数
    num_numbers = random.randint(3, 10)  # 5から10個の数値を生成
    min_value = -100  # 数値の最小値
    max_value = 100  # 数値の最大値

    # ランダムな整数のリストを生成
    numbers = [random.randint(min_value, max_value)
               for _ in range(num_numbers)]

    # 平均値の計算
    mean_value = sum(numbers) / len(numbers)

    # 問題文の作成
    problem_text = f"問題:\n次のデータの平均値を求めなさい\n点数: {', '.join(map(str, numbers))}"

    # 解答文の作成
    answer_text = f"\n\n解答:\n"
    answer_text += f"データの合計は {sum(numbers)} で、個数は {len(numbers)} です。\n"
    answer_text += f"したがって、平均値は {sum(numbers)} / {len(numbers)} = {mean_value:.2f} です。\n"

    return problem_text + answer_text
