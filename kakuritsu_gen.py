# %%
from tqdm import tqdm
import datetime
import json
import os
import itertools
import random


def generate_coin_problem_and_solution(num_coins, num_heads):
    num_tails = num_coins - num_heads
    problem_statement = f"コインを{num_coins}枚投げた時、{num_heads}枚が表で{num_tails}枚が裏である確率を求めよ。"
    total_outcomes = 2 ** num_coins
    all_outcomes = list(itertools.product('HT', repeat=num_coins))
    random.shuffle(all_outcomes)
    favorable_outcomes_list = [
        outcome for outcome in all_outcomes if outcome.count('H') == num_heads]
    favorable_outcomes = len(favorable_outcomes_list)
    probability = favorable_outcomes / total_outcomes
    favorable_outcomes_str = ', '.join(
        ''.join(outcome) for outcome in favorable_outcomes_list)

    steps = [
        f"1. コインを{num_coins}枚投げる全ての可能な結果の数を求めます。各コインには表(H)か裏(T)の2通りの結果があるので、全体の結果は 2^{num_coins} = {total_outcomes} 通りです。",
        f"2. 次に、{num_heads}枚が表で{num_tails}枚が裏になる結果の数を数えます。",
        f"3. {num_coins}枚のコインの全ての結果の組み合わせを生成し、その中で{num_heads}枚が表である結果の数を数えます。",
        f"4. {num_coins}枚のコインの全ての組み合わせの中で、{num_heads}枚が表である結果は {favorable_outcomes} 通りです。その組み合わせは次の通りです：{favorable_outcomes_str}",
        f"5. したがって、求める確率は {favorable_outcomes} / {total_outcomes} です。",
        f"6. 確率は {probability:.4f} です。"
    ]

    solution = "\n".join(steps)
    return problem_statement, solution


def generate_bead_problem_and_solution(num_beads, num_red):
    # Define possible colors and objects
    colors = [
        '赤', '青', '緑', '黄色', '紫', '橙', 'ピンク', '茶色', '黒', '白',
        '灰色', '金色', '銀色', 'ターコイズ', '紺色', 'オリーブ', 'シアン', 'マゼンタ', 'クリーム', 'ベージュ'
    ]

    objects = [
        'ビーズ', 'りんご', 'ボール', '石', 'ボタン', 'キューブ', 'キャンディ', 'シェル', 'コイン', 'マーブル',
        '葉っぱ', '花', 'ペン', '鍵', '時計', 'ネックレス', '靴', 'ハンカチ', '本', 'メガネ'
    ]

    # Randomly choose a color and an object
    color1, color2 = random.sample(colors, 2)
    object = random.choice(objects)

    num_color2 = num_beads - num_red
    problem_statement = f"袋の中に{color1}の{object}が{num_red}個、{color2}の{object}が{num_color2}個あります。この中から{num_beads}個の{object}を取り出すとき、ちょうど{num_red}個が{color1}で{num_color2}個が{color2}である確率を求めよ。"
    total_outcomes = 2 ** num_beads
    all_outcomes = list(itertools.product('01', repeat=num_beads))
    random.shuffle(all_outcomes)
    favorable_outcomes_list = [
        outcome for outcome in all_outcomes if outcome.count('0') == num_red]
    favorable_outcomes = len(favorable_outcomes_list)
    probability = favorable_outcomes / total_outcomes
    favorable_outcomes_str = ', '.join(
        ''.join(outcome) for outcome in favorable_outcomes_list)

    steps = [
        f"1. {num_beads}個の{object}を取り出す全ての可能な結果の数を求めます。各{object}は{color1}(0)か{color2}(1)の2通りの結果があるので、全体の結果は 2^{num_beads} = {total_outcomes} 通りです。",
        f"2. 次に、{num_red}個が{color1}で{num_color2}個が{color2}である結果の数を数えます。",
        f"3. {num_beads}個の{object}の全ての結果の組み合わせを生成し、その中で{num_red}個が{color1}である結果の数を数えます。",
        f"4. {num_beads}個の{object}の全ての組み合わせの中で、{num_red}個が{color1}である結果は {favorable_outcomes} 通りです。その組み合わせは次の通りです：{favorable_outcomes_str}",
        f"5. したがって、求める確率は {favorable_outcomes} / {total_outcomes} です。",
        f"6. 確率は {probability:.4f} です。"
    ]

    solution = "\n".join(steps)
    return problem_statement, solution


def generate_dice_problem_and_solution(num_dice, target_sum,):
    problem_type = random.choice(["equal", "greater_than_or_equal", "less_than_or_equal",
                                  # "odd_sum", "even_sum",
                                  "difference"])

    if problem_type == "equal":
        problem_statement = f"{num_dice}個のサイコロを振った時、出た目の合計が{target_sum}になる確率を求めよ。"
    elif problem_type == "greater_than_or_equal":
        problem_statement = f"{num_dice}個のサイコロを振った時、出た目の合計が{target_sum}以上になる確率を求めよ。"
    elif problem_type == "less_than_or_equal":
        problem_statement = f"{num_dice}個のサイコロを振った時、出た目の合計が{target_sum}以下になる確率を求めよ。"
    elif problem_type == "odd_sum":
        problem_statement = f"{num_dice}個のサイコロを振った時、出た目の合計が奇数になる確率を求めよ。"
    elif problem_type == "even_sum":
        problem_statement = f"{num_dice}個のサイコロを振った時、出た目の合計が偶数になる確率を求めよ。"
    else:  # difference
        diff = random.randint(0, num_dice*6)
        problem_statement = f"{num_dice}個のサイコロを振った時、出た目の最大値と最小値の差が{diff}になる確率を求めよ。"

    total_outcomes = 6 ** num_dice
    all_outcomes = list(itertools.product(range(1, 7), repeat=num_dice))
    random.shuffle(all_outcomes)

    if problem_type == "equal":
        favorable_outcomes_list = [
            outcome for outcome in all_outcomes if sum(outcome) == target_sum]
    elif problem_type == "greater_than_or_equal":
        favorable_outcomes_list = [
            outcome for outcome in all_outcomes if sum(outcome) >= target_sum]
    elif problem_type == "less_than_or_equal":
        favorable_outcomes_list = [
            outcome for outcome in all_outcomes if sum(outcome) <= target_sum]
    elif problem_type == "odd_sum":
        favorable_outcomes_list = [
            outcome for outcome in all_outcomes if sum(outcome) % 2 != 0]
    elif problem_type == "even_sum":
        favorable_outcomes_list = [
            outcome for outcome in all_outcomes if sum(outcome) % 2 == 0]
    else:  # difference
        favorable_outcomes_list = [
            outcome for outcome in all_outcomes if max(outcome) - min(outcome) == diff]

    favorable_outcomes = len(favorable_outcomes_list)
    probability = favorable_outcomes / total_outcomes
    favorable_outcomes_str = ', '.join(
        str(outcome) for outcome in favorable_outcomes_list)

    if problem_type == "equal":
        description = f"出た目の合計が{target_sum}になる"
    elif problem_type == "greater_than_or_equal":
        description = f"出た目の合計が{target_sum}以上になる"
    elif problem_type == "less_than_or_equal":
        description = f"出た目の合計が{target_sum}以下になる"
    elif problem_type == "odd_sum":
        description = "出た目の合計が奇数になる"
    elif problem_type == "even_sum":
        description = "出た目の合計が偶数になる"
    else:  # difference
        description = f"出た目の最大値と最小値の差が{diff}になる"

    steps = [
        f"1. {num_dice}個のサイコロを振る全ての可能な結果の数を求めます。各サイコロには1から6までの6通りの結果があるので、全体の結果は 6^{num_dice} = {total_outcomes} 通りです。",
        f"2. 次に、{description}結果の数を数えます。",
        f"3. {num_dice}個のサイコロの全ての結果の組み合わせを生成し、その中で{description}結果の数を数えます。",
        f"4. {num_dice}個のサイコロの全ての組み合わせの中で、{description}結果は {favorable_outcomes} 通りです。その組み合わせは次の通りです：{favorable_outcomes_str}",
        f"5. したがって、求める確率は {favorable_outcomes} / {total_outcomes} です。",
        f"6. 確率は {probability:.4f} です。"
    ]

    solution = "\n".join(steps)
    return problem_statement, solution


# Function to randomly choose a problem type and generate the problem and solution
def generate_random_problem_and_solution():
    problem_types = [generate_coin_problem_and_solution,
                     generate_bead_problem_and_solution, generate_dice_problem_and_solution]
    chosen_problem_type = random.choice(problem_types)

    if chosen_problem_type == generate_coin_problem_and_solution:
        num_coins = random.randint(3, 6)
        num_heads = random.randint(0, num_coins)
        return chosen_problem_type(num_coins, num_heads)
    elif chosen_problem_type == generate_bead_problem_and_solution:
        num_beads = random.randint(3, 6)
        num_red = random.randint(0, num_beads)
        return chosen_problem_type(num_beads, num_red)
    elif chosen_problem_type == generate_dice_problem_and_solution:
        num_dice = random.randint(1, 2)
        target_sum = random.randint(num_dice, num_dice * 6)
        return chosen_problem_type(num_dice, target_sum)

# Example of generating multiple random problems and solutions


def gen():
    text = ""
    questions, answers = generate_random_problem_and_solution()
    text += "問題: "+(questions)+"\n"
    text += "回答: "+(answers)+"\n\n"

    return text.strip()


# %%

save_dir = "out_kakuritsu"
n_records = 10**2
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# ファイル名を現在の日付と時刻から生成
filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".jsonl"
filepath = os.path.join(save_dir, filename)

problem_list = [gen() for _ in tqdm(range(n_records))]
problem_list = list(set(problem_list))

with open(filepath, 'a', encoding='utf-8') as f:
    for d in tqdm(problem_list):
        d = {"text": d}
        json.dump(d, f, ensure_ascii=False)
        f.write("\n")


# %%
