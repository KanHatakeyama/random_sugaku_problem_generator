
import random

def generate_random_expression():
    operators = ['+', '-', '*', '/']
    expression = []
    step_by_step = []

    # 数値の範囲を選択する確率を設定
    ranges = [(-10, 10), (-100, 100), (-1000, 1000)]
    range_choice = random.choice(ranges)
    
    # 初期の数値を選択
    current_value = random.randint(*range_choice)
    expression.append(str(current_value))
    step_by_step.append(f"初期値: {current_value}")

    # ランダムに操作を追加
    num_operations = random.randint(1, 7)
    for _ in range(num_operations):
        operator = random.choice(operators)
        number = random.randint(*range_choice)

        # マイナスの数値の掛け算・割り算には括弧を追加
        if number < 0 and operator in ['*', '/']:
            expression.append(operator)
            expression.append(f"({number})")
        else:
            expression.append(operator)
            expression.append(str(number))

    return ' '.join(expression), step_by_step

def evaluate_expression(expression):
    tokens = expression.split()
    step_by_step = []

    # 掛け算と割り算を優先して計算
    i = 0
    while i < len(tokens):
        if tokens[i] in ['*', '/']:
            prev_value = float(tokens[i-1])
            next_value = float(tokens[i+1].strip('()'))  # 括弧を除去
            if tokens[i] == '*':
                result = prev_value * next_value
                rounded_result = int(result) if result.is_integer() else round(result, 2)
                step_by_step.append(f"掛け算: {prev_value} * {next_value} = {rounded_result}")
            else:
                if next_value != 0:
                    result = prev_value / next_value
                    rounded_result = int(result) if result.is_integer() else round(result, 2)
                    step_by_step.append(f"割り算: {prev_value} / {next_value} = {rounded_result}")
                else:
                    step_by_step.append("割り算エラー: 0 で割ることはできません")
                    return "エラー: 0 で割ることはできません。", step_by_step
            tokens[i-1:i+2] = [str(rounded_result)]
            i -= 1
        i += 1

    # 次に加算と減算を計算
    result = float(tokens[0])
    i = 1
    while i < len(tokens):
        if tokens[i] == '+':
            temp_result = result
            result = result + float(tokens[i+1])
            rounded_result = int(result) if result.is_integer() else round(result, 2)
            step_by_step.append(f"加算: {temp_result} + {tokens[i+1]} = {rounded_result}")
        elif tokens[i] == '-':
            temp_result = result
            result = result - float(tokens[i+1])
            rounded_result = int(result) if result.is_integer() else round(result, 2)
            step_by_step.append(f"減算: {temp_result} - {tokens[i+1]} = {rounded_result}")
        i += 2

    final_result = int(result) if result.is_integer() else round(result, 2)
    return final_result, step_by_step

def generate_arithmetic_problem():
    expression, initial_steps = generate_random_expression()
    result, steps = evaluate_expression(expression)

    problem_text = f"問題:\n次の計算を行いなさい。\n{expression}\n"
    answer_text = "\n解答:\n"
    answer_text += f"式: {expression}\n"
    answer_text += "\n計算過程:\n"
    answer_text += "\n".join(steps)
    answer_text += f"\n最終結果: {result}"

    return problem_text + answer_text
