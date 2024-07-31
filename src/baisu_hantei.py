
import random

def generate_integer_sequence(length=20, min_val=1, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(length)]

def is_multiple(num, multiple):
    return num % multiple == 0

def generate_baisu_count_problem():
    # ランダムな整数列を生成
    sequence_length = random.randint(3, 15)  # 数列の長さをランダムに決定
    sequence = generate_integer_sequence(sequence_length)

    # ランダムに選んだ2から9の倍数を探す
    multiple = random.randint(2, 9)
    multiples_in_sequence = []
    step_by_step = []

    # 各数値について倍数かどうかを判定し、割り算を行う
    for num in sequence:
        quotient, remainder = divmod(num, multiple)
        if is_multiple(num, multiple):
            multiples_in_sequence.append(num)
            step_by_step.append(f"{num} は {multiple} の倍数です(商: {quotient}, 余り: {remainder})。")
        else:
            step_by_step.append(f"{num} は {multiple} の倍数ではありません(商: {quotient}, 余り: {remainder})。")

    multiple_count = len(multiples_in_sequence)

    problem_text = f"問題:\n次の整数列の中から、{multiple} の倍数を探し、その数を数えなさい。\n"
    problem_text += f"{sequence}\n"

    answer_text = "\n解答:\n"
    answer_text += "一つ一つの数値について、倍数であるかどうかを判定していきます。\n"
    answer_text += "\n".join(step_by_step)
    if multiple_count == 0:
        answer_text += f"\n\n以上より、{multiple} の倍数は見つかりませんでした。\n"
    else:
        answer_text += f"\n\n以上より、{multiple} の倍数は次の通りです: {multiples_in_sequence}\n"
        answer_text += f"合計 {multiple_count} 個の {multiple} の倍数があります。\n"

    return problem_text + answer_text
