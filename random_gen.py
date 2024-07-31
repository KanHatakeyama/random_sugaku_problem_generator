from tqdm import tqdm
from src.problem_system import problem_generator_dict
import json
import datetime
import os
import time
def generate_problems(n_records=10**4, save_dir="out_random",target_keys=None):
    # 保存先ディレクトリが存在しない場合は作成
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # ファイル名を現在の日付と時刻から生成
    filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".jsonl"
    filepath = os.path.join(save_dir, filename)

    if target_keys is None:
        keys = problem_generator_dict.keys()
    else:
        keys = [target_keys]
    with open(filepath, 'a', encoding='utf-8') as f:
        for _ in tqdm(range(n_records), desc="Generating problems"):
            for key in keys:
                #st=time.time()
                generator = problem_generator_dict[key]
                #print("time:",time.time()-st,"key:",key)
                d = {"text": generator().strip()}
                json.dump(d, f, ensure_ascii=False)
                f.write("\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate problems and save to JSONL.")
    parser.add_argument('--n_records', type=int, default=10**4, help="Number of records to generate.")
    parser.add_argument('--save_dir', type=str, default="out_random", help="Directory to save JSONL files.")
    parser.add_argument('--target_key', type=str, default="", help="target genre to be generated")
    args = parser.parse_args()

    if args.target_key:
        target_keys = args.target_key
    else:
        target_keys = None

    generate_problems(n_records=args.n_records, save_dir=args.save_dir,target_keys=target_keys)
