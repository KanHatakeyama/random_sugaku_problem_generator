# %%
import pandas as pd
import numpy as np
import random
import string
import re
from tqdm import tqdm
import json
import datetime
import os
import time

# ランダムなラベル名を生成する関数
def random_label():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

# データの種類をランダムに決める関数
def random_data_type(num_rows):
    data_type = random.choice(['float', 'int', 'neg_int', 'neg_float'])
    if data_type == 'float':
        return np.round(np.random.uniform(0, 400, size=num_rows), 2)
    elif data_type == 'int':
        return np.random.randint(0, 1000, size=num_rows)
    elif data_type == 'neg_int':
        return np.random.randint(-500, 500, size=num_rows)
    elif data_type == 'neg_float':
        return np.round(np.random.uniform(-200, 200, size=num_rows), 2)

def gen():
    # 行数と列数をランダムに決定
    num_rows = random.randint(5, 10)
    num_cols = random.randint(3, 7)

    # ラベル名を格納するリスト
    labels = []

    # データフレームの辞書を初期化
    data = {}

    # ランダムに日付を使用するかどうかを決定
    use_date = random.choice([True, False])

    # 日付を使用する場合
    if use_date:
        start_date = pd.to_datetime('2022-01-01')
        end_date = pd.to_datetime('2023-01-01')
        dates = pd.to_datetime(np.random.randint(start_date.value, end_date.value, num_rows)).normalize()
        data['date'] = dates
        labels.append('date')

    # 他のラベルとデータを追加
    for _ in range(num_cols):
        label = random_label()
        while label in labels:
            label = random_label()
        labels.append(label)
        data[label] = random_data_type(num_rows)

    # 読解問題をランダムに生成する関数
    def generate_questions(df):
        questions = []
        answers = []

        cols = df.columns.tolist()
        
        # 1. 列Xの平均値を求めよ
        col = random.choice(cols[1:])  # 日付列がある場合を除外
        values = df[col].values
        mean_value = df[col].mean()
        max_value = df[col].max()
        min_value = df[col].min()
        sum_value = df[col].sum()
        questions.append(f"・列{col}の平均値、最大値、最小値を求めよ")
        answers.append(f"各値は以下の計算式で求められます。\n"
                    f"平均値 = （全ての値の合計） / （値の数）\n"
                    f"つまり、\n"
                    f"{values} の合計 / {len(values)} = {sum_value} / {len(values)} = {mean_value:.2f}\n"
                    f"最大値 = {values.max()}\n"
                    f"最小値 = {values.min()}")

        # 2. 列Yが最小を取るdateはいつか? (日付列がある場合)
        if 'date' in df.columns:
            col = random.choice(cols[1:])  # 日付列を除外
            min_value = df[col].min()
            min_date = df.loc[df[col].idxmin(), 'date']
            min_date= min_date.strftime('%Y-%m-%d')
            questions.append(f"・列{col}が最小を取る日時はいつか?")
            answers.append(f"最小値は以下の手順で求められます。\n"
                        f"1. 列{col}の全ての値を確認する。\n"
                        f"列{col}の全ての値 = {df[col].values}\n"
                        f"2. 最小の値を特定する。\n"
                        f"{col}の最小値 = {min_value}\n"
                        f"3. 最小値を取る行の日時を確認する。\n"
                        f"最小値を取る日時 = {min_date}と判明しました｡")

        # 3. 列Yが最大を取るdateはいつか? (日付列がある場合)
            max_value = df[col].max()
            max_date = df.loc[df[col].idxmax(), 'date']
            max_date= max_date.strftime('%Y-%m-%d')
            questions.append(f"・列{col}が最大を取る日時はいつか?")
            answers.append(f"最大値は以下の手順で求められます。\n"
                        f"1. 列{col}の全ての値を確認する。\n"
                        f"列{col}の全ての値 = {df[col].values}\n"
                        f"2. 最大の値を特定する。\n"
                        f"{col}の最大値 = {max_value}\n"
                        f"3. 最大値を取る行の日時を確認する。\n"
                        f"最大値を取る日時 = {max_date}であることが分かりました｡")

        # 3. いくつの行があるか?
        questions.append("・いくつの行があるか?")
        answers.append(f"行数は以下のとおりです。\n"
                    f"行数 = {len(df)}")

        # 3. いくつの行があるか?
        questions.append("・いくつの列があるか?")
        answers.append(f"列の数は以下のとおりです｡\n"
                    f"列数 = {df.shape[1]}")

        # 4. 列X,Yはどちらが平均値が大きいか?
        col1, col2 = random.sample(cols[1:], 2)
        values1 = df[col1].values
        values2 = df[col2].values
        avg1 =np.round (df[col1].mean(),2)
        avg2 =np.round(df[col2].mean(),2)
        larger_col = col1 if avg1 > avg2 else col2
        questions.append(f"・列{col1},{col2}はどちらが平均値が大きいか?")
        answers.append(f"各列の平均値を以下の手順で比較します。\n"
                    f"1. 列{col1}の平均値を計算します。\n"
                    f"   {col1}の全ての値 = {values1}\n"
                    f"   {col1}の合計 = {values1.sum()}\n"
                    f"   {col1}の平均値 = {values1.sum()} / {len(values1)} = {avg1:.2f}\n"
                    f"2. 列{col2}の平均値を計算します。\n"
                    f"   {col2}の全ての値 = {values2}\n"
                    f"   {col2}の合計 = {values2.sum()}\n"
                    f"   {col2}の平均値 = {values2.sum()} / {len(values2)} = {avg2:.2f}\n"
                    f"3. どちらの平均値が大きいかを比較します。\n"
                    f"   以上より､平均値が大きいのは{larger_col}です｡")
        # 4. 列X,Yはどちらが平均値が小さいか?
        col1, col2 = random.sample(cols[1:], 2)
        values1 = df[col1].values
        values2 = df[col2].values
        avg1 =np.round (df[col1].mean(),2)
        avg2 =np.round(df[col2].mean(),2)
        larger_col = col1 if avg1 < avg2 else col2
        questions.append(f"・列{col1},{col2}はどちらが平均値が小さいか?")
        answers.append(f"各列の平均値を以下の手順で比較します。\n"
                    f"1. 列{col1}の平均値を計算します。\n"
                    f"   {col1}の全ての値 = {values1}\n"
                    f"   {col1}の合計 = {values1.sum()}\n"
                    f"   {col1}の平均値 = {values1.sum()} / {len(values1)} = {avg1:.2f}\n"
                    f"2. 列{col2}の平均値を計算します。\n"
                    f"   {col2}の全ての値 = {values2}\n"
                    f"   {col2}の合計 = {values2.sum()}\n"
                    f"   {col2}の平均値 = {values2.sum()} / {len(values2)} = {avg2:.2f}\n"
                    f"3. どちらの平均値が小さいかを比較します。\n"
                    f"   以上より､平均値が小さいのは{larger_col}です｡")
        # 5. 列Yの値が◯を取る列Xの値はいくつか? (数値をランダムに)
        col1, col2 = random.sample(cols[1:], 2)
        value = random.choice(df[col2].tolist())
        result = df[df[col2] == value][col1].tolist()
        questions.append(f"・列{col2}の値が{value}を取る列{col1}の値はいくつか?")
        answers.append(f"列{col2}の値が{value}の行を探した上で、その行の列{col1}の値を取得します。\n"
                    f"結果: {result}")
        # 7. 列Yの最大値はいくつか?
        col = random.choice(cols[1:])
        max_value = df[col].max()
        questions.append(f"・列{col}の最大値はいくつか?")
        answers.append(f"列{col}の最大値を以下の手順で求めます。\n"
                    f"1. 列{col}の全ての値を確認する。\n"
                    f"列{col}の全ての値 = {df[col].values}\n"
                    f"2. 最大の値を特定する。\n"
                    f"列{col}の最大値 = {max_value}です｡")
        # 7. 列Yの最大値はいくつか?
        col = random.choice(cols[1:])
        max_value = df[col].min()
        questions.append(f"・列{col}の最小値はいくつか?")
        answers.append(f"列{col}の最小値を以下の手順で求めます。\n"
                    f"1. 列{col}の全ての値を確認する。\n"
                    f"列{col}の全ての値 = {df[col].values}\n"
                    f"2. 最小の値を特定する。\n"
                    f"列{col}の最小値 = {max_value}です｡")

        # 10. 特定の行を抜き出してCSVとして出力せよ
        row_idx = random.sample(range(len(df)), random.randint(2, len(df)))
        questions.append(f"・行{row_idx}を抜き出してCSVとして出力せよ")
        row_data = df.iloc[row_idx]
        row_csv = row_data.to_csv(index=False)
        answers.append(f"以下の行データをCSV形式で出力した結果は以下のとおりです｡\n{row_csv}")

        # 11. 特定の列を抜き出してCSVとして出力せよ
        cols_sample = random.sample(cols, random.randint(2, len(cols)))
        questions.append(f"・列{cols_sample}を抜き出してCSVとして出力せよ")
        col_data = df[cols_sample]
        col_csv = col_data.to_csv(index=False)
        answers.append(f"以下の列データをCSVとして出力した結果は以下のとおりです。\n{col_csv}")

        return questions, answers

    # データフレームを作成
    df = pd.DataFrame(data)

    # データフレームを表示
    table_text = df.to_string()
    if random.random() < 0.5:
        table_text=table_text.strip()
        table_text=re.sub(r' +', ',', table_text)

    # 読解問題と回答を生成
    questions, answers = generate_questions(df)

    # ランダムに問題と回答のペアを選ぶ
    num_questions = random.randint(2, len(questions))
    selected_indices = random.sample(range(len(questions)), num_questions)
    questions = [questions[i] for i in selected_indices]
    answers = [answers[i] for i in selected_indices]

    text=f"""以下の表を読み取り、次の問いに答えなさい。\n{table_text}\n\n"""
    for i, q in enumerate(questions):
        text+=(q)+"\n"
        text+=(answers[i])+"\n\n"

    return text.strip()

save_dir="out_table"
n_records=100
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# ファイル名を現在の日付と時刻から生成
filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".jsonl"
filepath = os.path.join(save_dir, filename)

with open(filepath, 'a', encoding='utf-8') as f:
    for _ in tqdm(range(n_records), desc="Generating problems"):
        d = {"text": gen().strip()}
        json.dump(d, f, ensure_ascii=False)
        f.write("\n")

