import random
import sympy as sp


def generate_random_expression():
    operators = ['+', '-', '*']
    num_terms = random.randint(2, 4)  # 2から4つの項を持つ式を作成
    expression = 0
    variables = []

    for _ in range(num_terms):
        coef = random.randint(-10, 10)  # ランダムな係数
        var = chr(random.randint(97, 122))  # ランダムな変数 (a-z)

        while var in variables:
            var = chr(random.randint(97, 122))  # 重複を避ける

        variables.append(var)
        sym_var = sp.symbols(var)

        # 2乗項の追加
        if random.choice([True, False]):
            term = coef * sym_var**2
        else:
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


def format_expression(expression):
    formatted = str(expression).replace("**2", "^2")
    return formatted


def evaluate_expression(expression, values):
    return expression.subs(values)


def generate_dainyu_problem_jijo():
    expression, variables = generate_random_expression()
    values = {var: random.randint(-10, 10) for var in variables}
    answer = evaluate_expression(expression, values)

    variables_text = ", ".join(
        [f"{var}={value}" for var, value in values.items()])
    problem_text = f"問題:\n{variables_text} のとき，次の式の値を求めなさい。\n\n"
    problem_text += format_expression(expression)

    # ステップごとの計算過程を解答に含める
    steps = []
    substituted_expression = expression
    for var, value in values.items():
        step = f"{format_expression(substituted_expression)}について、{var} に {value} を代入すると､以下の式が得られます。"
        substituted_expression = substituted_expression.subs(
            sp.symbols(var), value)
        step += f"\n{format_expression(substituted_expression)}"
        steps.append(step)

    answer_text = "\n解答:\n"
    answer_text += f"式: {format_expression(expression)} を計算します。\n"
    answer_text += f"\n{variables_text} を式に代入していきます。\n"
    for step in steps:
        answer_text += f"{step}\n\n"
    answer_text += f"よって、最終的な値は {answer} です。\n"

    return problem_text + answer_text
