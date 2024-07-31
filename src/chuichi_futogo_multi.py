import random


def generate_numbers_with_random_precision(num_numbers):
    numbers = []
    for _ in range(num_numbers):
        number = random.uniform(-10, 10)
        precision = random.randint(0, 3)  # 小数点以下の桁数を0から3の間でランダムに選択
        number = round(number, precision)
        numbers.append(number)
    return numbers


def format_numbers(numbers):
    formatted_numbers = []
    for num in numbers:
        if isinstance(num, float) and num.is_integer():
            formatted_numbers.append(f"{int(num):+}")
        else:
            formatted_numbers.append(
                f"{num:+.2f}" if isinstance(num, float) else f"{num:+.0f}")
    return "，".join(formatted_numbers)


def create_inequality(numbers):
    sorted_numbers = sorted(numbers)
    formatted_numbers = []
    for num in sorted_numbers:
        if isinstance(num, float) and num.is_integer():
            formatted_numbers.append(f"{int(num):+}")
        else:
            formatted_numbers.append(
                f"{num:+.2f}" if isinstance(num, float) else f"{num:+.0f}")
    return " < ".join(formatted_numbers)


def create_inequality_suretsu(numbers):
    sorted_numbers = sorted(numbers)
    formatted_numbers = []
    for num in sorted_numbers:
        if isinstance(num, float) and num.is_integer():
            formatted_numbers.append(f"{int(num):+}")
        else:
            formatted_numbers.append(
                f"{num:+.2f}" if isinstance(num, float) else f"{num:+.0f}")
    return " , ".join(formatted_numbers)


def create_inequality_suretsu2(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    formatted_numbers = []
    for num in sorted_numbers:
        if isinstance(num, float) and num.is_integer():
            formatted_numbers.append(f"{int(num):+}")
        else:
            formatted_numbers.append(
                f"{num:+.2f}" if isinstance(num, float) else f"{num:+.0f}")
    return " , ".join(formatted_numbers)


def generate_inequality_problem_and_answer():
    num_numbers = random.randint(3, 10)  # 3から10個の数値をランダムに生成
    numbers = generate_numbers_with_random_precision(num_numbers)
    problem_text = f"問題:\n以下の数値を用いて不等式を作りなさい。\n{format_numbers(numbers)}\n"
    answer_text = f"\n解答:\nこれらの数値を使って不等式を作るには、数値を小さい順に並べ、大小関係を示します。\n{create_inequality(numbers)}\n"
    return problem_text + answer_text


def generate_sort_problem_and_answer():
    num_numbers = random.randint(3, 10)  # 3から10個の数値をランダムに生成
    numbers = generate_numbers_with_random_precision(num_numbers)
    problem_text = f"問題:\n以下の数値を小さい順に並べ替えなさい。\n{format_numbers(numbers)}\n"
    answer_text = f"\n解答:\nこれらの数値を小さい順に並べ替えた数列は以下の通りです。\n{create_inequality_suretsu(numbers)}\n"
    return problem_text + answer_text


def generate_sort_problem_and_answer2():
    num_numbers = random.randint(3, 10)  # 3から10個の数値をランダムに生成
    numbers = generate_numbers_with_random_precision(num_numbers)
    problem_text = f"問題:\n以下の数値を大きい順に並べ替えなさい。\n{format_numbers(numbers)}\n"
    answer_text = f"\n解答:\nこれらの数値を大きい順に並べ替えた数列は以下の通りです。\n{create_inequality_suretsu2(numbers)}\n"
    return problem_text + answer_text


def generate_nth_largest_problem_and_answer():
    num_numbers = random.randint(3, 10)
    n = random.randint(1, num_numbers)
    numbers = generate_numbers_with_random_precision(num_numbers)
    sorted_numbers = sorted(numbers, reverse=True)
    nth_largest = sorted_numbers[n - 1]

    problem_text = f"問題:\n以下の数列の中から {n} 番目に大きい数を見つけなさい。\n{format_numbers(numbers)}\n"
    answer_text = f"\n解答:\n"
    answer_text += f"はじめに､数列を大きい順に並べます。\n{create_inequality_suretsu2(numbers)}\n"
    if int(nth_largest) == float(nth_largest):
        nth_largest = int(nth_largest)
        answer_text += f"次に､並べた数列の中から {n} 番目に大きい数を見つけます。\nよって､{n} 番目に大きい数は {nth_largest} です。\n"
    else:
        answer_text += f"次に､並べた数列の中から {n} 番目に大きい数を見つけます。\nよって､{n} 番目に大きい数は {nth_largest:+.2f} です。\n"

    return problem_text + answer_text


def generate_nth_smallest_problem_and_answer():
    num_numbers = random.randint(3, 10)
    n = random.randint(1, num_numbers)
    numbers = generate_numbers_with_random_precision(num_numbers)
    sorted_numbers = sorted(numbers)
    nth_smallest = sorted_numbers[n - 1]

    problem_text = f"問題:\n以下の数列の中から {n} 番目に小さい数を見つけなさい。\n{format_numbers(numbers)}\n"
    answer_text = f"\n解答:\n"
    answer_text += f"はじめに､数列を小さい順に並べます。\n{create_inequality_suretsu(numbers)}\n"
    if int(nth_smallest) == float(nth_smallest):
        nth_smallest = int(nth_smallest)
        answer_text += f"次に､並べた数列の中から {n} 番目に小さい数を見つけます。\nよって､{n} 番目に小さい数は {nth_smallest} です。\n"
    else:
        answer_text += f"次に､並べた数列の中から {n} 番目に小さい数を見つけます。\nよって､{n} 番目に小さい数は {nth_smallest:+.2f} です。\n"

    return problem_text + answer_text


def generate_largest_number_problem_and_answer():
    num_numbers = random.randint(3, 10)
    numbers = generate_numbers_with_random_precision(num_numbers)
    largest_number = max(numbers)

    problem_text = f"問題:\n以下の数列の中から最も大きな数を見つけなさい。\n{format_numbers(numbers)}\n"
    answer_text = f"\n解答:\n"
    answer_text += f"はじめに､数列を大きい順に並べてみます。\n{create_inequality_suretsu2(numbers)}\n"
    if int(largest_number) == float(largest_number):
        largest_number = int(largest_number)
        answer_text += f"この数列より､最も大きな数は {largest_number} であることが分かります。"
    else:
        answer_text += f"この数列より､最も大きな数は {largest_number:+.2f} であることが分かります。"

    return problem_text + answer_text


def generate_smallest_number_problem_and_answer():
    num_numbers = random.randint(3, 10)
    numbers = generate_numbers_with_random_precision(num_numbers)
    smallest_number = min(numbers)

    problem_text = f"問題:\n以下の数列の中から最も小さな数を見つけなさい。\n{format_numbers(numbers)}\n"
    answer_text = f"\n解答:\n"
    answer_text += f"はじめに､数列を小さい順に並べてみます。\n{create_inequality_suretsu(numbers)}\n"
    if int(smallest_number) == float(smallest_number):
        smallest_number = int(smallest_number)
        answer_text += f"この数列より､最も小さな数は {smallest_number} です。"
    else:
        answer_text += f"この数列より､最も小さな数は  {smallest_number:+.2f} です。"

    return problem_text + answer_text


def generate_range_problem_and_answer():
    lower_bound = round(random.uniform(-10, 10), 1)
    upper_bound = round(random.uniform(lower_bound, 10), 1)

    while lower_bound == upper_bound:
        upper_bound = round(random.uniform(lower_bound, 10), 1)

    # lower_bound より大きく、upper_bound より小さい整数を探す
    lower_int = int(lower_bound) + \
        1 if lower_bound % 1 != 0 else int(lower_bound) + 1
    upper_int = int(upper_bound) if upper_bound % 1 != 0 else int(
        upper_bound) - 1

    # 範囲内のすべての整数をリスト化
    integer_list = list(range(lower_int, upper_int + 1))

    problem_text = f"問題:\n{lower_bound} より大きく，{upper_bound} より小さいすべての整数xを見つけなさい。"
    answer_text = f"\n\n解答:\n"
    answer_text += f"はじめに、与えられた範囲を確認します。\n"
    answer_text += f"{lower_bound} より大きい整数は {lower_int} から始まります。\n"
    answer_text += f"{upper_bound} より小さい整数は {upper_int} で終わります。\n\n"

    if len(integer_list) == 0:
        answer_text += f"したがって、{lower_bound} より大きく {upper_bound} より小さい整数xは存在しません。\n"
        return problem_text + answer_text

    answer_text += f"したがって、{lower_bound} より大きく {upper_bound} より小さいすべての整数xは次の通りです。\n"
    answer_text += ", ".join(map(str, integer_list)) + "\n"

    return problem_text + answer_text


def generate_inequality_problem_and_answer_futoshiki():
    lower_bound = round(random.uniform(-10, 10), 1)
    upper_bound = round(random.uniform(lower_bound, 10), 1)

    while lower_bound == upper_bound:
        upper_bound = round(random.uniform(lower_bound, 10), 1)

    # lower_bound より大きく、upper_bound より小さい整数を探す
    lower_int = int(lower_bound) + \
        1 if lower_bound % 1 != 0 else int(lower_bound) + 1
    upper_int = int(upper_bound) if upper_bound % 1 != 0 else int(
        upper_bound) - 1

    # 範囲内のすべての整数をリスト化
    integer_list = list(range(lower_int, upper_int + 1))

    problem_text = f"問題:\n不等式 {lower_bound} < x < {upper_bound} を満たす全ての整数xを見つけなさい。"
    answer_text = f"\n\n解答:\n"
    answer_text += f"はじめに、与えられた範囲を確認します。\n"
    answer_text += f"{lower_bound} より大きい整数は {lower_int} から始まります。\n"
    answer_text += f"{upper_bound} より小さい整数は {upper_int} で終わります。\n\n"
    if len(integer_list) == 0:
        answer_text += f"したがって、{lower_bound} より大きく {upper_bound} より小さい整数xは存在しません。\n"
        return problem_text + answer_text
    answer_text += f"したがって、{lower_bound} < x < {upper_bound} を満たすすべての整数xは次の通りです。\n"
    answer_text += ", ".join(map(str, integer_list)) + "\n"

    return problem_text + answer_text
