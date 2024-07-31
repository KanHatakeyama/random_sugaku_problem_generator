
import random
import sympy as sp


def generate_linear_equation():
    # ランダムな係数と定数項を生成
    a1 = random.randint(-100, 100)
    b1 = random.randint(-100, 100)
    a2 = random.randint(-100, 100)
    b2 = random.randint(-100, 100)

    x = sp.symbols('x')

    # 方程式の左辺と右辺
    lhs = a1 * x + b1
    rhs = a2 * x + b2

    # 方程式を解く
    equation = lhs - rhs
    solution = sp.solve(equation, x)

    return lhs, rhs, equation, solution


def format_equation(lhs, rhs):
    return f"{lhs} = {rhs}"
    return f"{sp.pretty(lhs)} = {sp.pretty(rhs)}"


def generate_ichiji_hoteshiki():
    lhs, rhs, equation, solution = generate_linear_equation()

    problem_text = "問題:\n次の方程式を解きなさい。\n"
    problem_text += format_equation(lhs, rhs)

    # 解を導くステップの記載
    steps = []
    # 方程式の標準形
    standard_form = lhs - rhs
    # steps.append(f"初めに方程式を標準形にします:\n   {sp.pretty(standard_form)} = 0")

    # 簡略化のための操作
    simplified = sp.simplify(standard_form)
    steps.append(f"方程式を簡略化します:\n   {sp.pretty(simplified)} = 0\n")

    # 両辺を共通の係数で割る操作
    coeff_x = sp.LC(simplified, sp.symbols('x'))
    if coeff_x != 0 and coeff_x != 1:
        simplified = simplified / coeff_x
        steps.append(f"両辺を {coeff_x} で割ります:\n   {(simplified)} = 0\n")

    # 方程式を解く過程の記載
    answer_text = "\n\n解答:\n"
    for step in steps:
        answer_text += step + "\n"

    # if solution:
    #    answer_text += f"最後に、x の解を求めます:\n   x = {solution[0]}"
    # else:
    #    answer_text += "等式が満たされていないので､この方程式の解は存在しないことが分かりました｡"
    if solution:
        solution_fraction = solution[0].evalf()
        solution_decimal = float(solution_fraction)
        rounded_solution = round(solution_decimal, 2)
        answer_text += f"最後に、x の解を求めます:\n   x = {solution[0]} ({rounded_solution})"
    else:
        answer_text += "解がありません。"
    return problem_text + answer_text
