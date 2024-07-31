import random


def generate_comparison_problems(num_problems):
    problems = []
    for _ in range(num_problems):
        digit = random.randint(0, 4)
        num1 = round(random.uniform(-100, 100), digit)
        digit = random.randint(0, 4)
        num2 = round(random.uniform(-100, 100), digit)
        problems.append((num1, num2))
    return problems


def format_problem(num1, num2):
    return f"{num1:+.2f}，{num2:+.2f}"


def compare_numbers(num1, num2):
    if num1 > num2:
        return ">"
    elif num1 < num2:
        return "<"
    else:
        return "="


def generate_problem_and_answer_futogo():
    num_problems = random.randint(2, 10)
    problems = generate_comparison_problems(num_problems)
    problem_text = "問題:\n不等号を使って2つの数値の関係を表しなさい。\n"
    answer_text = "\n解答:\n"

    for i, (num1, num2) in enumerate(problems, 1):
        problem_text += f"({i}) {format_problem(num1, num2)}\n"
        if num1 == num2:
            continue
        comparison = compare_numbers(num1, num2)
        explanation = f"{num1:+.2f} は {num2:+.2f} よりも {'大きい' if comparison == '>' else '小さい'}です。"
        answer_text += f"({i}) {explanation}よって {num1:+.2f} {comparison} {num2:+.2f} が成立します。\n"

    return problem_text + answer_text
