
import random
import sympy as sp
import string


def generate_random_equation():
    # ランダムな変数のアルファベットを2つ選ぶ
    selected_variables = random.sample(string.ascii_lowercase, 2)
    solve_for = random.choice(selected_variables)

    # ランダムな係数と次数を決定
    max_degree = 2
    coefficients = [random.randint(-10, 10) for _ in range(max_degree + 1)]
    while coefficients[0] == 0:
        coefficients[0] = random.randint(-10, 10)  # 最高次の係数は0でないようにする

    symbols = sp.symbols(selected_variables)

    # 方程式の左辺の生成
    lhs = sum(coeff * sym**deg for coeff, sym,
              deg in zip(coefficients, symbols, range(max_degree, -1, -1)))
    rhs = random.randint(-20, 20)

    # 特定の変数について方程式を解く
    solution = sp.solve(lhs - rhs, sp.symbols(solve_for))

    return lhs, rhs, symbols, solve_for, solution


def format_equation(lhs, rhs, solve_for):
    return f"{lhs} = {rhs} を {solve_for} について解きなさい。"


def generate_transformation_problem_niji():
    lhs, rhs, symbols, solve_for, solution = generate_random_equation()

    problem_text = "次の等式を # の中の文字について解きなさい。\n"
    problem_text += format_equation(lhs, rhs, solve_for)

    # 解答の詳細
    answer_text = "\n\n解答:\n"
    answer_text += f"式: {lhs} = {rhs}\n"

    # ステップ1: 方程式の標準形への変形
    standard_form = lhs - rhs
    answer_text += f"1. 方程式を標準形にします:\n   {standard_form} = 0\n"

    # ステップ2: 特定の変数について解くために他の項を移項し整理
    solve_for_symbol = sp.symbols(solve_for)
    lhs_isolated = sp.collect(standard_form, solve_for_symbol)
    # answer_text += f"2. {solve_for} について解くために、他の項を移項し整理します:\n"
    # answer_text += f"   {lhs_isolated} = 0\n"

    # ステップ3: 両辺を係数で割る
    coefficient = sp.LC(lhs_isolated, solve_for_symbol)
    if coefficient != 1 and coefficient != 0:
        lhs_isolated = lhs_isolated / coefficient
        answer_text += f"2. {solve_for} の項の係数 {coefficient} で両辺を割ります:\n"
        answer_text += f"   {lhs_isolated} = 0\n"

    # ステップ4: 方程式を解く
    solution = sp.solve(lhs_isolated, solve_for_symbol)
    answer_text += f"3. 最終的に、{solve_for} の解を求めた結果は以下の通りになります:\n   {solve_for} = {solution}\n"

    return problem_text + answer_text
