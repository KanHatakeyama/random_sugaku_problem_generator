
import random
import sympy as sp


def generate_random_expression():
    operators = ['+', '-', '*']
    num_terms = random.randint(2, 6)  # 2から4つの項を持つ式を作成
    expression = 0
    variables = []

    for _ in range(num_terms):
        coef = random.randint(-10, 10)  # ランダムな係数
        var = chr(random.randint(97, 122))  # ランダムな変数 (a-z)

        while var in variables:
            var = chr(random.randint(97, 122))  # 重複を避ける

        variables.append(var)
        sym_var = sp.symbols(var)

        term = coef * sym_var
        if expression == 0:
            expression = term
        else:
            op = random.choice(operators)
            if op == '+':
                expression += term
            elif op == '-':
                expression -= term
            elif op == '*':
                expression *= term

    return expression, variables


def evaluate_expression(expression, values):
    return expression.subs(values)


def generate_takoshiki_dainyu_problem():
    expression, variables = generate_random_expression()
    values = {var: random.randint(-10, 10) for var in variables}
    answer = evaluate_expression(expression, values)

    variables_text = ", ".join(
        [f"{var}={value}" for var, value in values.items()])
    problem_text = f"問題:\n{variables_text} のとき，次の式の値を求めなさい。\n"
    problem_text += f"{sp.pretty(expression)}"

    # ステップごとの計算過程を解答に含める
    steps = []
    substituted_expression = expression
    for var, value in values.items():
        step = f"{sp.pretty(substituted_expression)} について、{var} に {value} を代入すると､以下の式が得られます。"
        substituted_expression = substituted_expression.subs(
            sp.symbols(var), value)
        step += f"\n{sp.pretty(substituted_expression)}"
        steps.append(step)

    answer_text = "\n\n解答:\n"
    answer_text += f"式: {sp.pretty(expression)} を計算します。\n"
    answer_text += f"\n{variables_text} を式に代入していきます。\n"
    for step in steps:
        answer_text += f"{step}\n\n"
    answer_text += f"よって、最終的な値は {answer} です。\n"

    return problem_text + answer_text
