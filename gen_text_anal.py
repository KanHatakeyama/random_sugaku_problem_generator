# %%

import datetime
import json
import os
from tqdm import tqdm
from datasets import load_dataset

# %%

import MeCab
from collections import Counter
import random


# MeCabの設定
mecab = MeCab.Tagger("-Ochasen")


def extract_nouns_adjectives(text):
    nouns = []
    adjectives = []

    # 形態素解析
    node = mecab.parseToNode(text)

    while node:
        features = node.feature.split(',')
        pos = features[0]
        if pos == '名詞':
            nouns.append(node.surface)
        elif pos == '形容詞':
            adjectives.append(node.surface)
        node = node.next

    return nouns, adjectives


def count_words(words):
    return Counter(words)


def find_word_positions(text, word):
    positions = []
    start = 0
    while start < len(text):
        start = text.find(word, start)
        if start == -1:
            break
        positions.append(start)
        start += len(word)
    return positions


def highlight_context(text, word, position, window=10):
    start = max(0, position - window)
    end = min(len(text), position + len(word) + window)
    return text[start:position] + f"({word})" + text[position+len(word):end]


# テキスト入力
text = """言語（げんご、language）は、狭義には「声による記号の体系」をいう。 広辞苑や大辞泉には次のように解説されている。 『日本大百科全書』では、「言語」という語は多義である、と解説され、大脳のに蓄えられた《語彙と文法規則の体系》を指すこともあり、その体系を用いる能力としてとらえることもある、と解説され、一方では、抽象的に「すべての人間が共有する言語能力」を指すこともあり、「個々の個別言語」を指すこともある、と解説されている。 広義の言語には、verbalな（言葉に表す）ものとnon-verbalな（言葉として表されない）もの（各種記号、アイコン、図形、ボディーランゲージ等）の両方を含み、日常のコミュニケーションでは狭義の言語表現に身振り、手振り、図示、擬音等も加えて表現されることもある。  """


def gen_q_a(text):
    # 名詞と形容詞を抽出
    nouns, adjectives = extract_nouns_adjectives(text)

    # カウント
    noun_counts = count_words(nouns)
    adjective_counts = count_words(adjectives)

    # 出現頻度が2回以上で、長さが1文字より大きい単語のみを抽出
    vocab_counts = {k: v for k, v in noun_counts.items() if v >
                    1 and len(k) > 1}
    adjective_counts = {k: v for k,
                        v in adjective_counts.items() if v > 1 and len(k) > 1}
    vocab_counts.update(adjective_counts)

    # 質問用に単語をランダムに選択
    n_ask_vocabs = min(random.randint(1, len(vocab_counts)), 5)
    ask_vocabs = random.sample(list(vocab_counts.keys()), n_ask_vocabs)

    # 問題文作成
    q_text = "問い: 以下の文章において、次の単語の出現頻度を数えなさい\n"
    q_text += "単語: " + ", ".join(ask_vocabs) + "\n\n"
    q_text += text + "\n\n"

    # 回答文作成
    a_text = "回答: 指定された単語の出現頻度と出現箇所は以下の通りです:\n\n"

    for vocab in ask_vocabs:
        positions = find_word_positions(text, vocab)
        a_text += f"単語: {vocab}\n"
        a_text += f"出現回数: {len(positions)}\n"
        for i, pos in enumerate(positions):
            context = highlight_context(text, vocab, pos)
            a_text += f"{i + 1}: ...{context}...\n"
        a_text += "\n"

    qa = q_text+a_text
    return qa

# gen_q_a2: 文章の数を数える


def gen_q_a2(text):
    # 文章を分割
    sentences = text.split('。')
    sentences = [s for s in sentences if len(s) > 2]

    # 問題文作成
    q_text = "問い: 以下の文章において、「｡」で区切られた文章の数を数えなさい\n\n"
    q_text += text + "\n\n"

    # 回答文作成
    a_text = f"回答: 文章の数は {len(sentences)} です。\n\n"

    qa = q_text + a_text
    return qa

# gen_q_a3: 名詞と形容詞を抽出する


def gen_q_a3(text):
    # 名詞と形容詞を抽出
    nouns, adjectives = extract_nouns_adjectives(text)

    # 問題文作成
    q_text = "問い: 以下の文章から名詞と形容詞を全て抽出しなさい\n\n"
    q_text += text + "\n\n"

    # 回答文作成
    a_text = "回答: 名詞と形容詞は以下の通りです:\n\n"
    a_text += "名詞: " + ", ".join(nouns) + "\n\n"
    a_text += "形容詞: " + ", ".join(adjectives) + "\n\n"

    qa = q_text + a_text
    return qa

# gen_q_a4: 指定された文字数以上の単語を抽出する


def gen_q_a4(text):
    nouns, adjectives = extract_nouns_adjectives(text)
    min_length = random.randint(2, 4)
    long_nouns = [word for word in nouns if len(word) >= min_length]
    q_text = f"問い: 以下の文章から、{min_length}文字以上の名詞を全て抽出しなさい\n\n" + text + "\n\n"
    a_text = f"回答: {min_length}文字以上の単語は以下の通りです:\n\n"
    a_text += "名詞: " + ", ".join(long_nouns) + "\n\n"
    if len(long_nouns) == 0:
        a_text += "該当する単語はありませんでした。\n\n"
    return q_text + a_text

# gen_q_a5: 特定の単語が含まれている文を抽出する


def gen_q_a5(text):
    nouns, _ = extract_nouns_adjectives(text)
    common_noun = random.choice(nouns)
    sentences = text.split('。')
    sentences = [s for s in sentences if len(s) > 2]
    containing_sentences = [s for s in sentences if common_noun in s]
    q_text = f"問い: 以下の文章から、単語「{common_noun}」を含む文をすべて抽出しなさい\n\n" + text + "\n\n"
    a_text = f"回答: 単語「{common_noun}」を含む文は以下の通りです:\n\n" + \
        "。".join(containing_sentences) + "\n\n"
    return q_text + a_text

# gen_q_a6: 文の長さを測定する


def gen_q_a6(text):
    sentences = text.split('。')
    sentences = [s for s in sentences if len(s) > 2]
    q_text = "問い: 以下の文章のそれぞれの文の長さを測定しなさい\n\n" + text + "\n\n"
    a_text = "回答: 各文の長さは以下の通りです:\n\n"
    for i, sentence in enumerate(sentences[:]):
        a_text += f"文{i + 1}: {len(sentence)}文字\n"
    return q_text + a_text

# gen_q_a7: 最も頻出する単語を見つける


def gen_q_a7(text):
    nouns, adjectives = extract_nouns_adjectives(text)
    all_words = nouns + adjectives
    word_counts = count_words(all_words)
    most_common_word, count = word_counts.most_common(1)[0]
    q_text = "問い: 以下の文章において、最も頻出する名詞または形容詞は何ですか？\n\n" + text + "\n\n"
    a_text = f"回答: 最も頻出する単語は「{most_common_word}」で、{count}回出現します。\n\n"
    return q_text + a_text

# gen_q_a8: 特定の単語の前後の単語を抽出する


def gen_q_a8(text):
    nouns, _ = extract_nouns_adjectives(text)
    common_noun = random.choice(nouns)
    positions = find_word_positions(text, common_noun)
    q_text = f"問い: 以下の文章において、単語「{common_noun}」の前後の文章を20文字程度で抽出しなさい\n\n" + text + "\n\n"
    a_text = f"回答: 単語「{common_noun}」の前後の文章は以下の通りです:\n\n"
    for pos in positions:
        before = text[max(0, pos - 10):pos].strip()
        after = text[pos + len(common_noun):min(len(text),
                                                pos + len(common_noun) + 10)].strip()
        a_text += f"出現位置: ...{before}({common_noun}){after}...\n"
    a_text += "\n"
    return q_text + a_text

# gen_q_a9: 単語の出現頻度とその割合を求める


def gen_q_a9(text):
    nouns, adjectives = extract_nouns_adjectives(text)
    all_words = nouns + adjectives
    word_counts = count_words(all_words)
    total_words = sum(word_counts.values())
    most_common_words = word_counts.most_common(5)
    q_text = "問い: 以下の文章において、最も頻出する単語5つの出現頻度を求めなさい\n\n" + text + "\n\n"
    a_text = "回答: 最も頻出する単語5つの出現頻度は以下の通りです:\n\n"
    for word, count in most_common_words:
        a_text += f"単語: {word}, 出現回数: {count}\n"
    a_text += "\n"
    return q_text + a_text


# gen_q_a14: テキストの最初と最後の文を抽出する
def gen_q_a14(text):
    sentences = text.split('。')
    sentences = [s for s in sentences if len(s) > 2]
    first_sentence = sentences[0] if sentences else ""
    last_sentence = sentences[-2] if len(sentences) > 1 else ""
    q_text = "問い: 以下の文章において、最初の文と最後の文を抽出しなさい\n\n" + text + "\n\n"
    a_text = f"回答: 最初の文は「{first_sentence}」、最後の文は「{last_sentence}」です。\n\n"
    return q_text + a_text
# gen_q_a16: 最も長い文を抽出する


def gen_q_a16(text):
    sentences = text.split('。')
    sentences = [s for s in sentences if len(s) > 2]
    longest_sentence = max(sentences, key=len, default="")
    q_text = "問い: 以下の文章において、最も長い文を抽出しなさい\n\n" + text + "\n\n"
    a_text = f"回答: 最も長い文は「{longest_sentence}」です。\n\n"
    return q_text + a_text
# gen_q_a19: 最も短い文を抽出する


def gen_q_a19(text):
    sentences = text.split('。')
    sentences = [s for s in sentences if len(s) > 2]
    shortest_sentence = min(sentences, key=len, default="")
    q_text = "問い: 以下の文章において、最も短い文を抽出しなさい\n\n" + text + "\n\n"
    a_text = f"回答: 最も短い文は「{shortest_sentence}」です。\n\n"
    return q_text + a_text


# 各関数を実行する
prob_functions = [gen_q_a, gen_q_a2, gen_q_a3, gen_q_a4, gen_q_a5, gen_q_a6, gen_q_a7, gen_q_a8, gen_q_a9,
                  gen_q_a14, gen_q_a16, gen_q_a19]


# %%
ds = load_dataset("izumi-lab/wikipedia-ja-20230720", split="train")

# %%
ds = ds.shuffle()

# %%
record_id = 0
n_problems = 10
max_text_length = 400


# %%

save_dir = "out_text"
n_records = 10**6
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# ファイル名を現在の日付と時刻から生成
filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".jsonl"
filepath = os.path.join(save_dir, filename)

with open(filepath, 'a', encoding='utf-8') as f:
    for record_id in tqdm(range(n_records)):
        record = ds[record_id]
        text = record["text"]
        sentences = text.split("。")
        sentences = [s for s in sentences if len(s) > 2]
        shorten_text = ""
        for t in sentences:
            if len(shorten_text)+len(t) < max_text_length:
                shorten_text += t+"。"
            else:
                break
        text = shorten_text
        gen = random.choice(prob_functions)
        try:
            problem = gen(text)
        except:
            continue
        d = {"text": problem.strip()}
        json.dump(d, f, ensure_ascii=False)
        f.write("\n")


# %%
