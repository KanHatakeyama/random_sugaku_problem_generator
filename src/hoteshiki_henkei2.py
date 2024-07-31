import random
import sympy as sp
import string

def generate_random_polynomial(max_degree=2):
    # ランダムな数の変数を選ぶ（2〜5）
    num_vars = random.randint(2, 5)
    # ランダムな変数のアルファベットを選ぶ
    selected_variables = random.sample(string.ascii_lowercase, num_vars)
    solve_for = random.choice(selected_variables)
    
    # ランダムな係数を生成（数値または変数）
    coefficients = []
    for _ in range(num_vars):
        if random.choice([True, False]):
            coefficients.append(sp.Symbol(random.choice(string.ascii_lowercase)))
        else:
            coefficients.append(random.randint(-10, 10))
    
    symbols = sp.symbols(selected_variables)
    
    # ランダムに次数を決定（0からmax_degreeの範囲で設定）
    degrees = [random.randint(0, max_degree) for _ in range(num_vars)]

    # 方程式の左辺の生成
    lhs = sum(coeff * sym**deg for coeff, sym, deg in zip(coefficients, symbols, degrees))
    rhs = random.randint(-20, 20)
    
    # 特定の変数について方程式を解く
    solution = sp.solve(lhs - rhs, sp.symbols(solve_for))
    
    return lhs, rhs, coefficients, symbols, solve_for, solution

def format_equation(lhs, rhs, solve_for):
    return f"{lhs} = {rhs} を {solve_for} について解きなさい。"

def generate_transformation_problem_polynomial():
    lhs, rhs, coefficients, symbols, solve_for, solution = generate_random_polynomial()

    problem_text = ""
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
    if not any(solve_for_symbol in term.free_symbols for term in lhs_isolated.args):
        answer_text += f"方程式には {solve_for} が含まれていません。\n"
        return problem_text + answer_text

    answer_text += f"2. {solve_for} について解くために、他の項を移項し整理します:\n"
    answer_text += f"   {lhs_isolated} = 0\n"

    # ステップ3: 両辺を係数で割る
    coefficient = sp.LC(lhs_isolated, solve_for_symbol)
    if coefficient != 1 and coefficient != 0:
        lhs_isolated = lhs_isolated / coefficient
        answer_text += f"3. {solve_for} の項の係数 {coefficient} で両辺を割ります:\n"
        answer_text += f"   {lhs_isolated} = 0\n"

    # ステップ4: 方程式を解く
    solution = sp.solve(lhs_isolated, solve_for_symbol)
    answer_text += f"4. 最終的に、{solve_for} の解を求めた結果は以下の通りになります:\n   {solve_for} = {solution}\n"

    return problem_text + answer_text

# 実行例
